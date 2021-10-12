def largest(arr,n):

    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
        
    return max

def smallest(arr,n):


    min = arr[0]


    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    return min

print("These are the time moments from the stop_watch in seconds")
arr = (10, 324, 45, 90, 980, 40)
n = len(arr)
Ans1 = largest(arr, n)
Ans2 = smallest(arr, n)
print("Largest is",Ans1)
print("Smallest is",Ans2)
print("Here you go sucka")