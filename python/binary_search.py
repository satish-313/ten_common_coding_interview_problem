'''
  Note - binary search is not present in video but subset of second problem.
  binary search is a most common thing is competetive programing.
  condition 
    - array most be sorted

  return the index, if not return -1
'''

def binarySearch(arr,target):
  low,high = 0,len(arr)-1

  while low <= high:
    mid = (low+high)//2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  
  return -1

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
target = 50
print(binarySearch(arr,target))

