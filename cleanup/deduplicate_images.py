import os
import shutil
import hashlib
from typing import Set
from datetime import datetime
from pathlib import Path

from PIL import Image, ExifTags  # Requires: pip install Pillow
from tqdm import tqdm  # Requires: pip install tqdm


def get_image_checksum(file_path: Path) -> str:
    """Compute SHA-256 checksum of an image file."""
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def get_image_timestamp(file_path: Path) -> datetime:
    """Extract full datetime from EXIF metadata or fallback to file modification time."""
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        if exif_data:
            for tag, value in ExifTags.TAGS.items():
                if value == "DateTimeOriginal":
                    date_str = exif_data.get(tag)
                    if date_str:
                        return datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass

    # Fallback to file's modification timestamp
    return datetime.fromtimestamp(file_path.stat().st_mtime)


def deduplicate_and_sort_images(source_dir: Path, output_dir: Path) -> None:
    """Scan for image files, deduplicate by checksum, and store by year and timestamp filename."""
    checksums_seen: Set[str] = set()
    supported_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    # Gather all image files first for progress tracking
    image_files: list[Path] = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in supported_exts:
                image_files.append(file_path)

    # Process with progress bar
    for file_path in tqdm(image_files, desc="Processing images"):
        try:
            checksum = get_image_checksum(file_path)
        except Exception as e:
            tqdm.write(f"Error reading {file_path}: {e}")
            continue

        if checksum in checksums_seen:
            continue

        checksums_seen.add(checksum)

        try:
            timestamp = get_image_timestamp(file_path)
            year = str(timestamp.year)
            formatted_name = timestamp.strftime("%Y%m%d_%H%M%S")
            ext = file_path.suffix.lower()
            dest_folder = output_dir / year
            dest_folder.mkdir(parents=True, exist_ok=True)

            dest_file_path = dest_folder / f"{formatted_name}{ext}"

            # Append number suffix if name conflict
            counter = 1
            while dest_file_path.exists():
                dest_file_path = dest_folder / f"{formatted_name}_{counter}{ext}"
                counter += 1

            shutil.copy2(file_path, dest_file_path)
        except Exception as e:
            tqdm.write(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Deduplicate and organize images by year and timestamp.")
    parser.add_argument("source", type=str, help="Source directory with images.")
    parser.add_argument("output", type=str, help="Output directory for sorted images.")
    args = parser.parse_args()

    deduplicate_and_sort_images(Path(args.source), Path(args.output))

#python deduplicate_images.py /path/to/source /path/to/output/images