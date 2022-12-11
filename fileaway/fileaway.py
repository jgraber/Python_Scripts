import os
import sys
import shutil


def format_number(number):
    # https://python-reference.readthedocs.io/en/latest/docs/str/rjust.html
    return str(number).rjust(3, '0')


def collector(folder: str) -> set:
    result = set()
    for root, dirs, files in os.walk(folder):
        # print(f"{root}, {dirs}, {files}")
        for fileName in files:
            result.add(root.replace(folder, "") + os.sep + fileName)

    return result


def transform(files: set, prefix: str) -> dict:
    last_number_in_dir = {}
    result = {}
    
    for file in sorted(files, key=str.lower):
        last_index = file.rindex('\\')
        path, file_name = file[:last_index+1], file[last_index+1:]
        current = last_number_in_dir.get(path, 0)
        current = current + 1
        current_formatted = format_number(current)
        replaced_path = path.replace('\\', '_')
        suffix = file[file.rindex("."):]
        new_name = f'{prefix}_{replaced_path}{current_formatted}{suffix}'
        result[file] = new_name.replace("__", "_")
        last_number_in_dir[path] = current

    return result


def copy(source, target, files) -> None:
    for key, value in files.items():
        print(f"cp {source}{key} ==> {target}{value}")
        shutil.copy(f"{source}{key}", f"{target}{value}")


if __name__ == "__main__":
    args = sys.argv[1:]
    source = args[0]
    target = args[1]
    prefix = args[2]
    print(f"fileaway runs with {source} -> {target} and prefix {prefix}")

    files = collector(source)
    work = transform(files, prefix)
    copy(source, target, work)
