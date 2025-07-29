"""
File to manage work with solvers.

Solver is a bunch of files that is stored in special folder on /platform/solvers.

Each solver has its source files and metadata.
"""
import os
import random
import shutil
import sys
from datetime import datetime
from pathlib import Path

ADJECTIVES = [
    "Bright",
    "Quick",
    "Silent",
    "Tiny",
    "Brave",
    "Ancient",
    "Curious",
    "Modern",
    "Strange",
    "Lazy",
]
NOUNS = [

    "Mountain",
    "River",
    "Cat",
    "Book",
    "Idea",
    "Forest",
    "Dream",
    "Bridge",
    "Star",
    "Garden",
]


def make_metadata(name: str | None, ) -> dict:
    return {
        "name": name,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def add(src_dir, new_dir_name=None):
    """
    Create a new solver from files in some folder.
    :return:
    """
    dest_parent = Path(__file__).parent / "solvers"
    if new_dir_name is None:
        new_dir_name = f"{random.choice(ADJECTIVES)}-{random.choice(NOUNS)}"
    dest_dir = os.path.join(dest_parent, new_dir_name)

    # Copy the directory
    shutil.copytree(src_dir, dest_dir)
    print(f'Copied directory to: {dest_dir}')

    # Path for the new text file
    txt_file_path = os.path.join(dest_dir, "metadata.txt")

    # Write the text file
    with open(txt_file_path, 'w', encoding="utf-8") as f:
        f.write(str(make_metadata(new_dir_name)))
    print(f'Added text file: {txt_file_path}')


def solver(*args):
    if args[0][0] == 'add':
        add(*args[0][1::])

if __name__ == '__main__':
    solver(sys.argv[1::])
