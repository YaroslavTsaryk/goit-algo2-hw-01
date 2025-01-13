conc = 0
comp = 0


def minmax(arr):
    global conc
    global comp
    print(arr)
    min_v = 0
    max_v = 0
    if len(arr) > 3:
        print("DIV")
        mid = len(arr) // 2
        print(f"### {arr[:mid]}   |  {arr[mid:]}")
        r1 = minmax(arr[:mid])
        r2 = minmax(arr[mid:])

        print(f"CONCAT: {r1}  |  {r2}")
        conc += 1
        if r1[0] < r2[0]:
            min_v = r1[0]
        else:
            min_v = r2[0]
        comp += 1
        print(f"COMPAIR: {min_v},{max_v}")
        if r1[1] < r2[1]:
            max_v = r2[1]
        else:
            max_v = r1[1]
        comp += 1
        print(f"COMPAIR: {min_v},{max_v}")
    elif len(arr) == 2:
        print("ARR2")
        if arr[0] > arr[1]:
            min_v = arr[1]
            max_v = arr[0]
        else:
            min_v = arr[0]
            max_v = arr[1]
        comp += 1
        print(f"COMPAIR: {min_v},{max_v}")
    else:
        print("ARR3")
        if arr[0] > arr[1]:
            min_v = arr[1]
            max_v = arr[0]
        else:
            min_v = arr[0]
            max_v = arr[1]
        comp += 1
        print(f"COMPAIR: {min_v},{max_v}")
        if arr[2] < min_v:
            min_v = arr[2]
        comp += 1
        print(f"COMPAIR: {min_v},{max_v}")
        if arr[2] > max_v:
            max_v = arr[2]
        comp += 1
        print(f"COMPAIR: {min_v},{max_v}")
    print(f"minmax result: {min_v},{max_v}")

    return (min_v, max_v)


a = [1, 3, 5, 9, 3, 4, -5, 17, 23, 34, 54, 7, 12, 3, 4, 9, 56, 34, 5]

minmax(a)
print(f"CAMPARATIONS {comp = }")
print(f"CONCATENATIONS {conc = }")
print(f"array size {len(a)}")
