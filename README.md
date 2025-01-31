# String Search Algorithm Comparison

This Python script implements and compares the performance of three well-known string search algorithms:

- **Knuth-Morris-Pratt (KMP) Algorithm**
- **Boyer-Moore Algorithm**
- **Rabin-Karp Algorithm**

The script reads text from two files and searches for a given pattern using all three algorithms, measuring their execution time.

## Features

- Implements **three string matching algorithms** to search for a pattern in a text.
- Uses **timeit** to measure the execution time of each algorithm.
- Reads data from text files and applies each algorithm to evaluate performance.

## Algorithms Used

### 1. Knuth-Morris-Pratt (KMP) Algorithm

- Uses **prefix function (LPS array)** to avoid redundant comparisons.
- Efficient for repeated pattern searches.

### 2. Boyer-Moore Algorithm

- Utilizes a **bad-character shift table** to skip unnecessary comparisons.
- Performs well for large texts.

### 3. Rabin-Karp Algorithm

- Uses **polynomial hashing** to quickly compare substrings.
- Efficient when searching for multiple patterns.

## How It Works

1. **Reads two text files** (`test_data1.txt` and `test_data2.txt`).
2. **Applies all three search algorithms** to find occurrences of a pattern.
3. **Measures and ranks execution time** of each algorithm.

## Usage

### Prerequisites

- Python 3.x installed

### Dependencies

This script uses only built-in Python libraries:

- timeit for performance measurement

### Running the script

1. Place the text files inside `task_3/test_data/`
2. Execute the script:

```bash
python main.py
```

### Expected Output


    ------------------test data 1----------------------- 
    Пошук Алгоритмом Кнута-Морріса-Пратта: [206, 1103, 1266, 2632, 8169, 8364, 11306]    
    Пошук Алгоритмом Боєра-Мура: [206, 1103, 1266, 2632, 8169, 8364, 11306]     
    Пошук Алгоритмом Рабіна-Карпа: [206, 1103, 1266, 2632, 8169, 8364, 11306]     
    Sorting algorithms ranked by time:     
    Алгоритм Кнута-Морріса-Пратта: 0.002088 seconds     
    Алгоритм Боєра-Мура: 0.000353 seconds     
    Алгоритм Рабіна-Карпа: 0.002206 seconds     
    ------------------test data 2-----------------------     
    Пошук Алгоритмом Кнута-Морріса-Пратта: [2886, 4279, 5638]     
    Пошук Алгоритмом Боєра-Мура: [2886, 4279, 5638]     
    Пошук Алгоритмом Рабіна-Карпа: [2886, 4279, 5638]     
    Sorting algorithms ranked by time:     
    Алгоритм Кнута-Морріса-Пратта: 0.002967 seconds     
    Алгоритм Боєра-Мура: 0.000496 seconds     
    Алгоритм Рабіна-Карпа: 0.003097 seconds     


## Conclusions

- The Boyer-Moore algorithm is generally the fastest for long texts.
- Rabin-Karp performs well when multiple patterns need to be found.
- KMP is effective for repeated pattern searches in large texts.
