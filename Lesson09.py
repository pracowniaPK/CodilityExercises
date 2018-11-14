def max_slice_sum(A):
    local_sum = -1000000
    max_sum = -1000000
    for i in A:
        if max_sum >= 0:
            local_sum = max(0, local_sum + i)
        else:
            local_sum = max(local_sum, i, local_sum + i)
        max_sum = max(local_sum, max_sum)
    return max_sum

def max_profit(A):
    min_price = 200000
    prof = 0
    for i in A:
        min_price = min(min_price, i)
        prof = max(prof, i - min_price)
    return prof

def max_double_slice_sum(A):
    A = A[1:-1]
    
    l_max_sum = len(A) * [0]
    for i in range(1,len(A)):
        l_max_sum[i] = max(0, l_max_sum[i-1] + A[i-1])
        
    r_max_sum = len(A) * [0]
    for i in range(1,len(A)):
        j = len(A) - i - 1
        r_max_sum[j] = max(0, r_max_sum[j+1] + A[j+1])
        
    max_max = 0
    for i in range(len(A)):
        max_max = max(max_max, l_max_sum[i] + r_max_sum[i])
    
    return max_max
