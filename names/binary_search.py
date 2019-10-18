def binary_search(list, target):
    if len(list) == 0:
        return -1
    low = 0
    high = len(list) - 1
    while low <= high:
        guess = (low + high) // 2
        if list[guess] == target:
            return 1
        elif list[guess] > target:
            high = guess - 1
        else:
            low = guess + 1
    return -1
