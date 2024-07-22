# Image to Crochet Grid Converter

## Overview

This Python script converts an image into a crochet grid, where each pixel is represented by a crochet symbol that corresponds to the closest color from a predefined set of colors. The output grid can be saved to a CSV file and visualized in the console. The script currently supports up to four colors (X, O, M, S symbols)

## Features

- Load an image and resize it to specified dimensions.
- Convert the image to a crochet grid using specified colors.
- Visualize the crochet grid with actual colors in the console.
- Save the crochet grid to a CSV file.

## Requirements

- Python 3.x
- Pillow (PIL) library
- NumPy library

## Installation

To install the required libraries, run:

```bash
pip install Pillow numpy
```
## Command Line Arguments

The script requires the following command-line arguments:

- image_path: Path to the input image file.
- target_width: Width of the resized image.
- target_height: Height of the resized image.
- colors: RGB values for the colors to be used in the crochet grid. Provide these as a flat list of integers (e.g., 255 0 0 0 255 0 for red and green).
- output_file: Path to the output CSV file where the crochet grid will be saved.

Example:
python script.py path/to/image.jpg 10 10 255 0 0 0 255 0 0 0 255 output.csv

## Author
Emily Ma

For any questions or feedback, please contact Emily Ma at emilymaa@umich.edu.


