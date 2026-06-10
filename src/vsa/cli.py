import argparse


def main():
    parser = argparse.ArgumentParser(description="VSA CLI")

    parser.add_argument("input", nargs="?")

    args = parser.parse_args()

    print("VSA CLI placeholder")
    print(f"Input: {args.input}")


if __name__ == "__main__":
    main()
