"""Command-line interface."""

import argparse

from capital_growth.calculator import projection


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compound interest projection")
    parser.add_argument("--initial", type=float, default=1000)
    parser.add_argument("--target", type=float, default=200000)
    parser.add_argument("--rate", type=float, default=0.03)
    args = parser.parse_args(argv)
    try:
        balances = projection(args.initial, args.target, args.rate)
    except ValueError as exc:
        parser.error(str(exc))
    for year, capital in enumerate(balances[1:], 1):
        print(f"capital={capital:.2f}\tannee={year}")
    print(f"Annees necessaires: {len(balances) - 1}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
