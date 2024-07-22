import argparse
from PIL import Image
import numpy as np
import csv

def image_to_crochet_grid(image_path, colors, target_width, target_height):
    # Load the image
    img = Image.open(image_path)
    
    # Resize the image
    img_resized = img.resize((target_width, target_height))
    
    # Convert the image to RGB mode
    img_rgb = img_resized.convert('RGB')
    
    # Get the dimensions of the image
    width, height = img_rgb.size

    # Initialize the crochet grid
    crochet_grid = [[' ' for _ in range(width)] for _ in range(height)]

    # Iterate through each pixel of the image
    for y in range(height):
        for x in range(width):
            # Get the color of the pixel
            pixel_color = img_rgb.getpixel((x, y))
            
            # Find the closest color among the specified colors
            closest_color = min(colors, key=lambda c: sum((a - b) ** 2 for a, b in zip(c, pixel_color)))
            
            # Determine the index of the closest color
            closest_index = colors.index(closest_color)
            
            # Assign the corresponding crochet symbol based on the index
            if len(colors) == 1:
                crochet_symbol = ['X'][closest_index]
            if len(colors) == 2:
                crochet_symbol = ['X', 'O'][closest_index]
            if len(colors) == 3:
                crochet_symbol = ['X', 'O', 'M'][closest_index]
            else:
                crochet_symbol = ['X', 'O', 'M', 'S'][closest_index]
            
            # Set the corresponding cell in the crochet grid to the mapped symbol
            crochet_grid[y][x] = crochet_symbol

    return crochet_grid

def visualize_crochet_grid(crochet_grid, colors):
    # Create color palette
    color_palette = np.array(colors, dtype=np.uint8)

    # Map crochet symbols to colors
    color_mapping = {}
    for i, symbol in enumerate(['X', 'O', 'M', 'S'][:len(colors)]):
        color_mapping[symbol] = color_palette[i]

    # Create image from crochet grid
    for row in crochet_grid:
        for symbol in row:
            color = color_mapping.get(symbol)  # No default, let it be None if symbol not found
            if color is not None:
                print('\033[48;2;{};{};{}m  \033[0m'.format(color[0], color[1], color[2]), end='')
            else:
                print(' ', end='')  # Print a space if color not found
        print()
    # Print crochet symbols with color codes
    print("\nCrochet Symbols:")
    for row in crochet_grid:
        for symbol in row:
            color = color_mapping.get(symbol)
            if color is not None:
                print('\033[48;2;{};{};{}m{}\033[0m'.format(color[0], color[1], color[2], symbol), end='')
            else:
                print(symbol, end='')
        print()
def save_crochet_grid_to_csv(crochet_grid, colors, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in crochet_grid:
            writer.writerow(row)
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert image to crochet grid')
    parser.add_argument('image_path', help='Path to input image file')
    parser.add_argument('target_width', type=int, help='Width of the resized image')
    parser.add_argument('target_height', type=int, help='Height of the resized image')
    parser.add_argument('colors', nargs='+', type=int, help='RGB values for colors')
    parser.add_argument('output_file', help='Path to output CSV file')
    args = parser.parse_args()

    # Convert RGB values to color tuples
    colors = [(args.colors[i], args.colors[i+1], args.colors[i+2]) for i in range(0, len(args.colors), 3)]

    # Convert image to crochet grid
    crochet_grid = image_to_crochet_grid(args.image_path, colors, args.target_width, args.target_height)

    # Save crochet grid to CSV file
    save_crochet_grid_to_csv(crochet_grid, colors, args.output_file)

    # Visualize crochet grid with actual colors
    visualize_crochet_grid(crochet_grid, colors)

if __name__ == "__main__":
    main()