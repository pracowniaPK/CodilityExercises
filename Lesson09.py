def solution(A):
    local_sum = -1000000
    max_sum = -1000000
    for i in A:
        if max_sum >= 0:
            local_sum = max(0, local_sum + i)
        else:
            local_sum = max(local_sum, i, local_sum + i)
        max_sum = max(local_sum, max_sum)
    return max_sum