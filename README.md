# gradio-2b-chat

## Introduction

This is a simple Gradio chat UI for interacting with small langauge models.

## Models

All ungated models under 2B parameters:

- [01-ai/Yi-Coder-1.5B-Chat](https://huggingface.co/01-ai/Yi-Coder-1.5B-Chat)
- [HuggingFaceTB/SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct)
- [HuggingFaceTB/SmolLM2-360M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct)
- [HuggingFaceTB/SmolLM2-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct)
- [ibm-granite/granite-3.0-2b-instruct](https://huggingface.co/ibm-granite/granite-3.0-2b-instruct)
- [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
- [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
- [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct)
- [stabilityai/stablelm-2-zephyr-1_6b](https://huggingface.co/stabilityai/stablelm-2-zephyr-1_6b)
- [THUDM/glm-edge-1.5b-chat](https://huggingface.co/THUDM/glm-edge-1.5b-chat)

## Installation

```bash
# install
uv venv
uv pip install -r requirements.txt

# gradio
source .venv/bin/activate
gradio app.py
```
