import mailbox
from email.header import decode_header
from typing import List, Optional, Dict
from collections import defaultdict
from tqdm import tqdm  # Progress bar

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

def collect_label_frequencies(mbox_path: str) -> Dict[str, int]:
    """
    Scans the mbox and counts frequency of all labels found in X-Gmail-Labels.
    """
    freq = defaultdict(int)
    mbox = mailbox.mbox(mbox_path)
    for msg in tqdm(mbox, desc="Scanning labels"):
        raw = msg.get('X-Gmail-Labels', '')
        for label in decode_labels(raw):
            freq[label] += 1
    return dict(freq)

def sort_labels_by_priority(labels: List[str], global_priority: List[str]) -> Optional[str]:
    """
    Selects the most significant label based on global priority order.
    """
    for candidate in global_priority:
        if candidate in labels:
            return candidate
    return None

def is_read(labels: List[str]) -> bool:
    """
    Determines if the email is marked as read based on the label list.
    """
    return "Geöffnet" in labels or "Gelesen" in labels or "Ungelesen" not in labels

def infer_label_priority(freq_map: Dict[str, int]) -> List[str]:
    """
    Builds a priority list dynamically by filtering generic labels and sorting the rest by frequency.
    """
    ignored = {"Archiviert", "Ungelesen", "Geöffnet", "Kategorie: \"Neuigkeiten\"", "Kategorie: \"Persönlich\""}
    candidates = {k: v for k, v in freq_map.items() if k not in ignored}
    return sorted(candidates, key=candidates.get, reverse=True)

def process_mbox(input_file: str, output_file: str) -> None:
    """
    Processes emails from input_file, categorizes them based on labels,
    and writes them to output_file with relevant label and read status.
    """
    freq_map = collect_label_frequencies(input_file)
    dynamic_priority = infer_label_priority(freq_map)

    mbox_in = mailbox.mbox(input_file)
    mbox_out = mailbox.mbox(output_file)

    for msg in tqdm(mbox_in, desc="Processing messages"):
        raw_labels = msg.get('X-Gmail-Labels', '')
        labels = decode_labels(raw_labels)
        significant = sort_labels_by_priority(labels, dynamic_priority)
        read_status = is_read(labels)

        if significant:
            msg['X-Sorted-Label'] = significant
        msg['X-Is-Read'] = str(read_status)

        mbox_out.add(msg)

    mbox_out.flush()

if __name__ == "__main__":
    process_mbox("allmails.mbox", "sorted_mails.mbox")
