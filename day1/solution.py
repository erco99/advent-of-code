import sys

def solve(input, document):
    result = 0
    for line in document.splitlines():
        val = (1 if line[0] == "R" else -1) * (int(line[1:]) % 100)
        input = (input + val) % 100
        result += (input == 0)

    return result


if __name__ == "__main__":
    initial_value = int(sys.argv[1])

    filename = sys.argv[2]
    with open(filename, "r") as f:
        content = f.read()

    print(solve(initial_value, content))