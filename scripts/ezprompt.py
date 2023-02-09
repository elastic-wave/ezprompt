import contextlib
from pathlib import Path

import gradio as gr

import modules.scripts as scripts
from modules.ui_components import ToolButton

ezprompt_dir = scripts.basedir()

class Script(scripts.Script):
    def title(self):
        return "EZPrompt"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        return []

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui:
        with gr.Column():
            with gr.Tabs():
                with gr.TabItem(label="Single"):
                    with gr.Row().style(equal_height=False):
                        with gr.Column():
                            # with gr.Tabs():
                            image = gr.Image(
                                source="upload",
                                label="Image",
                                interactive=True,
                                type="pil",
                            )

                            single_start_btn = gr.Button(
                                value="Judge", variant="primary"
                            )

    return [(ui, "EZPrompt", "ezprompt") ]     

script_callbacks.on_ui_tabs(on_ui_tabs)                                                          
