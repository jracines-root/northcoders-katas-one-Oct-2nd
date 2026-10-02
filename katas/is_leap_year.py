# Test case 1900, expect is_leap_year(500):= False

def is_leap_year(year):
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
        return False 
    if year % 4 == 0:
        return True
    return False

print(f"test case 2024, expect: True . We got {is_leap_year(2024)}")
print(f"test case 1900, expect: False . We got {is_leap_year(1900)}")
print(f"test case 2000, expect: True . We got {is_leap_year(2000)}")


"""
check if divisble by 4 and 100 both yes--> then is divisble by 400 if yes --> True . False implied if not
check special case if divisble just by (only) 4 (not 100) --> output True
if not anything --> False 
"""