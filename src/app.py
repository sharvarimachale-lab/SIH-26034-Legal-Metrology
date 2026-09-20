
import gradio as gr


def analyze_demo():
    return """
MRP: DETECTED | 120
Net Quantity: DETECTED | 500 g
Manufacturer: DETECTED | ABC Foods Pvt Ltd
Manufacturing Date: DETECTED | 01/08/2026
Consumer Care: DETECTED | 1800-123-4567
"""


with gr.Blocks(
    title="Legal Metrology Compliance Checker"
) as demo:

    gr.Markdown(
        """
        # Legal Metrology Compliance Checker

        Upload a packaged commodity label image
        and analyze its declarations.
        """
    )

    image_input = gr.Image(
        type="filepath",
        label="Upload Product Image"
    )

    analyze_button = gr.Button(
        "Analyze Product"
    )

    result_output = gr.Textbox(
        label="Compliance Results",
        lines=10
    )

    analyze_button.click(
        fn=analyze_demo,
        inputs=[],
        outputs=result_output
    )


if __name__ == "__main__":
    demo.launch(share=True)
