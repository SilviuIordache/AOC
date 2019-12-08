with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

image_data = content[0]

#print(image_data)


def split(word):
    return [int(char) for char in word]


def get_layers_from_code(code, width, height):
    layers = []
    pos = 0
    img_size = width * height
    while pos != len(code):
        new_layer = split(code[pos:pos + img_size])
        layers.append(new_layer)
        pos += img_size

    return layers


def find_min_digit_layer(digit, layers):
    min_digit_layer = -1
    min_digit_count = 100000

    for layer in layers:
        count = 0
        for i in layer:
            if i == digit:
                count = count + 1
        if count < min_digit_count:
            min_digit_count = count
            min_digit_layer = layer

    return min_digit_layer


def operation_on_layer(digit1, digit2, layer):
    digit1_count = 0
    digit2_count = 0
    for digit in layer:
        if digit == digit1:
            digit1_count += 1
        if digit == digit2:
            digit2_count += 1
    return digit1_count * digit2_count


def generate_final_img(layers, width, height):
    img_size = width * height
    final_image = []
    for i in range(img_size):
        final_image.append(2)

    for layer in layers:
        for i in range(len(layer)):
            if layer[i] != 2 and final_image[i] == 2:
                final_image[i] = layer[i]

    final_image_code = ''.join(str(e) for e in final_image)
    return final_image_code


def show_image_nicely(code, width, height):
    code = code.replace("1", "O")
    code = code.replace("0", " ")
    curr_line = 0
    while curr_line != height:
        line_start = curr_line * width
        line_end = curr_line * width + width + 1
        code_line = code[line_start:line_end - 1]
        print(code_line)
        curr_line += 1


my_layers = get_layers_from_code(image_data, 25, 6)

# PART 1
min_digit_layer = find_min_digit_layer(0, my_layers)
operation_result = operation_on_layer(1, 2, min_digit_layer)
# print(my_layers)
# print(min_digit_layer)
print(operation_result)

# PART 2
image = generate_final_img(my_layers, 25, 6)
show_image_nicely(image, 25, 6)



