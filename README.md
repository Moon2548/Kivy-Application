
# Kivy Application

## Overview
This project is a basic Kivy application built using Python. It focuses on creating interactive GUI applications with Kivy, covering the main aspects of the framework.

## Features
- Basic UI elements with Kivy
- Event handling and widget management
- Kivy's `.kv` file system to separate logic and design

## Prerequisites
- Python 3.x
- Kivy library (install via `pip install kivy`)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Moon2548/Kivy-Application.git
   cd Kivy-Application
   ```
2. Install required libraries:
   ```bash
   pip install kivy
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Code Explanation

### main.py
This is the primary file that initializes the application, defining the logic and handling events.

### my.kv and display_screen.kv
These `.kv` files contain the UI design, written in Kivy's declarative language, separating the layout from the logic.

### Folder Structure
```
Kivy-Application/
├── main.py         # Main Python file to run the app
├── my.kv           # Kivy UI layout file
├── display_screen.kv # Another layout configuration
├── .gitignore      # Git ignore rules
├── README.md       # This file
├── image/           # Image for game
├── slot/           # Game slot 
```