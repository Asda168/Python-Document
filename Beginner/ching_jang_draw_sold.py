art = [
    "⠀⠀⠀⠀⢀⣄⣠⣤⡶⢶⣶⣾⠷⣦⣄⡀⠀⠀⠀⠀",
    "⠀⠀⠀⣰⡟⠋⠻⠂⠀⠘⠁⡈⣙⠿⣏⠙⢦⡀⠀⠀",
    "⠀⠀⣸⠙⠀⠄⠒⠢⡀⠀⠊⢀⣀⡁⠈⢧⠀⠹⣄⡀",
    "⠀⠀⣯⠀⠘⢠⠤⣦⣄⠀⢰⠁⣹⣿⠀⢸⣦⠞⠁⢹",
    "⠀⠀⣹⠤⠂⢧⣤⡿⠃⠀⠈⠙⠋⠁⠀⠸⠃⠀⠀⢸",
    "⠀⣰⠃⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠈⡖⠒⠁",
    "⠀⣿⠀⠀⠀⠀⢀⠞⠁⠀⠑⡄⠀⠀⠀⢀⣼⡁⠀⠀",
    "⠀⠘⣆⠀⠀⠀⢸⡀⠀⠀⢠⣇⣠⠤⠞⠉⠀⠱⣄⠀",
    "⢀⡴⠋⢉⡗⠒⠒⠛⠋⠉⠉⠀⠀⠀⠀⠀⡆⢀⡼⠃",
    "⠈⡱⠢⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢟⠉⡆⠀",
    "⠀⠓⢴⠃⠀⣀⢤⡀⠀⣀⠤⠄⠀⢀⡀⠀⣸⠔⠁⠀",
    "⠀⠀⢸⠁⠉⠀⠀⠁⠬⣤⠀⠈⠂⠁⠈⠉⠘⡆⠀⠀",
    "⠀⠀⠘⠒⠲⠤⠤⡤⠤⠾⣀⣀⣀⣀⣀⣠⠤⠇⠀⠀",
    "⠀⠀⠀⠀⠀⢣⠄⡇⠀⠀⠀⠀⢧⠄⢴⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⣄⣂⣓⡇⠀⠀⠀⠀⠨⢒⣊⣢⡄⠀⠀⠀",
]

BLANK = '⠀'
SCALE = 3  # dots per character cell

rows = len(art)
cols = max(len(row) for row in art)

# Build dot grid
grid_h = rows * SCALE
grid_w = cols * SCALE
grid = [['  ' for _ in range(grid_w)] for _ in range(grid_h)]

for r, line in enumerate(art):
    for c, ch in enumerate(line):
        if ch != BLANK and ch != ' ':
            # Fill a SCALE x SCALE block with dots
            for dr in range(SCALE):
                for dc in range(SCALE):
                    grid[r * SCALE + dr][c * SCALE + dc] = '. '

# Print the dot grid
for row in grid:
    print(''.join(row))