passwords = range(138241, 674034 + 1)

def test_number(number):
    arr = [char for char in str(number)]

    last_digit = -1
    curr_digit = -1

    increasing_digit_order = True
    dual_found = False
    dual_digit = -1
    occurrence = [-1, 0]
    for i in range(len(arr)):
        if i == 0:
            last_digit = arr[i]
        else:
            last_digit = arr[i-1]
            curr_digit = arr[i]
            if int(curr_digit) - int(last_digit) < 0:
                increasing_digit_order = False
        if last_digit == curr_digit:
            if dual_digit != -1 and dual_digit == curr_digit:
                dual_digit = -1
            else:
                dual_digit = int(curr_digit)
    if dual_digit >= 0:
        dual_found = True
    return dual_found and increasing_digit_order


print(test_number(123444))

# print(len(list(filter(lambda x: test_number(x), passwords))))


