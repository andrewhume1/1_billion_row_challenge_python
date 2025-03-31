import sys
import mmap
import os
from datetime import datetime


def parse_line(line):
    """Parse a single line and return station and temperature."""
    try:
        line_str = line.decode('utf-8')
        station, temp_str = line_str.split(';')
        temperature = float(temp_str)
        return station, temperature
    except (ValueError, UnicodeDecodeError):
        return None, None


def process_chunk(data, station_stats):
    """Process a chunk of data and update station statistics."""
    lines = data.split(b'\n')
    for line in lines:
        if not line:
            continue

        station, temperature = parse_line(line)
        if station is None:
            continue

        if station not in station_stats:
            # Initialize [min, sum, max, count]
            station_stats[station] = [temperature, temperature, temperature, 1]
        else:
            stats = station_stats[station]
            stats[0] = min(stats[0], temperature)  # Update min
            stats[1] += temperature               # Update sum
            stats[2] = max(stats[2], temperature)  # Update max
            stats[3] += 1                         # Update count


def display_progress(chunks_processed, mmap_obj, file_size, start_time):
    """Display progress of file processing."""
    if chunks_processed % 100 == 0:
        position = mmap_obj.tell()
        progress = position / file_size * 100
        elapsed_time = (datetime.now() - start_time).total_seconds()
        bytes_per_second = position / elapsed_time if elapsed_time > 0 else 0
        print(f"Progress: {progress:.2f}% ({bytes_per_second / 1_000_000:.2f} MB/s)")


def process_file(data_file, buffer_size=8 * 1024 * 1024):
    """Process the input file and calculate temperature statistics."""
    station_stats = {}
    file_size = os.path.getsize(data_file)
    start_time = datetime.now()

    with open(data_file, 'r') as f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            chunks_processed = 0
            remaining = b""

            while True:
                chunk = mmap_obj.read(buffer_size)
                if not chunk:
                    break

                data = remaining + chunk
                last_newline = data.rfind(b'\n')
                if last_newline == -1:
                    remaining = data
                    continue

                lines_data = data[:last_newline + 1]
                remaining = data[last_newline + 1:]

                process_chunk(lines_data, station_stats)
                chunks_processed += 1
                display_progress(chunks_processed, mmap_obj, file_size, start_time)

            # Process remaining data
            if remaining:
                process_chunk(remaining, station_stats)

    elapsed_time = (datetime.now() - start_time).total_seconds()
    total_rows = sum(stats[3] for stats in station_stats.values())
    print(f"\nProcessed {total_rows} rows in {elapsed_time:.2f} seconds ({total_rows / elapsed_time:.2f} rows/s)")

    return station_stats


def display_results(station_stats):
    """Display the final results."""
    print("\nResults:")
    print(f"{'Station':<15} {'Min':>8} {'Mean':>8} {'Max':>8}")
    print("-" * 41)

    for station in sorted(station_stats.keys()):
        stats = station_stats[station]
        mean = stats[1] / stats[3]  # Calculate mean
        print(f"{station:<15} {stats[0]:>8.1f} {mean:>8.1f} {stats[2]:>8.1f}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python v2_implementation.py <data_file>")
        sys.exit(1)

    data_file = sys.argv[1]
    print(f"Processing file: {data_file}")

    station_stats = process_file(data_file)
    display_results(station_stats)


if __name__ == "__main__":
    main()