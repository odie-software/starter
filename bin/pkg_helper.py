#!/usr/bin/env python
import subprocess
import sys
from typing import List


def main():
    """
    A helper script to install packages in the web or api containers.
    """
    if len(sys.argv) < 2:
        print("Usage: python pkg-helper.py [web|api]")
        sys.exit(1)

    target = sys.argv[1]

    if target not in ["web", "api"]:
        print(f"Invalid target: {target}. Please use 'web' or 'api'.")
        sys.exit(1)

    try:
        package_name = input(f"Enter the name of the {target} package to install: ")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(1)

    if not package_name:
        print("No package name provided. Exiting.")
        sys.exit(1)

    print(f"\nInstalling '{package_name}' in the '{target}' container...")

    if target == "web":
        install_command = f"docker compose exec web npx pnpm install {package_name}"
        update_command = "make web_modules"
    else:  # api
        install_command = f"docker compose exec api pip install {package_name}"
        update_command = "make api_modules"

    try:
        run_command(install_command.split())

        if target == "api":
            print("Updating requirements.txt...")
            update_requirements()

        print(f"Updating local modules for '{target}'...")
        run_command(update_command.split())

        print(f"\nSuccessfully installed '{package_name}' and updated dependencies.")
    except subprocess.CalledProcessError as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


def run_command(command: List[str]):
    """
    Runs a command and streams its output.
    """
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    if process.stdout:
        for line in iter(process.stdout.readline, ""):
            print(line, end="")
    process.wait()
    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, command)


def update_requirements():
    """
    Updates the api/requirements.txt file from the container.
    """
    freeze_command = "docker compose exec api pip freeze"
    result = subprocess.run(
        freeze_command.split(), capture_output=True, text=True, check=True
    )
    with open("api/requirements.txt", "w") as f:
        f.write(result.stdout)


if __name__ == "__main__":
    main()
