import os


def get_image_paths(input_dir):
    """
    Get a sorted list of image file paths from the input directory.

    Args:
        input_dir (str): Directory containing input images

    Returns:
        list: List of full image file paths
    """
    valid_extensions = (".jpg", ".jpeg", ".png")
    image_paths = []

    for file in os.listdir(input_dir):
        if file.lower().endswith(valid_extensions):
            image_paths.append(os.path.join(input_dir, file))

    image_paths.sort()
    return image_paths


def ensure_dir(path):
    """
    Create directory if it does not exist.
    """
    os.makedirs(path, exist_ok=True)
