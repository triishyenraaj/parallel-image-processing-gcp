import csv
import os

from utils import get_image_paths, ensure_dir
from sequential import run_sequential
from multiprocessing_version import run_multiprocessing
from futures_version import run_futures


INPUT_DIR = "../data/input"
OUTPUT_DIR = "../data/output"
RESULTS_CSV = "../experiments/timings.csv"

WORKER_COUNTS = [2, 4, 8]


def main():
    # Prepare directories
    ensure_dir("experiments")
    ensure_dir(OUTPUT_DIR)

    # Load dataset
    image_paths = get_image_paths(INPUT_DIR)
    if not image_paths:
        raise RuntimeError("No images found in input directory.")

    results = []

    # 1. Sequential baseline
    print("Running sequential version...")
    seq_output = os.path.join(OUTPUT_DIR, "sequential")
    ensure_dir(seq_output)

    t_seq = run_sequential(image_paths, seq_output)
    results.append(("sequential", 1, t_seq, 1.0, 1.0))
    print(f"Sequential time: {t_seq:.4f} seconds")

    # 2. Multiprocessing runs
    for workers in WORKER_COUNTS:
        print(f"Running multiprocessing with {workers} processes...")
        mp_output = os.path.join(OUTPUT_DIR, f"multiprocessing_{workers}")
        ensure_dir(mp_output)

        t_mp = run_multiprocessing(image_paths, mp_output, workers)
        speedup = t_seq / t_mp
        efficiency = speedup / workers

        results.append(("multiprocessing", workers, t_mp, speedup, efficiency))
        print(f"Time: {t_mp:.4f} seconds | Speedup: {speedup:.2f} | Efficiency: {efficiency:.2f}")

    # 3. concurrent.futures runs
    for workers in WORKER_COUNTS:
        print(f"Running futures with {workers} workers...")
        fut_output = os.path.join(OUTPUT_DIR, f"futures_{workers}")
        ensure_dir(fut_output)

        t_fut = run_futures(image_paths, fut_output, workers)
        speedup = t_seq / t_fut
        efficiency = speedup / workers

        results.append(("futures", workers, t_fut, speedup, efficiency))
        print(f"Time: {t_fut:.4f} seconds | Speedup: {speedup:.2f} | Efficiency: {efficiency:.2f}")

    # Save results to CSV
    with open(RESULTS_CSV, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["mode", "workers", "time_seconds", "speedup", "efficiency"])
        writer.writerows(results)

    print("All experiments completed.")
    print(f"Results saved to {RESULTS_CSV}")



if __name__ == "__main__":
    main()
