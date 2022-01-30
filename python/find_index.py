'''
  In these program we will learn about the find indexes of same element in an array
  condition - 
    - array most be sorted
  
  input - array, target value
  output - start index and end index of array return [start, end]
         - if not in array return [-1,-1]
'''

# using the loop or normal approach
# my solution
def find_indexes_loop(arr,target): # time complexity O(n^2)
  start,end = -1,-1

  for i in range(len(arr)):
    if arr[i] == target:
      start = i
      end = i
      while i+1 < len(arr) and arr[i+1] == target:
        i = i + 1
        end = i
      
      break
  
  return [start,end]

# video solution
def start_end_index(arr,target):
  for i in range(len(arr)):
    if arr[i] == target:
      start = i

      while i+1 < len(arr) and arr[i+1] == target:
        i += 1
      
      return [start,i]
  
  return [-1,-1]

arr = [0,1,1,1,3,4,4,6,6,6,8,8,9,9,9,9,12,12,13,15,29,29]
target = 29

# print(find_indexes_loop(arr,target))
print(start_end_index(arr,target))

# using binary search reduce O(n^2) to O(log(n))
def binary_search_start(arr,target):
  l,h = 0,len(arr) - 1

  if arr[l] == target:
    return l

  while l<=h:
    mid = (l+h)//2

    if arr[mid] == target and arr[mid - 1] < target:
      return mid
    elif arr[mid] > target:
      h = mid - 1
    else:
      l = mid  + 1
  
  return -1

def binary_search_end(arr,target):
  l,h = 0,len(arr) - 1
  
  if arr[h] == target:
    return h

  while l<=h:
    mid = (l+h)//2

    if arr[mid] == target and arr[mid + 1] > target:
      return mid
    elif arr[mid] > target:
      h = mid - 1
    else:
      l = mid  + 1
  
  return -1



def binary_approach(arr,target):

  start = binary_search_start(arr,target)
  end = binary_search_end(arr,target)

  return [start,end]

print(binary_approach(arr,target))