#!/usr/bin/env python3
"""Print the SHA-256 hash index.html expects for an answer.

The page trims the typed answer and lowercases it before hashing.
"""

import hashlib
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print('usage: hash_answer.py "the answer"', file=sys.stderr)
        sys.exit(1)
    answer = " ".join(sys.argv[1:]).strip().lower()
    print(hashlib.sha256(answer.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
