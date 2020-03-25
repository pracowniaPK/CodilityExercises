def CountFactors(N):
    f_number = 0
    for i in range(1, int(N**.5)+1):
        if N % i == 0:
            f_number += 1
    f_number *= 2
    if N**.5 % 1 == 0:
        f_number -= 1
        
    return f_number

def Flags(A):
    distances = []
    last_distance = 0
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            distances.append(last_distance+1)
            last_distance = 0
        else:
            last_distance += 1
    
    flags_number = int(len(A)**.5)+1
    actual_number = 0
    while (flags_number >= actual_number):
        additional_distance = 0
        actual_number = 1
        for d in distances[1:]:
            if additional_distance + d >= flags_number:
                additional_distance = 0
                actual_number += 1
            else:
                additional_distance += d
            if actual_number == flags_number:
                break
        flags_number -= 1
    if len(distances) == 0: 
        actual_number = 0
        
    return actual_number

def MinPerimeterRectangle(N):
    factor = int(N**0.5)
    while N / factor % 1 != 0:
        factor -= 1
    
    A = factor
    B = N / factor
        
    return int(2 * (A + B))

def peaks(A):
    length = len(A)
    peaks = []
    last_distance = 0
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            try:
                peaks.append(peaks[-1]+last_distance+1)
            except IndexError:
                peaks.append(last_distance+1)
            last_distance = 0
        else:
            last_distance += 1
    
    parts = len(peaks)
    if parts is 0:
        return 0
        
    def checkPeaks(parts, peaks, length):
        if length % parts == 0:
            k = int(length / parts)
            peak = 0
            for i in range(parts):
                while not i*k <= peaks[peak] < (i+1)*k:
                    if peak >= len(peaks)-1:
                        return False
                    peak += 1
            return True
        else:
            return False
    while True:
        if checkPeaks(parts, peaks, length):
            return parts
        parts -= 1    
    

