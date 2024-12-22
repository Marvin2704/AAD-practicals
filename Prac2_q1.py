import time
import matplotlib.pyplot as plt
import sys

# Set the recursion limit
sys.setrecursionlimit(1000000)

# Define functions
def sum_using_loop(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    return total

def sum_using_equation(N):
    return N * (N + 1) // 2

def sum_using_recursion(N):
    if N == 1:
        return 1
    return N + sum_using_recursion(N - 1)

def measure_time(func, N):
    start_time = time.time()
    try:
        func(N)
    except RecursionError:
        return float('inf')  
    end_time = time.time()
    return end_time - start_time

# Measure execution times
input_sizes = [100, 1000, 5000, 10000, 20000, 50000, 100000]
loop_times = []
equation_times = []
recursion_times = []

for size in input_sizes:
    loop_times.append(measure_time(sum_using_loop, size))
    equation_times.append(measure_time(sum_using_equation, size))
    recursion_times.append(measure_time(sum_using_recursion, size))

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, loop_times, label='Loop', marker='o')
plt.plot(input_sizes, equation_times, label='Equation', marker='o')
plt.plot(input_sizes, recursion_times, label='Recursion', marker='o')
plt.xlabel('Input Size (N)')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Execution Time for Sum of 1 to N')
plt.legend()
plt.grid(True)

# Save the plot to a file
plot_file_path = 'sum_execution_times.png'
plt.savefig(plot_file_path)

# Inform the user to open the file
print(f"Plot saved as {plot_file_path}. Please open this file in your web browser.")
