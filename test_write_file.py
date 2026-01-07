from functions.write_file import write_file

def _print_section(title: str, result: str) -> None:
    print(title)
    if result.startswith("Error:"):
        print(f"    {result}")
        return
    print(f"    {result}")

if __name__ == "__main__":
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    _print_section("Result for lorem.txt:", result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    _print_section("Result for pkg/morelorem.txt:", result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    _print_section("Result for /tmp/temp.txt:", result)
