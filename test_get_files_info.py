from functions.get_files_info import get_files_info


def _print_section(title: str, result: str) -> None:
    print(title)
    if result.startswith("Error:"):
        print(f"    {result}")
        return

    for line in result.splitlines():
        print(f"  {line}")


if __name__ == "__main__":
    _print_section(
        "Result for current directory:",
        get_files_info("calculator", "."),
    )
    print()

    _print_section(
        "Result for 'pkg' directory:",
        get_files_info("calculator", "pkg"),
    )
    print()

    _print_section(
        "Result for '/bin' directory:",
        get_files_info("calculator", "/bin"),
    )
    print()

    _print_section(
        "Result for '../' directory:",
        get_files_info("calculator", "../"),
    )
