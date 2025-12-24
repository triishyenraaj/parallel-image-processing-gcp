import os
import time

from pipeline import process_image


def run_sequential(image_paths, output_dir):
    """
    Run the image processing pipeline sequentially.

    Args:
        image_paths (list): List of image file paths
        output_dir (str): Directory to save output images

    Returns:
        float: Total execution time in seconds
    """
    start_time = time.perf_counter()

    for image_path in image_paths:
        process_image((image_path, output_dir))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return elapsed_time
