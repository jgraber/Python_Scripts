import os
import sys
import shutil


def collector(folder: str) -> set:
    result = set()
    for root, dirs, files in os.walk(folder):
        # print(f"{root}, {dirs}, {files}")
        for dirName in dirs:
            if 'images' == dirName:
                continue
            result.add(dirName)
    # print(result)
    return result


def transform_folder(folder: str, source: str, target: str) -> None:
    print(folder)

    year = folder[0:4]
    print(f"Year: {year}")
    new_name = folder[25:]
    print(f"New name: {new_name}")

    new_folder_path = target + os.sep + year + os.sep + new_name + os.sep 
    print(f"New folder path: {new_folder_path}")

    os.makedirs(new_folder_path)
    shutil.copy(f"{source}{os.sep}{folder}{os.sep}index.md", f"{new_folder_path}{new_name}.md")
    
    image_folder = f'{source}{os.sep}{folder}{os.sep}images'
    if os.path.isdir(image_folder):
        shutil.copytree(image_folder, new_folder_path, dirs_exist_ok=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    source = args[0]
    target = args[1]
    print(f"transform_posts runs with {source} -> {target}")

    folders = collector(source)
    for folder in folders:
        transform_folder(folder, source, target)