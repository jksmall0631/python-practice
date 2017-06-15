import math

def gimme(input_array):
    mid = math.floor(len(input_array) / 2)
    sort = sorted(input_array)
    for index, number in enumerate(input_array):
        if number == sort[mid]:
            return index
