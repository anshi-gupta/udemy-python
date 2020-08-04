# Program to find the largest element of an array of size n

def largest(arr, n):
  # initialize maximum element
  max = arr[0]

  for i in range(1, n):
    if arr[i] > max:
      max = arr[i]
  return max

arr = [2, 10, 100, 45, 32]
n = len(arr)
result = largest(arr, n)
print("The array is ", arr)
print("The largest element of given array is ", result)