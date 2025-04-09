import os

import torch

from .config import CONFIG


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

            config = CONFIG[model]
            self.tokenizer = config["tokenizer"].from_pretrained(model)
            self.llm = config["model"].from_pretrained(model, **kwargs)
            self.llm.eval()
            self.model = model

            # Clean up
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
            torch.cuda.reset_peak_memory_stats()
            torch.cuda.synchronize()


# Get a singleton
def get_loader():
    if not hasattr(get_loader, "_instance"):
        get_loader._instance = Loader()
    return get_loader._instance
