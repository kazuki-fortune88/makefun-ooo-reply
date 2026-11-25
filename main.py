"""Write the funniest one-line out-of-office reply to entry.txt.

The reply is a real away message with a fresh twist: instead of promising
answers "in the order received", it promises answers in the order the
emails stop mattering. Short, stands alone, no name or signature needed.
"""

import os

LINE = "I'm away until Friday \u2014 my emails will be answered in the order they stop mattering."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never delete the output directory itself: on the grader it is a
    # mount point. Just make sure it exists.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
