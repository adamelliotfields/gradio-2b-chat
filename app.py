import random

import gradio as gr
import numpy as np
import torch

from lib import CONFIG, generate

HEAD = """
<style>
    @media (min-width: 1536px) {
        gradio-app > .gradio-container { max-width: 1280px !important }
    }
</style>
"""

HEADER = """
# Chat 🤖

Serverless small language model inference.
"""

SEED = 0
PORT = 7860

if gr.NO_RELOAD:
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)

chatbot = gr.Chatbot(type="messages", show_label=False, height=None, scale=1)
textbox = gr.Textbox(placeholder="Type a message...", autofocus=True, scale=7)

# https://github.com/gradio-app/gradio/blob/main/gradio/chat_interface.py
chat_interface = gr.ChatInterface(
    title=None,
    fn=generate,
    chatbot=chatbot,
    textbox=textbox,
    type="messages",  # interface type must match bot type
    description=None,
    additional_inputs=[
        gr.Textbox(
            label="System Message",
            lines=2,
            value="You are a helpful assistant. Be concise and precise.",
        ),
        gr.Dropdown(
            label="Model",
            filterable=False,
            value="Qwen/Qwen2.5-0.5B-Instruct",
            choices=list(CONFIG.keys()),
        ),
        gr.Slider(
            label="Max new tokens",
            minimum=1,
            maximum=2048,
            step=1,
            value=512,
            info="Maximum number of new tokens to generate.",
        ),
        gr.Slider(
            label="Temperature",
            minimum=0.1,
            maximum=2.0,
            step=0.1,
            value=0.6,
            info="Modulates next token probabilities.",
        ),
        gr.Slider(
            # https://arxiv.org/abs/1909.05858
            label="Repetition penalty",
            minimum=1.0,
            maximum=2.0,
            step=0.05,
            value=1.2,
            info="Penalizes repeating tokens.",
        ),
        gr.Slider(
            # https://arxiv.org/abs/1904.09751
            label="Top-p",
            minimum=0.05,
            maximum=1.0,
            step=0.05,
            value=0.9,
            info="Only tokens with cumulative probability p are considered (nucleus sampling).",
        ),
        gr.Slider(
            # https://arxiv.org/pdf/1805.04833
            label="Top-k",
            minimum=1,
            maximum=100,
            step=1,
            value=50,
            info="Only k-th highest probability tokens are considered.",
        ),
    ],
)

with gr.Blocks(head=HEAD, fill_height=True) as demo:
    gr.Markdown(HEADER)
    chat_interface.render()

if __name__ == "__main__":
    demo.queue(default_concurrency_limit=1).launch(
        server_name="0.0.0.0",
        server_port=PORT,
    )
