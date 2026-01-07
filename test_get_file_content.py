from config import MAX_CHARS
from functions.get_file_content import get_file_content


def _print_section(title: str, result: str) -> None:
    print(title)
    if result.startswith("Error:"):
        print(f"    {result}")
        return

    # preview_len = min(120, len(result))
    # print(f"  length={len(result)}")
    # print(f"  preview={result[:preview_len]!r}")

    print(f"  length={len(result)}")
    print(f"  result={result!r}")


if __name__ == "__main__":
    lorem_result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt:")
    if lorem_result.startswith("Error:"):
        print(f"    {lorem_result}")
    else:
        expected_suffix = f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'
        print(f"  content_length={len(lorem_result)}")
        print(f"  ends_with_truncation_notice={lorem_result.endswith(expected_suffix)}")
        if not lorem_result.endswith(expected_suffix):
            print("  Error: lorem.txt was not truncated as expected")

    print()

    _print_section(
        "Result for main.py:",
        get_file_content("calculator", "main.py"),
    )
    print()

    _print_section(
        "Result for pkg/calculator.py:",
        get_file_content("calculator", "pkg/calculator.py"),
    )
    print()

    _print_section(
        "Result for /bin/cat:",
        get_file_content("calculator", "/bin/cat"),
    )
    print()

    _print_section(
        "Result for pkg/does_not_exist.py:",
        get_file_content("calculator", "pkg/does_not_exist.py"),
    )
