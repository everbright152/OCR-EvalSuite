import argparse
from src.benchmark.runner import BenchmarkRunner


def main():
    parser = argparse.ArgumentParser(
        description="PolyOCR-Bench: Multilingual OCR Benchmarking Tool"
    )

    parser.add_argument(
        "--lang",
        type=str,
        default="eng",
        help="Language code (eng, hin, tam, etc.)"
    )

    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Path to dataset folder"
    )

    args = parser.parse_args()

    runner = BenchmarkRunner(
        dataset_path=args.dataset,
        lang=args.lang
    )

    runner.run()


if __name__ == "__main__":
    main()
    