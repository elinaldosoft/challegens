### Abount the challenge
https://www.hackerrank.com/challenges/apple-and-orange/problem

### Benchmark (I made 10000 calls)
#### 01 
```
   10004 function calls in 0.027 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.027    0.027 <string>:1(<listcomp>)
        1    0.000    0.000    0.027    0.027 <string>:1(<module>)
    10000    0.022    0.000    0.022    0.000 main.py:11(count_apples_and_oranges_01)
        1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
#### 02
```
   10010 function calls in 0.006 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.006    0.006 <string>:1(<listcomp>)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
    10000    0.002    0.000    0.002    0.000 main.py:30(count_apples_and_oranges_02)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
```
#### 03
```
    50004 function calls in 0.030 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    0.030    0.030 <string>:1(<listcomp>)
        1    0.000    0.000    0.030    0.030 <string>:1(<module>)
    10000    0.013    0.000    0.024    0.000 main.py:47(count_apples_and_oranges_03)
    10000    0.004    0.000    0.004    0.000 main.py:51(<listcomp>)
    10000    0.004    0.000    0.004    0.000 main.py:52(<listcomp>)
        1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
    20000    0.003    0.000    0.003    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
### 04
```
   110004 function calls in 0.039 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.038    0.038 <string>:1(<listcomp>)
        1    0.000    0.000    0.038    0.038 <string>:1(<module>)
    10000    0.009    0.000    0.033    0.000 main.py:56(count_apples_and_oranges_04)
    40000    0.006    0.000    0.006    0.000 main.py:60(<genexpr>)
    40000    0.006    0.000    0.006    0.000 main.py:61(<genexpr>)
        1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
    20000    0.012    0.000    0.024    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```