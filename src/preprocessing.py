
import cv2


def preprocess_image(image_path):
    """
    Load and preprocess a product-label image
    for OCR.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            f"Could not read image: {image_path}"
        )

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    denoised = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    _, thresholded = cv2.threshold(
        denoised,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return thresholded
