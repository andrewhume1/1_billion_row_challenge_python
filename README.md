# 1 Billion Row Challenge - Python Implementation

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

## 🚀 Challenge Overview
This project implements two progressively optimized Python solutions for processing 1 billion weather station measurements. Each version demonstrates significant performance improvements while maintaining accuracy.

## 📂 Project Structure

- 📂 __1\_billion\_row\_challenge\_python__
   - 📄 [README.md](README.md)
   - 📂 __data\_generator__
     - 📂 __data__
     - 📄 [data\_generator.py](data_generator/data_generator.py)
   - 📂 __src__
     - 📄 [v1\_basic.py](src/v1_basic.py)
     - 📄 [v2\_implementation.py](src/v2_implementation.py)



## 🧠 Design Approach
### Version Progression Strategy
1. **V1: Baseline**  
   - Simple line-by-line processing
   - Native dictionary storage
   - Progress reporting every 10M rows

2. **V2: Memory Optimization**  
   - Memory-mapped file I/O (mmap)
   - Buffer chunk processing (8MB chunks)
   - Separate dictionaries for min/max/sum/count
   - Reduced string decoding overhead
   - Code cleanup for better readibility


**Sample Benchmark (10M rows):**


V1: 8.72s @ 1.14M rows/s

V2: 5.06s @ 1.98M rows/s
