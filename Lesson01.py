from math import floor, log

def BinaryGap(n):
    start = floor(log(n, 2))
    
    local_gap = 0
    max_gap = 0
    for i in range(start, -1, -1):
        if 2**i <= n:
            n -= 2**i
            max_gap = max(local_gap, max_gap)
            local_gap = 0
        else:
            local_gap += 1
        
    
    return max_gap