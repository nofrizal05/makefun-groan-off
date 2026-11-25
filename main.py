import os

LINE = "My calendar went to therapy because every single day it has to face another date — and not one of them has ever called it back for a second one."

if "\n" in LINE or "\r" in LINE:
    raise ValueError("entry must be a single line")
if len(LINE) > 280:
    raise ValueError("entry exceeds 280 characters")

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
