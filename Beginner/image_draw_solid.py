import numpy as np
from PIL import Image


def draw_image_as_ascii(image_path, new_width=100):
    try:
        # 1. Load the image and convert to grayscale ('L' mode)
        img = Image.open(image_path).convert('L')

        # 2. Resize maintaining aspect ratio (crucial so you don't look stretched!)
        width, height = img.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.5)  # 0.5 compensates for tall text characters
        img = img.resize((new_width, new_height))

        # 3. Convert image pixels to a numpy array
        pixels = np.array(img)

        # 4. Generate and print the ASCII grid
        print("\n--- GENERATING ART ---\n")
        for row in pixels:
            line = ""
            for pixel_value in row:
                # If the pixel is dark (suit/hair), print *
                # If the pixel is light (background/shirt), print a space
                if pixel_value < 120:
                    line += "*"
                else:
                    line += " "
            print(line)

    except Exception as e:
        print(f"Error: {e}")


# --- THIS PART RUNS THE CODE ---
# Put the full path to your image here!
my_image = r"C:\Project\PythonProject\Beginner\image.jpg"
draw_image_as_ascii(my_image)