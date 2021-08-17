#! /usr/bin/env python3

from os import remove
from pathlib import Path

exts_to_clean = {'.mp4', '.gif', '.jpg', '.jpeg', '.png', '.svg'}
for d in (Path.home() / 'Desktop').iterdir():
    if d.suffix in exts_to_clean:
        remove(d)
