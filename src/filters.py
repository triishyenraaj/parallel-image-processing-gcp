import cv2
import numpy as np


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image to grayscale using luminance formula.
    """
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray
    return image


def gaussian_blur(image: np.ndarray) -> np.ndarray:
    """
    Apply 3x3 Gaussian blur to the image.
    """
    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ], dtype=np.float32) / 16.0

    return cv2.filter2D(image, -1, kernel)


def sobel_edge(image: np.ndarray) -> np.ndarray:
    """
    Apply Sobel edge detection.
    """
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    magnitude = np.uint8(np.clip(magnitude, 0, 255))

    return magnitude


def sharpen(image: np.ndarray) -> np.ndarray:
    """
    Apply image sharpening using convolution.
    """
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float32)

    return cv2.filter2D(image, -1, kernel)


def adjust_brightness(image: np.ndarray, beta: int = 30) -> np.ndarray:
    """
    Adjust image brightness.
    beta > 0 increases brightness
    beta < 0 decreases brightness
    """
    adjusted = cv2.convertScaleAbs(image, alpha=1.0, beta=beta)
    return adjusted
