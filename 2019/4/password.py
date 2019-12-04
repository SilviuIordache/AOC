passwords = range(138241, 674035)

arr = range(1, 5)
print(arr[3])


def test_number(number):
    arr = [int(x) for x in str(number)]
    last_digit = -1
    curr_digit = -1
    increasing_digit_order = True
    dual_found = False
    secured = False
    dual_digit = -1
    for i in range(len(arr)):
        if i == 0:
            last_digit = arr[i]
        else:
            last_digit = arr[i-1]
            curr_digit = arr[i]
            if curr_digit - last_digit < 0:
                increasing_digit_order = False
        if last_digit == curr_digit and not secured:
            if dual_digit == curr_digit:
                dual_found = False
            else:
                dual_digit = curr_digit
                dual_found = True
        else:
            if dual_found:
                secured = True
            else:
                dual_digit = -1
    return dual_found and increasing_digit_order


print(test_number(112233))
print(test_number(123444))
print(test_number(111122))
print(test_number(112333))

# test_arr = [112233, 111222, 333455, 444444, 555678, 112233, 112333]
# print(list(filter(lambda x: test_number(x), test_arr)))

print(len(list(filter(lambda x: test_number(x), passwords))))
# print(list(filter(lambda x: test_number(x), passwords)))


