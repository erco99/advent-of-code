import sys

def solve(input):
    parti = input.strip().split("\n\n")

    # splitto ogni parte in righe
    ranges = parti[0].splitlines()
    numbers = [int(n) for n in parti[1].splitlines()]
    
    ranges = [tuple(map(int, item.split('-'))) for item in ranges]
    
    print(ranges)
    print(numbers)

    
    return len([x for x in numbers if any(ran[0] <= x <= ran[1] for ran in ranges)])
    
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        content = f.read()

    print(solve(content))