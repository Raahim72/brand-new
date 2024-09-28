import math

def calculate_perimeter(radius):
    """Calculate the perimeter (circumference) of a circle."""
    return 2 * math.pi * radius

def get_radius():
    """Get a valid radius from the user."""
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                print("Please enter a non-negative radius.")
            else:
                return radius
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    radius = get_radius()
    perimeter = calculate_perimeter(radius)
    print(f"The perimeter (circumference) of the circle is: {perimeter:.2f}")

if __name__ == "__main__":
    main()
