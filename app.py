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
<div id="header">
    <div>
        <h1>Text</h1>
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 15 15">
            <path d="M7.48877 6.75C7.29015 6.75 7.09967 6.82902 6.95923 6.96967C6.81879 7.11032 6.73989 7.30109 6.73989 7.5C6.73989 7.69891 6.81879 7.88968 6.95923 8.03033C7.09967 8.17098 7.29015 8.25 7.48877 8.25C7.68738 8.25 7.87786 8.17098 8.0183 8.03033C8.15874 7.88968 8.23764 7.69891 8.23764 7.5C8.23764 7.30109 8.15874 7.11032 8.0183 6.96967C7.87786 6.82902 7.68738 6.75 7.48877 6.75ZM7.8632 0C11.2331 0 11.3155 2.6775 9.54818 3.5625C8.80679 3.93 8.47728 4.7175 8.335 5.415C8.69446 5.565 9.00899 5.7975 9.24863 6.0975C12.0195 4.5975 15 5.19 15 7.875C15 11.25 12.3265 11.325 11.4428 9.5475C11.0684 8.805 10.2746 8.475 9.57813 8.3325C9.42836 8.6925 9.19621 9 8.89665 9.255C10.3869 12.0225 9.79531 15 7.11433 15C3.74438 15 3.67698 12.315 5.44433 11.43C6.17823 11.0625 6.50774 10.2825 6.65751 9.5925C6.29056 9.4425 5.96855 9.2025 5.72891 8.9025C2.96555 10.3875 0 9.8025 0 7.125C0 3.75 2.666 3.6675 3.54967 5.445C3.92411 6.1875 4.71043 6.51 5.40689 6.6525C5.54918 6.2925 5.78882 5.9775 6.09586 5.7375C4.60559 2.97 5.1972 0 7.8632 0Z"></path>
        </svg>
    </div>
    <p>Serverless small language model inference.</p>
</div>
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

with gr.Blocks(head=HEAD, css="./app.css", fill_height=True) as demo:
    gr.HTML(HEADER)
    chat_interface.render()

if __name__ == "__main__":
    demo.queue(default_concurrency_limit=1).launch(
        server_name="0.0.0.0",
        server_port=PORT,
    )
