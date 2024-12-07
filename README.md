---
# https://huggingface.co/docs/hub/en/spaces-config-reference
title: Chat
short_description: Serverless small language model inference
emoji: 🤖
colorFrom: blue
colorTo: yellow
sdk: gradio
sdk_version: 4.44.1
python_version: 3.11.9
app_file: app.py
fullWidth: false
pinned: true
header: mini
license: apache-2.0
preload_from_hub:
  - >-
    01-ai/Yi-Coder-1.5B-Chat
    config.json,generation_config.json,model.safetensors,special_tokens_map.json,tokenizer.model,tokenizer_config.json
  - >-
    HuggingFaceTB/SmolLM2-135M-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    HuggingFaceTB/SmolLM2-360M-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    HuggingFaceTB/SmolLM2-1.7B-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    ibm-granite/granite-3.0-2b-instruct
    added_tokens.json,config.json,merges.txt,model-00001-of-00002.safetensors,model-00002-of-00002.safetensors,model.safetensors.index.json,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    Qwen/Qwen2.5-0.5B-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    Qwen/Qwen2.5-1.5B-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    Qwen/Qwen2.5-Coder-1.5B-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    stabilityai/stablelm-2-zephyr-1_6b
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    THUDM/glm-edge-1.5b-chat
    config.json,generation_config.json,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json
---

# chat

Serverless small language model inference.

## Models

Ungated models under 2B parameters:

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
# clone
git clone https://huggingface.co/spaces/adamelliotfields/chat.git
cd chat

# install
uv venv
uv pip install -r requirements.txt

# gradio
source .venv/bin/activate
gradio app.py
```

## Development

### Auth

Use existing `HF_TOKEN`:

```sh
git remote set-url origin https://adamelliotfields:$HF_TOKEN@huggingface.co/spaces/adamelliotfields/chat
```

### PRs

See [pull requests and discussions](https://huggingface.co/docs/hub/en/repositories-pull-requests-discussions).

```sh
git fetch origin refs/pr/42:pr/42
git checkout pr/42
# ...
git add .
git commit -m "Commit message"
git push origin pr/42:refs/pr/42
```
