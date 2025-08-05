import os
import subprocess
from dotenv import load_dotenv

load_dotenv()


def run_command_with_live_output(cmd):
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1
    )

    all_output = []
    # Read line-by-line as the process outputs data
    for line in iter(process.stdout.readline, ""):
        if line:
            line = line.rstrip()  # Strip newline
            print(line)  # Print or log line immediately
            all_output.append(line)

    process.stdout.close()
    process.wait()
    full_output = "\n".join(all_output)
    return full_output


def get_job_info(job_id: str):
    result = run_command_with_live_output(
        ["datasphere", "project", "job", "get", "--id", job_id]
    )
    return result


def get_job_files(job_id: str, output_dir: str):
    extra = ["--output-dir", output_dir] if output_dir else []
    result = run_command_with_live_output(
        ["datasphere", "project", "job", "download-files", "--id", job_id] + extra
    )
    return result


def execute_job(job_configuration_path: str):
    result = run_command_with_live_output(
        [
            "datasphere",
            "project",
            "job",
            "execute",
            "--p",
            os.environ["DS_PROJECT"],
            "-c",
            job_configuration_path,
        ]
    )
    return result


if __name__ == "__main__":
    result = get_job_files("bt1gaom31dcvn70qs8ka", ".")

    # Access the command's standard output
    print("STDOUT:")
    print(result)
