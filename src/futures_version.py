import time
import os
from concurrent.futures import ProcessPoolExecutor, as_completed

from pipeline import process_image


def run_futures(image_paths, output_dir, num_workers):
    """
    Run the image processing pipeline using concurrent.futures.

    Args:
        image_paths (list): List of image file paths
        output_dir (str): Directory to save output images
        num_workers (int): Number of worker processes

    Returns:
        float: Total execution time in seconds
    """
    tasks = [(image_path, output_dir) for image_path in image_paths]

    start_time = time.perf_counter()

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(process_image, task) for task in tasks]

        # Ensure all tasks complete
        for future in as_completed(futures):
            future.result()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return elapsed_time
