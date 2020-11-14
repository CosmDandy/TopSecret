def mirror(arr):
    mirrored_part = arr.copy().reverse()
    arr += mirrored_part
    return arr