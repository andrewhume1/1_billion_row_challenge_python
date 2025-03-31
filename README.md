# 1_billion_row_challenge_python
# 1 Billion Row Challenge - Python Implementation

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

## 🚀 Challenge Overview
This project implements three progressively optimized Python solutions for processing 1 billion weather station measurements. Each version demonstrates significant performance improvements while maintaining accuracy.

## 📂 Project Structure
1_billion_row_challenge_python/
├── data_generator/
│   ├── data/  # Data output directory
│   └── data_generator.py # Data generation script
├── src/
│   ├── v1_basic.py       # Baseline implementation
│   └── v2_implementation.py # Memory-optimized version
└── README.md         # Project documentation



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