# CST435 – Parallel Image Processing on Google Cloud Platform

## Course
CST435: Parallel and Cloud Computing  
Universiti Sains Malaysia

## Assignment
Assignment 2 – Parallel Image Processing System

---

## 📌 Project Overview

This project implements a **parallel image processing system** that applies multiple image filters to a subset of the **Food-101 dataset**. The same image processing pipeline is executed using different **parallel programming paradigms** to analyze performance, scalability, speedup, and efficiency.

All experiments are designed to be **reproducible**, **dataset-agnostic**, and suitable for execution on **Google Cloud Platform (GCP)** or local multi-core systems.

---

## 🎯 Objectives

- Design a multi-stage image processing pipeline
- Implement parallel execution using multiple paradigms
- Compare performance against a sequential baseline
- Measure execution time, speedup, and efficiency
- Apply parallel computing theory (Amdahl’s Law)
- Demonstrate good software engineering practices

---

## 🖼 Image Processing Pipeline

Each image is processed sequentially through the following filters:

1. Grayscale Conversion  
2. Gaussian Blur (3×3 kernel)  
3. Sobel Edge Detection  
4. Image Sharpening  
5. Brightness Adjustment  

The pipeline is identical across all execution modes to ensure **fair comparison**.

---

## ⚙️ Execution Modes (Parallel Paradigms)

### 1️⃣ Sequential (Baseline)
- Single-process execution
- Used as reference for performance comparison

### 2️⃣ multiprocessing
- Implemented using `multiprocessing.Pool`
- True parallelism via OS-level processes
- Explicit control over worker count

### 3️⃣ concurrent.futures
- Implemented using `ProcessPoolExecutor`
- Higher-level abstraction for process management
- Cleaner task scheduling and error handling

---

## ☁️ Cloud Deployment

Experiments can be executed on:
- Google Cloud Platform (Compute Engine)
- Ubuntu Linux VM
- Multi-core CPU environment

The system is also compatible with local machines.

---

## 📊 Performance Metrics

- Execution Time (seconds)
- Speedup  

Speedup = T_sequential / T_parallel

- Efficiency  

Efficiency = Speedup / Number_of_Workers

Speedup and efficiency are computed programmatically for consistency and reproducibility.

---

## 📁 Project Structure

image_parallel_project/
│
├── data/
│   ├── input/                 # Generated dataset subset (ignored by git)
│   └── output/                # Processed images (ignored by git)
│
├── experiments/
│   └── timings.csv            # Execution results (ignored by git)
│
├── scripts/
│   └── prepare_input_dataset.py
│
├── src/
│   ├── filters.py
│   ├── pipeline.py
│   ├── sequential.py
│   ├── multiprocessing_version.py
│   ├── futures_version.py
│   ├── utils.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md

---

## 📂 Dataset Management

The Food-101 dataset is organised into class-based subdirectories.  
A reproducible subset is created using a provided script that selects **10 images per class** (~1000 images total).

The loader function automatically flattens all class folders, allowing the pipeline to remain independent of dataset structure.

---

## ▶️ How to Run

1. Install dependencies  
   pip install numpy opencv-python

2. Prepare dataset  
   python scripts/prepare_input_dataset.py

3. Run experiments  
   python src/main.py

---

## 📈 Output

Results are saved in:
experiments/timings.csv

Including:
- mode
- workers
- time_seconds
- speedup
- efficiency

---

## 🧹 Version Control

Datasets, outputs, and experiment results are excluded via `.gitignore` to keep the repository clean and lightweight.

---

## 📜 License

Academic use only – CST435 coursework.
