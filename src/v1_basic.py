import sys
import time
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python v1_basic.py <data_file>")
    sys.exit(1)

data_file = sys.argv[1]

# Dictionary to store statistics for each station
station_stats = {}

print(f"Processing file: {data_file}")
start_time = datetime.now()

# Process the file line by line
with open(data_file, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if not line:
            continue
            
        # Parse station and temperature
        parts = line.split(';')
        if len(parts) != 2:
            print(f"Warning: Invalid line format at line {i+1}: {line}")
            continue
            
        station, temp_str = parts
        try:
            temperature = float(temp_str)
        except ValueError:
            print(f"Warning: Invalid temperature at line {i+1}: {temp_str}")
            continue
            
        # Update statistics for this station
        if station not in station_stats:
            station_stats[station] = {
                'min': temperature,
                'max': temperature,
                'sum': temperature,
                'count': 1
            }
        else:
            stats = station_stats[station]
            stats['min'] = min(stats['min'], temperature)
            stats['max'] = max(stats['max'], temperature)
            stats['sum'] += temperature
            stats['count'] += 1
        
        # Print progress every 10 million lines
        if (i + 1) % 10_000_000 == 0:
            elapsed_time = (datetime.now() - start_time).total_seconds()
            lines_per_second = (i + 1) / elapsed_time if elapsed_time > 0 else 0
            print(f"Processed {i + 1} lines ({lines_per_second:.2f} lines/s)")

# Calculate and display results
print("\nResults:")
print(f"{'Station':<15} {'Min':>8} {'Mean':>8} {'Max':>8}")
print("-" * 41)

for station, stats in sorted(station_stats.items()):
    mean = stats['sum'] / stats['count']
    print(f"{station:<15} {stats['min']:>8.1f} {mean:>8.1f} {stats['max']:>8.1f}")

elapsed_time = (datetime.now() - start_time).total_seconds()
total_rows = sum(stats['count'] for stats in station_stats.values())
print(f"\nProcessed {total_rows} rows in {elapsed_time:.2f} seconds ({total_rows/elapsed_time:.2f} rows/s)")