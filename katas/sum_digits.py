def sum_digits(x):
    digit = []
    string_of_numbers = str(x)
    for i in  range(0,len(string_of_numbers)):
        if string_of_numbers[i].isnumeric():
            number_in_string = string_of_numbers[i]
            number = float(number_in_string)
            digit.append(number)
    return int(sum(digit))


print(sum_digits(10.5))