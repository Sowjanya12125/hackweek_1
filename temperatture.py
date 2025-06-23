import argparse

# Create parser
parser = argparse.ArgumentParser(description="Converting Celsius to Fahrenheit")

# Add argument
parser.add_argument("c", type=float, help="Celsius temperature")

# Parse arguments
args = parser.parse_args()

# Convert and print
fahrenheit = (9 * args.c) / 5 + 32
print("Temperature in Fahrenheit:", fahrenheit)
