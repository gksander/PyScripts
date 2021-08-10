from os import remove
from pathlib import Path

video_suffixes = ['.mp4', '.gif']
for d in (Path.home() / 'Desktop').iterdir():
    if d.suffix in video_suffixes:
        remove(d)
