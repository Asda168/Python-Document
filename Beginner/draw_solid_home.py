def draw_solid_home(height):
    # 1. The Roof
    # Creates a triangle where the base width is (2 * height - 1)
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

    # 2. The Body (The Walls)
    # We use (2 * height - 3) to align the walls slightly inside the roof edges
    body_width = (2 * height - 1)
    for _ in range(height - 1):
        print('*' * body_width)

# Run the function
draw_solid_home(6)