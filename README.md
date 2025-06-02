# Mini CNC G-code Visualizer

A simple Python tool to read and visualize CNC G-code toolpaths in 2D using matplotlib.

## Features

- Parses standard G-code files (supports G0 and G1 commands)
- Visualizes toolpaths, differentiating rapid (G0) and feed (G1) moves with colors
- Marks start and end points
- Displays basic toolpath statistics (total moves, distance)
- Command-line file selection

## Requirements

- Python 3.x
- matplotlib

Install dependencies:

pip install matplotlib

## Usage

1. Place your G-code file (e.g., `sample_square.gcode`) in the project folder.
2. Run the visualizer:

python visualize_gcode.py sample_square.gcode
If no file is specified, it defaults to `sample_square.gcode`.

## Project Structure
mini-cnc-visualizer/
├── gcode_parser.py
├── visualize_gcode.py
├── sample_square.gcode
└── README.md


