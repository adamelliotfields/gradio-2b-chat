from threading import Thread
from typing import Iterator

from spaces import GPU, config
from transformers import TextIteratorStreamer

from .loader import get_loader


@GPU
def generate(
    message: str,
    chat_history: list[dict[str, str]],
    system_message="",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    max_tokens=512,
    temperature=0.6,
    repetition_penalty=1.2,
    top_p=0.9,
    top_k=50,
) -> Iterator[str]:
    # Prepend system prompt
    if not chat_history or chat_history[0].get("role") != "system":
        chat_history.insert(0, {"role": "system", "content": system_message})
    else:
        chat_history[0]["content"] = system_message

    # Append user message before generating
    chat_history.append({"role": "user", "content": message})

    yield from transformers_generate(
        chat_history,
        model,
        max_tokens,
        temperature,
        repetition_penalty,
        top_p,
        top_k,
    )


def transformers_generate(
    chat_history: list[dict[str, str]],
    model: str,
    max_tokens: int,
    temperature: float,
    repetition_penalty: float,
    top_p: float,
    top_k: int,
) -> Iterator[str]:
    loader = get_loader(singleton=not config.Config.zero_gpu)
    loader.load(model)

    llm = loader.llm
    tokenizer = loader.tokenizer

    # Handle models that don't have a padding token
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    # https://huggingface.co/docs/transformers/main/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.apply_chat_template
    results = tokenizer.apply_chat_template(
        chat_history,
        tokenize=True,
        return_dict=True,  # get the attention mask
        return_tensors="pt",
        # https://huggingface.co/docs/transformers/chat_templating#what-are-generation-prompts
        add_generation_prompt=True,
    )

    input_ids = results["input_ids"].to(llm.device)
    attention_mask = results["attention_mask"].to(llm.device)

    streamer = TextIteratorStreamer(
        tokenizer,
        skip_prompt=True,
        skip_special_tokens=True,
    )

    # https://huggingface.co/blog/how-to-generate
    generate_kwargs = dict(
        do_sample=True,
        streamer=streamer,
        input_ids=input_ids,
        attention_mask=attention_mask,
        pad_token_id=tokenizer.pad_token_id,
        top_p=top_p,
        top_k=top_k,
        temperature=temperature,
        max_new_tokens=max_tokens,
        repetition_penalty=repetition_penalty,
    )

    # Stream text off the main thread
    t = Thread(target=llm.generate, kwargs=generate_kwargs)
    t.start()

    # Collect output tokens
    outputs = []
    for text in streamer:
        outputs.append(text)
        yield "".join(outputs)
