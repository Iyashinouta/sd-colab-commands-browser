import os
import gradio as gr
from modules import scripts, script_callbacks
from subprocess import getoutput

def run(command):
    out = getoutput(f"{command}")
    return out

def on_ui_tabs():     
    with gr.Blocks() as terminal:
        gr.Markdown(
        """
        ### Google Colab Manually Run Command
        ```py
        Example : pip, git, curl, wget, aria2c, or something else (no need to add "!,$,#"etc. in first code)
        ```
        """)
        with gr.Group():
            with gr.Box():
                command = gr.Textbox(label="Input Command Here", max_lines=1, placeholder="command")
                out_text = gr.Textbox(label="Output Results (no need to scroll down if the output code has appeared, if the output code appears, the code sign is complete)", placeholder="outputs")
                btn_run = gr.Button("run command")
                btn_run.click(fn=run, inputs=command, outputs=out_text)
    return (terminal, "Colab Terminal", "terminal"),
script_callbacks.on_ui_tabs(on_ui_tabs)
