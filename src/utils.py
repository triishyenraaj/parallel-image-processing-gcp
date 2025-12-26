import os


def get_image_paths(input_dir):
    """
    Recursively collect all image file paths from input_dir.

    This function supports datasets organized into class subdirectories
    and returns a flat list of image paths.

    Args:
        input_dir (str): Root input directory

    Returns:
        list: List of full image file paths
    """
    image_paths = []

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_paths.append(os.path.join(root, file))

    image_paths.sort()
    return image_paths


def ensure_dir(path):
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
