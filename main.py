"""Potionomics Desktop — A local helper for Potionomics shop folders, brew notes, and card-week photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='potionomics_desktop',
        description='A local helper for Potionomics shop folders, brew notes, and card-week photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Potionomics Desktop')
    print('Keep the potion shop on disk before a market week.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
