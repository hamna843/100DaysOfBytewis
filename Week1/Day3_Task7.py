# # #Maximum Subarray
# #    - Write a program to find the maximum sum of a contiguous subarray within a given array.
# #    - Expected output: If the input array is `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, 
# # the output should be `6`, as the maximum subarray is `[4, -1, 2, 1]`.
# def Maximum_Subarray(Arr):
#     max_sum=Arr[0]
#     current_sum=Arr[0]
#     print(Arr)

#     for i in range(1, len(Arr)):
#         current_sum = max(Arr[i], current_sum + Arr[i])  # Update current_sum
#         max_sum = max(max_sum, current_sum)  # Update max_sum
#         sub_Array.append()
#            # max_array=[i:j:]
#     return(max_sum) 

# Arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print("amx sum= ", Maximum_Subarray(Arr))



def Maximum_Subarray(Arr):
    max_sum = Arr[0]  
    current_sum = Arr[0]  
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(Arr)):
        if current_sum < 0:
            current_sum = Arr[i]
            temp_start = i
        else:
            current_sum += Arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return Arr[start:end+1]

Arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sum subarray: ", Maximum_Subarray(Arr))