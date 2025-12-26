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

```text
image_parallel_project/
│
├── data/
│   ├── input/                 # Generated dataset subset (ignored by git)
│   └── output/                # Processed images (ignored by git)
│   └── prepare_input_dataset.py
│
├── experiments/
│   └── timings.csv            # Execution results (ignored by git)
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
```
---

## 📂 Dataset Management

The Food-101 dataset is organised into class-based subdirectories.  
A reproducible subset is created using a provided script that selects **10 images per class** (~1000 images total).

The loader function automatically flattens all class folders, allowing the pipeline to remain independent of dataset structure.

---

▶️ How to Run on Google Cloud Platform (GCP)

### 1️⃣ GCP Account & Project (Once Only)
1. Go to [Google Cloud Console](https://console.cloud.google.com/) and sign in.
2. Create a new project:
   - Click **Project Selector → New Project**
   - Name example: `CST435-Parallel-Image-Processing`
   
📌 **Why:** Keeps billing/resources clean and professional.

---

### 2️⃣ Create the Virtual Machine (VM)
1. Go to **Compute Engine → VM instances → Create Instance**
2. Configure VM:
   - **Name:** `cst435-image-parallel`
   - **Region / Zone:** Any (e.g., `asia-southeast1`)
   - **Machine Configuration:**
     - Series: `E2`
     - Machine type: `e2-standard-8` (8 vCPUs, enough RAM for experiments)
   - **Boot Disk:** default or Ubuntu 20.04 LTS or 22.04 LTS 
   - **Firewall:** ✔ Allow HTTP, ✔ Allow HTTPS (optional)
3. Click **Create** (~30 seconds to launch)

---

### 3️⃣ Connect to the VM
- Click **SSH → Open in browser window**  
  You now have a Linux terminal on the cloud VM.  

📌 This is what you will show in your demo video.

---

### 4️⃣ Set Up Python Environment
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
pip3 --version

sudo apt install git
git --version
```

---

### 5️⃣ Clone the GitHub Repository

#### **Option A: SSH Key Setup (Recommended)**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "nandanjunior@github"
# Press Enter for defaults, Enter twice for no passphrase

# Copy public key
cat ~/.ssh/id_ed25519.pub
```
- Copy the **entire output** starting with `ssh-ed25519`.
- Add to GitHub: [SSH Keys](https://github.com/settings/ssh/new)
  - **Title:** Google Cloud CST435
  - **Key:** paste copied key
- Test SSH connection (optional):
```bash
ssh -T git@github.com
```
- Expected output:
```
Hi nandanjunior! You've successfully authenticated, but GitHub does not provide shell access.
```

- Clone the repository:
```bash
cd ~
git clone git@github.com:nandanjunior/cpc357-assg2.git
cd cpc357-assg2
```

#### **Option B: HTTPS + PAT (Alternative)**
```bash
git clone https://github.com/nandanjunior/cpc357-assg2.git
# When prompted:
# Username: nandanjunior
# Password: <paste your Personal Access Token>
```
---

### 6️⃣ Activate Virtual Environment & Install Python Dependencies
```bash
python3 -m venv venv
source venv/bin/activate

# Inside your virtual environment
pip install -r requirements.txt

# If requirements.txt is missing or incomplete
pip install numpy opencv-python 
```

---

### 7️⃣ Install OpenCV System Dependencies
On minimal Linux VM, OpenCV may fail due to missing libraries:
```bash
sudo apt install -y libgl1
```
✅ This ensures no `libGL.so.1` import errors occur.

---

### 8️⃣ Run the Project
With the virtual environment active:
```bash
cd src
python3 main.py
```

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
