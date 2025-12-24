import time
import os
from multiprocessing import Pool, cpu_count

from pipeline import process_image


def run_multiprocessing(image_paths, output_dir, num_processes):
    """
    Run the image processing pipeline using multiprocessing.

    Args:
        image_paths (list): List of image file paths
        output_dir (str): Directory to save output images
        num_processes (int): Number of worker processes

    Returns:
        float: Total execution time in seconds
    """
    # Prepare arguments for each task
    tasks = [(image_path, output_dir) for image_path in image_paths]

    start_time = time.perf_counter()

    with Pool(processes=num_processes) as pool:
        pool.map(process_image, tasks)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return elapsed_time
