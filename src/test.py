from futures_version import run_futures
from utils import get_image_paths

def main():
    paths = get_image_paths("../data/input")

    t = run_futures(
        paths,
        "../data/output/futures",
        num_workers=8
    )

    print("Futures time:", t)

if __name__ == "__main__":
    main()