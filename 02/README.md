Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].



### Benchmark (I made 10000 calls)
#### 01
```
   20004 function calls in 0.012 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.013    0.013 <string>:1(<listcomp>)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
    10000    0.008    0.000    0.010    0.000 main.py:1(solution_01)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.002    0.000    0.002    0.000 {method 'sort' of 'list' objects}
```

#### 02
```
   40004 function calls in 0.015 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.014    0.014 <string>:1(<listcomp>)
        1    0.000    0.000    0.014    0.014 <string>:1(<module>)
    10000    0.009    0.000    0.012    0.000 main.py:10(solution_02)
    20000    0.001    0.000    0.001    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.002    0.000    0.002    0.000 {method 'sort' of 'list' objects}
```
#### 03
```
   40004 function calls in 0.024 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.039    0.039 <string>:1(<listcomp>)
        1    0.000    0.000    0.039    0.039 <string>:1(<module>)
    10000    0.020    0.000    0.034    0.000 main.py:27(solution_03)
        1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
    10000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    20000    0.013    0.000    0.013    0.000 {method 'index' of 'list' objects}
```