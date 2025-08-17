import sys
import shutil
from subprocess import run  # nosec B404


def main() -> None:
    black_path = shutil.which("black")
    if not black_path:
        print("Black not found in PATH")
        sys.exit(1)
    sys.exit(run([black_path, "src", "tests"]).returncode)  # nosec B603


if __name__ == "__main__":
    main()
