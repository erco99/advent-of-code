import sys

def check_if_valid(id):
    s = str(id)

    if len(s) % 2 != 0:
        return True
    
    half = len(s) // 2
    left, right = s[:half], s[half:]

    return left != right

def solve(ranges):
    result = 0
    for val in ranges.split(","):
        first_id, last_id = map(int, val.split("-"))
        for val_id in range(first_id, last_id + 1):
            result += val_id if not check_if_valid(val_id) else 0
            
    return result
    
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        content = f.read()

    print(solve(content))