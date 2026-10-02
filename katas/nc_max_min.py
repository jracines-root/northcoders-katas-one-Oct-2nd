import math

# [3, 7, 2, 9, 4] = 9 
def nc_max(list_numbers):
    
    if len(list_numbers) <= 0:
        return 0
    
    max_number = -math.inf
    
    for i in list_numbers:
        max_number = max(i, max_number)
    
    return max_number

print(nc_max([])) # 9

def nc_min(list_numbers):
    
    if len(list_numbers) <= 0:
        return 0
    
    min_number = +math.inf
    
    for i in list_numbers:
        min_number = min(i, min_number)
    
    return min_number
    

print(f"Expected: 2, Actual:{nc_min([3, 7, 2, 9, 4])}")