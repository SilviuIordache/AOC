# print('[1518-02-28 00:47]' > '[1518-02-28 00:46]')

filepath = 'input.txt'

logs = []
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        # print("Line %s: %s" % (cnt, line.strip()))
        line = fp.readline()
        logs.append(line.strip())
        cnt += 1

# todo SORT THE LOGS


# print(logs[2])
# print(arr[2].strip().split(' '))

def displayArr(arr):
    for item in arr:
        print(item)

logs.sort()

displayArr(logs)

