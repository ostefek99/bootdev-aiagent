from functions.run_python_file import run_python_file


def _print_section(title: str, result: str) -> None:
    print(title)
    if result.startswith("Error:"):
        print(f"  {result}")
        return
    print(f"{result}")

if __name__ == "__main__":
    result = run_python_file("calculator", "main.py")
    _print_section("Result for main.py:", result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    _print_section("Result for main.py with args [3 + 5]:", result)

    result = run_python_file("calculator", "tests.py")
    _print_section("Result for tests.py:", result)

    result = run_python_file("calculator", "../main.py")
    _print_section("Result for ../main.py:", result)

    result = run_python_file("calculator", "nonexistent.py")
    _print_section("Result for nonexistent.py:", result)

    result = run_python_file("calculator", "lorem.txt")
    _print_section("Result for lorem.txt:", result)
