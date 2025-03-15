import math

def get_positive_number(prompt):
    """
    Ask the user for a positive number and return it.
    Steps:
    1. Use a while loop to repeatedly ask for input until a valid positive number is provided.
    2. Use a try-except block to handle non-numeric inputs.
    3. If the input is valid and positive, return the number.
    4. If the input is invalid or non-positive, display an error message and re-prompt.
    """
    pass

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.
    Steps:
    1. Use the formula: Area = 0.5 * base * height.
    2. Return the calculated area.
    """
    pass

def calculate_square_area(side):
    """
    Calculate the area of a square.
    Steps:
    1. Use the formula: Area = side * side.
    2. Return the calculated area.
    """
    pass

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    Steps:
    1. Use the formula: Area = length * width.
    2. Return the calculated area.
    """
    pass

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    Steps:
    1. Use the formula: Area = π * radius * radius.
    2. Use math.pi for the value of π.
    3. Return the calculated area.
    """
    pass

def main():
    """
    Main function to run the Multi-Shape Area Calculator.
    Steps:
    1. Print a welcome message.
    2. Use a while loop to create an interactive menu:
       - Display the options: Triangle, Square, Rectangle, Circle.
       - Ask the user to choose a shape.
    3. Based on the user's choice:
       - For Triangle:
         - Call get_positive_number() to get the base and height.
         - Call calculate_triangle_area() to calculate the area.
         - Display the area.
       - For Square:
         - Call get_positive_number() to get the side length.
         - Call calculate_square_area() to calculate the area.
         - Display the area.
       - For Rectangle:
         - Call get_positive_number() to get the length and width.
         - Call calculate_rectangle_area() to calculate the area.
         - Display the area.
       - For Circle:
         - Call get_positive_number() to get the radius.
         - Call calculate_circle_area() to calculate the area.
         - Display the area.
    4. If the user enters an invalid choice, display an error message and re-prompt.
    5. After calculating the area, ask the user if they want to calculate another area.
    6. If the user chooses not to continue, print a goodbye message and exit.
    """
    pass

if __name__ == "__main__":
    main()