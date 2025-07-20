def even_odd_divider(lst):
    even_numbers = []
    odd_numbers = []
    string_to_int = list(map(int, lst))

    for num in string_to_int:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    # loop ke baad result check karo
    if not even_numbers and not odd_numbers:
        return []
    else:
        return [even_numbers, odd_numbers]


# input list
num_list = ["1", "2", "3", "4", "5"]

# function call
print(even_odd_divider(num_list))
