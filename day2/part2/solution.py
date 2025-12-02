import sys

def get_divisors_exclude_one(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def check_if_valid(id):
    s = str(id)
    
    for divisor in get_divisors_exclude_one(len(s)):
        part_len = len(s) // divisor
        parts = [int(s[i*part_len : (i+1)*part_len]) for i in range(divisor)]
        if all(x == parts[0] for x in parts):
            return False

    return True

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