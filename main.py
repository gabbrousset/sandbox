import argparse
import sys

from config import load


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("config")
    args = p.parse_args(argv)
    cfg = load(args.config)
    print(cfg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
