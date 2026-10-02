# [1, 2, 5, 8]
def are_ordered(list_of_numbers):
    if len(list_of_numbers) == 0:
        return False
    last_number = None
    for i in list_of_numbers:
        if last_number is not None:
            if i <last_number:
                return False
        last_number = i
    return True

print(are_ordered([1, 2, 5, 8]))
print(f"if the list empty should return False, our function returns {are_ordered(list_of_numbers=[])}")
print(f"test case '[1, 5, 2, 8]' expected result: [1, 2, 5, 8]. We get {are_ordered([1, 5, 2, 8])}")