import random
import sys
import os
from datetime import datetime

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python generator.py <number_of_rows>")
    sys.exit(1)

try:
    num_rows = int(sys.argv[1])
    if num_rows <= 0:
        raise ValueError("Number of rows must be positive")
except ValueError:
    print("Error: Invalid number of rows. Please provide a positive integer.")
    sys.exit(1)

# Define a list of example weather station names
stations = [
    "Hamburg", "Berlin", "Munich", "Cologne", "Frankfurt",
    "Stuttgart", "Düsseldorf", "Leipzig", "Dortmund", "Essen",
    "Bremen", "Dresden", "Hanover", "Nuremberg", "Duisburg",
    "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster"
]

# Create data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Generate output file name with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"data/measurements_{num_rows}_{timestamp}.csv"

print(f"Generating {num_rows} rows of weather data...")
start_time = datetime.now()

# Generate and write data
with open(output_file, "w") as f:
    for i in range(num_rows):
        station = random.choice(stations)
        # Generate temperature between -30.0 and 45.0 degrees Celsius
        temperature = round(random.uniform(-30.0, 45.0), 1)
        f.write(f"{station};{temperature}\n")
        
        # Print progress every 10 million rows
        if (i + 1) % 10_000_000 == 0:
            progress = (i + 1) / num_rows * 100
            elapsed_time = (datetime.now() - start_time).total_seconds()
            rows_per_second = (i + 1) / elapsed_time if elapsed_time > 0 else 0
            print(f"Progress: {progress:.2f}% ({i + 1} rows, {rows_per_second:.2f} rows/s)")

elapsed_time = (datetime.now() - start_time).total_seconds()
print(f"Done! Generated {num_rows} rows in {elapsed_time:.2f} seconds.")
print(f"Output file: {output_file}")