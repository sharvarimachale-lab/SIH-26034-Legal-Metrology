
import pytesseract

from preprocessing import preprocess_image


def extract_text(image_path):
    """
    Convert a product image into OCR text.
    """

    processed_image = preprocess_image(
        image_path
    )

    text = pytesseract.image_to_string(
        processed_image,
        config="--psm 6"
    )

    return text
