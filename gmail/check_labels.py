import re
from collections import defaultdict
from email.header import decode_header
from typing import List
from tqdm import tqdm

def decode_labels(raw_header: str) -> List[str]:
    """
    Decodes MIME-encoded Gmail labels into a list of strings.
    """
    decoded_parts = decode_header(raw_header)
    decoded_string = ''.join(
        part.decode(enc or 'utf-8') if isinstance(part, bytes) else part
        for part, enc in decoded_parts
    )
    return [label.strip() for label in decoded_string.split(',')]

def count_lines(filepath: str) -> int:
    """
    Counts the number of lines in the file.
    Used to initialize tqdm with a total.
    """
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        return sum(1 for _ in f)

def collect_label_frequencies_from_file(filepath: str) -> defaultdict:
    """
    Scans the file line by line and counts Gmail label frequencies,
    showing a tqdm progress bar based on total lines.
    """
    label_pattern = re.compile(r'^X-Gmail-Labels:\s*(.*)', re.IGNORECASE)
    freq = defaultdict(int)

    total_lines = count_lines(filepath)

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f, tqdm(total=total_lines, desc="Scanning for labels") as pbar:
        for line in f:
            pbar.update(1)
            match = label_pattern.match(line)
            if match:
                raw_header = match.group(1).strip()
                labels = decode_labels(raw_header)
                for label in labels:
                    freq[label] += 1

    return freq

def main():
    mbox_file = "allmails.mbox"  # Change path if needed
    freq_map = collect_label_frequencies_from_file(mbox_file)

    print("\nLabel Frequencies:")
    for label, count in sorted(freq_map.items(), key=lambda x: x[1], reverse=True):
        print(f"{label}: {count}")

if __name__ == "__main__":
    main()
