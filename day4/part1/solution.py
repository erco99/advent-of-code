import sys

def solve(input):
    grid = [list(line) for line in input.splitlines()]
    R, C = len(grid), len(grid[0])
    dirs = [(-1,-1),(-1,0),(-1,1),
            (0,-1),        (0,1),
            (1,-1),(1,0),(1,1)]

    resullt = [
        "".join([
            (
                '@' if sum(
                    1 for dr, dc in dirs
                    if 0 <= r+dr < R and 0 <= c+dc < C 
                    and grid[r+dr][c+dc] == '@'
                ) >= 4 else 'x'
            ) if grid[r][c] == '@' else grid[r][c]
            for c in range(C)
        ])
        for r in range(R)
    ]

    return sum(row.count('x') for row in resullt)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as f:
        content = f.read()

    print(solve(content))