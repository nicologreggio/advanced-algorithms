from distutils.log import error
from algorithms.measure_algorithm_performance import measure_algorithm_performance, measure_run_time
from algorithms.random_insertion import random_insertion
from main import print_measurement_data

from graph.graph import * 

def error_function(approximate_solution, optimal_solution):
    return (approximate_solution - optimal_solution) / optimal_solution

path = "/Users/dilettarigo/Desktop/advanced-algorithms/assignment-2/tsp_dataset"
A = read_all(path)

g = A[0][0]
o = A[0][1]

# PRINT MEASUREMENT DATA WORKS
approximate_solutions, run_times, errors = measure_algorithm_performance(random_insertion, A, error_function, num_calls=10)

print_measurement_data(approximate_solutions, run_times, errors)

'''
# MEASURE ALGORITHMIC PERFORMANCE WORKS 
approximate_solutions, run_times, errors = measure_algorithm_performance(random_insertion, A, error_function, num_calls=10)

print(approximate_solutions)
print(run_times)
print(errors)
'''

'''
# MEASURE RUN TIME WORKS 
t, w = measure_run_time(random_insertion, g, 10)

print(t)
print(w)
print(error_function(w, o))
'''

'''
# WORKS ON THE FIRST INPUT 
w = random_insertion(g)
print(w)
print(o)
print(error_function(w, o))
'''