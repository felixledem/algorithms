def max_slice(arr):
    result = 0
    local_max = 0
    for x in arr:
        local_max = max(0, local_max + x)
        result = max(result, local_max)
    return result
