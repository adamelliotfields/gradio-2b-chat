from transformers import (
    GlmForCausalLM,
    GPT2TokenizerFast,
    GraniteForCausalLM,
    LlamaForCausalLM,
    LlamaTokenizerFast,
    PreTrainedTokenizerFast,
    Qwen2ForCausalLM,
    Qwen2TokenizerFast,
    StableLmForCausalLM,
)

CONFIG = {
    "01-ai/Yi-Coder-1.5B-Chat": {
        "model": LlamaForCausalLM,
        "tokenizer": LlamaTokenizerFast,
    },
    "HuggingFaceTB/SmolLM2-135M-Instruct": {
        "model": LlamaForCausalLM,
        "tokenizer": GPT2TokenizerFast,
    },
    "HuggingFaceTB/SmolLM2-360M-Instruct": {
        "model": LlamaForCausalLM,
        "tokenizer": GPT2TokenizerFast,
    },
    "HuggingFaceTB/SmolLM2-1.7B-Instruct": {
        "model": LlamaForCausalLM,
        "tokenizer": GPT2TokenizerFast,
    },
    "ibm-granite/granite-3.0-2b-instruct": {
        "model": GraniteForCausalLM,
        "tokenizer": GPT2TokenizerFast,
    },
    "Qwen/Qwen2.5-0.5B-Instruct": {
        "model": Qwen2ForCausalLM,
        "tokenizer": Qwen2TokenizerFast,
    },
    "Qwen/Qwen2.5-1.5B-Instruct": {
        "model": Qwen2ForCausalLM,
        "tokenizer": Qwen2TokenizerFast,
    },
    "Qwen/Qwen2.5-Coder-1.5B-Instruct": {
        "model": Qwen2ForCausalLM,
        "tokenizer": Qwen2TokenizerFast,
    },
    "stabilityai/stablelm-2-zephyr-1_6b": {
        "model": StableLmForCausalLM,
        "tokenizer": GPT2TokenizerFast,
    },
    "THUDM/glm-edge-1.5b-chat": {
        "model": GlmForCausalLM,
        "tokenizer": PreTrainedTokenizerFast,
    },
}
