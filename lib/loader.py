import os

import torch
from transformers import (
    AutoConfig,
    Gemma2ForCausalLM,
    GemmaTokenizer,
    GlmForCausalLM,
    GPT2Tokenizer,
    LlamaForCausalLM,
    LlamaTokenizer,
    PreTrainedTokenizerFast,
    Qwen2ForCausalLM,
    Qwen2Tokenizer,
)


class Loader:
    def __init__(self):
        self.model = ""
        self.llm = None
        self.tokenizer = None

    def load(self, model):
        if model != self.model:
            token = os.getenv("HF_TOKEN", None)
            cuda_capability = torch.cuda.get_device_capability()[0]

            # Set device_map and low_cpu_mem_usage to stream weights from disk to GPU with Accelerate
            # See https://github.com/huggingface/transformers/blob/main/src/transformers/modeling_utils.py
            kwargs = {
                "token": token,
                "device_map": "auto",
                "low_cpu_mem_usage": True,
                "torch_dtype": torch.bfloat16 if cuda_capability >= 8 else torch.float16,
            }
            model_fns = {
                # Could have used auto-classes or a pipeline
                "01-ai/Yi-Coder-1.5B-Chat": LlamaForCausalLM.from_pretrained,
                "google/gemma-2-2b-it": Gemma2ForCausalLM.from_pretrained,
                "hugging-quants/Meta-Llama-3.1-8B-Instruct-BNB-NF4": LlamaForCausalLM.from_pretrained,
                "HuggingFaceTB/SmolLM2-135M-Instruct": LlamaForCausalLM.from_pretrained,
                "HuggingFaceTB/SmolLM2-360M-Instruct": LlamaForCausalLM.from_pretrained,
                "HuggingFaceTB/SmolLM2-1.7B-Instruct": LlamaForCausalLM.from_pretrained,
                "meta-llama/Llama-3.2-1B-Instruct": LlamaForCausalLM.from_pretrained,
                "Qwen/Qwen2.5-0.5B-Instruct": Qwen2ForCausalLM.from_pretrained,
                "Qwen/Qwen2.5-Coder-1.5B-Instruct": Qwen2ForCausalLM.from_pretrained,
                "THUDM/glm-edge-1.5b-chat": GlmForCausalLM.from_pretrained,
            }
            model_tokenizers = {
                "01-ai/Yi-Coder-1.5B-Chat": LlamaTokenizer,
                "google/gemma-2-2b-it": GemmaTokenizer,
                "hugging-quants/Meta-Llama-3.1-8B-Instruct-BNB-NF4": PreTrainedTokenizerFast,
                "HuggingFaceTB/SmolLM2-135M-Instruct": GPT2Tokenizer,
                "HuggingFaceTB/SmolLM2-360M-Instruct": GPT2Tokenizer,
                "HuggingFaceTB/SmolLM2-1.7B-Instruct": GPT2Tokenizer,
                "meta-llama/Llama-3.2-1B-Instruct": PreTrainedTokenizerFast,
                "Qwen/Qwen2.5-0.5B-Instruct": Qwen2Tokenizer,
                "Qwen/Qwen2.5-Coder-1.5B-Instruct": Qwen2Tokenizer,
                "THUDM/glm-edge-1.5b-chat": PreTrainedTokenizerFast,
            }

            llm_fn = model_fns[model]
            self.tokenizer = model_tokenizers[model].from_pretrained(model)

            if model == "hugging-quants/Meta-Llama-3.1-8B-Instruct-BNB-NF4":
                # Remove unused settings
                config = AutoConfig.from_pretrained(model)
                for key in ["_load_in_4bit", "_load_in_8bit", "quant_method"]:
                    del config.quantization_config[key]
                self.llm = llm_fn(model, config=config, **kwargs)
            else:
                self.llm = llm_fn(model, **kwargs)

            self.llm.eval()
            self.model = model

            # Clean up
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
            torch.cuda.reset_peak_memory_stats()
            torch.cuda.synchronize()


# Get a singleton or new instance
def get_loader(singleton=False):
    if not singleton:
        return Loader()
    else:
        if not hasattr(get_loader, "_instance"):
            get_loader._instance = Loader()
        return get_loader._instance
