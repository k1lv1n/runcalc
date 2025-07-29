import os
import shutil
import sys
from pathlib import Path



CONFIG_TEMPLATE = """ 

name: simple-bash-script
desc: Find text pattern in input file with grep
cmd: ./experiments/{1}/run.sh
inputs:
{0}
  - ./experiments/{1}/run.sh
  - ./experiments/{1}/solver/outputs/output_wtf.txt
outputs:
  - ./experiments/{1}/solver/outputs/outputs.zip
""" # TODO что делать с output-ом?

RUN_TEMPLATE = """
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

"$SCRIPT_DIR/solver/run.sh"
"""
OUTPUT_WTF_TEMPLATE = """
Вспомогательный файл для инициализации директории
"""

def get_dir_files(path, exp_name):
    directory = Path(path)
    files = []
    for f in directory.rglob('*'):
        if f.is_file():
            files.append(f.name)
    return f"  - ./experiments/{exp_name}/solver/" +f"\n  - ./experiments/{exp_name}/solver/".join(files)


def init_experiment(exp_name, solver_name):
    dest_parent = Path(__file__).parent / "experiments"
    exp_dir = os.path.join(dest_parent, exp_name)

    os.makedirs(exp_dir, exist_ok=True)
    config_path = os.path.join(exp_dir, "config.yaml")
    cmd_path = os.path.join(exp_dir, "run.sh")

    solver_path = Path(__file__).parent / "solvers" / solver_name

    shutil.copytree(solver_path, os.path.join(exp_dir, "solver"), dirs_exist_ok=True)
    outputs_path = os.path.join(os.path.join(exp_dir, "solver"), "outputs")
    os.makedirs(outputs_path, exist_ok=True)

    input_files = get_dir_files(os.path.join(exp_dir, "solver"), exp_name)

    # Write the text file
    with open(os.path.join(outputs_path, "output_wtf.txt"), 'w', encoding="utf-8") as f:
        f.write(OUTPUT_WTF_TEMPLATE)

    # Write the text file
    with open(config_path, 'w', encoding="utf-8") as f:
        f.write(CONFIG_TEMPLATE.format(input_files, exp_name))

    # Write the text file
    with open(cmd_path, 'w', encoding="utf-8") as f:
        f.write(RUN_TEMPLATE)


def run_experiment():
    pass


def experiment(*args):
    if args[0][0] == 'init':
        init_experiment(*args[0][1::])
    elif args[0][0] == 'run':
        run_experiment(*args[0][1::])


if __name__ == '__main__':
    experiment(sys.argv[1::])
    # print(get_dir_files('.'))
