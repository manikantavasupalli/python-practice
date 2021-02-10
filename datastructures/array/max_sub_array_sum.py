def maxSubArraySum(a,size): 
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1, size):
        curr_max = max(a[i], curr_max+a[i]) # current running seq with greate value
        max_so_far = max(curr_max, max_so_far) # greater sequence formed so far
    return max_so_far


a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print(maxSubArraySum(a, len(a)))