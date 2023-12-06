#!/usr/bin/env python3
from pathlib import Path

from snakebids.app import SnakeBidsApp
from snakebids.plugins.validator import BidsValidator




def main():
    app = SnakeBidsApp(
        Path(__file__).resolve().parent,  # to get repository root
    )
    app.run_snakemake()


if __name__ == "__main__":
    main()
