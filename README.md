---
# https://huggingface.co/docs/hub/en/spaces-config-reference
title: Text Generation
short_description: Simple app for small language model inference
emoji: ⌨️
colorFrom: blue
colorTo: yellow
sdk: gradio
sdk_version: 4.44.1
python_version: 3.11.9
app_file: app.py
fullWidth: false
pinned: false
header: default
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
    Qwen/Qwen2.5-0.5B-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    Qwen/Qwen2.5-Coder-1.5B-Instruct
    config.json,generation_config.json,merges.txt,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json,vocab.json
  - >-
    THUDM/glm-edge-1.5b-chat
    config.json,generation_config.json,model.safetensors,special_tokens_map.json,tokenizer.json,tokenizer_config.json
---

# text

Simple app for small language model inference.

## Installation

```bash
# clone
git clone https://huggingface.co/spaces/adamelliotfields/text.git
cd text
git remote set-url origin https://adamelliotfields:$HF_TOKEN@huggingface.co/spaces/adamelliotfields/text

# install
uv venv
uv pip install -r requirements.txt

# gradio
source .venv/bin/activate
gradio app.py
```

## Development

See [pull requests and discussions](https://huggingface.co/docs/hub/en/repositories-pull-requests-discussions).

```sh
git fetch origin refs/pr/42:pr/42
git checkout pr/42
# ...
git add .
git commit -m "Commit message"
git push origin pr/42:refs/pr/42
```
