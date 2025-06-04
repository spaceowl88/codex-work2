from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Meme-Coin Spike Hunter")
    parser.add_argument(
        "--handles", type=str, default="", help="Comma-separated Twitter handles"
    )
    parser.add_argument(
        "--keywords", type=str, default="", help="Comma-separated keywords"
    )
    args = parser.parse_args()

    handles = [h.strip() for h in args.handles.split(",") if h.strip()]
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]

    print(f"Monitoring handles: {handles}")
    print(f"Keywords: {keywords}")


if __name__ == "__main__":
    main()
