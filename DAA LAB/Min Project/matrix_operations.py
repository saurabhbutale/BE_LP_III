import threading
import numpy as np
import time

# Standard matrix multiplication
def matrix_multiply(A, B):
  #return np.dot(A, B)
  
    result = np.zeros((A.shape[0], B.shape[1]))
    
    for i in range(A.shape[0]):  
        for j in range(B.shape[1]):  
            for k in range(A.shape[1]):  
                result[i][j] += A[i][k] * B[k][j]  # Accumulate the product
    return result

# Multithreaded matrix multiplication (one thread per row)
def matrix_multiply_multithreaded_row(A, B):
    result = np.zeros((len(A), len(B[0])))

    def compute_row(row_index):
        for j in range(len(B[0])):
            result[row_index][j] = sum(A[row_index][k] * B[k][j] for k in range(len(B)))

    threads = []
    for i in range(len(A)):
        thread = threading.Thread(target=compute_row, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

# Multithreaded matrix multiplication (one thread per cell)
def matrix_multiply_multithreaded_cell(A, B):
    result = np.zeros((len(A), len(B[0])))

    def compute_cell(i, j):
        result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

    threads = []
    for i in range(len(A)):
        for j in range(len(B[0])):
            thread = threading.Thread(target=compute_cell, args=(i, j))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return result

# Function to compare performance
def compare_performance(A, B):
    start = time.time()
    matrix_multiply(A, B)
    end = time.time()
    std_time = end - start

    start = time.time()
    matrix_multiply_multithreaded_row(A, B)
    end = time.time()
    row_thread_time = end - start

    start = time.time()
    matrix_multiply_multithreaded_cell(A, B)
    end = time.time()
    cell_thread_time = end - start

    return {
        "Standard": std_time,
        "Multithreaded_Row": row_thread_time,
        "Multithreaded_Cell": cell_thread_time
    }
