def sum_args(*args):
    
    total_sum = 0
    
    for i in args:
        total_sum += i
    
    return total_sum

## tests

print(f"expected result : 6, actual result: {sum_args(1, 2, 3)}")

print(f"expected result : 5, actual result: {sum_args(5)}")

print(f"expected result : 0, actual result: {sum_args()}")

print(f"expected result : -9, actual result: {sum_args(-1,-3,-5)}")