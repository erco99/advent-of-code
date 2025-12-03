import sys

def solve(input):
    result = 0
    for line in input.splitlines():
        d = {i: int(c) for i, c in enumerate(line)}
        sorted_keys = sorted(d, key=lambda k: d[k], reverse=True)
        max_key = sorted_keys[0]
        if max_key == max(d.keys()):
            max_key = sorted_keys[1]

        candidates = {k: v for k, v in d.items() if k > max_key}
        second_max_key = max(candidates, key=lambda k: candidates[k])

        result += int(str(d[max_key] ) + str(d[second_max_key] ))

    return result

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        content = f.read()

    print(solve(content))