import os
import cv2
import numpy as np

from filters import (
    to_grayscale,
    gaussian_blur,
    sobel_edge,
    sharpen,
    adjust_brightness
)


def process_image(args):
    """
    Apply the full image processing pipeline to a single image.

    Args:
        args (tuple): (image_path, output_dir)

    Returns:
        None
    """
    image_path, output_dir = args

    # Load image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image: {image_path}")

    # Apply filters in fixed order
    image = to_grayscale(image)
    image = gaussian_blur(image)
    image = sobel_edge(image)
    image = sharpen(image)
    image = adjust_brightness(image, beta=30)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save processed image
    filename = os.path.basename(image_path)
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, image)
