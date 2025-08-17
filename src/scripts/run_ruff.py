import sys
import shutil
from subprocess import run  # nosec B404


def main() -> None:
    ruff_path = shutil.which("ruff")
    if not ruff_path:
        print("Ruff not found in PATH")
        sys.exit(1)
    # Use 'check' subcommand explicitly
    sys.exit(run([ruff_path, "check", "src", "tests"]).returncode)  # nosec B603


if __name__ == "__main__":
    main()
