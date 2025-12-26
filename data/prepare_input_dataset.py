import os
import random
import shutil

# =========================
# CONFIGURATION
# =========================
SOURCE_DATASET = r"C:\cst435\food-101\food-101\images"     # Original Food-101 images
TARGET_DATASET = "../data/input"     # Subset used in experiments
IMAGES_PER_CLASS = 10
SEED = 42


def prepare_dataset():
    random.seed(SEED)

    if not os.path.exists(SOURCE_DATASET):
        raise RuntimeError(f"Source dataset not found: {SOURCE_DATASET}")

    os.makedirs(TARGET_DATASET, exist_ok=True)

    class_names = sorted(os.listdir(SOURCE_DATASET))
    total_images = 0

    for class_name in class_names:
        class_path = os.path.join(SOURCE_DATASET, class_name)
        if not os.path.isdir(class_path):
            continue

        images = [
            f for f in os.listdir(class_path)
            if f.lower().endswith(".jpg")
        ]

        if len(images) < IMAGES_PER_CLASS:
            print(f"Skipping {class_name}: not enough images")
            continue

        selected_images = random.sample(images, IMAGES_PER_CLASS)

        target_class_dir = os.path.join(TARGET_DATASET, class_name)
        os.makedirs(target_class_dir, exist_ok=True)

        for img in selected_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(target_class_dir, img)
            shutil.copy2(src, dst)

        total_images += IMAGES_PER_CLASS
        print(f"{class_name}: {IMAGES_PER_CLASS} images selected")

    print(f"\nDataset preparation completed.")
    print(f"Total images copied: {total_images}")


if __name__ == "__main__":
    prepare_dataset()
