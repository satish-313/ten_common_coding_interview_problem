'''
  In kth largest is a problem in which we find out about the kth largest number
  simple
'''

arr = [1,4,2,7,7,9,12,0,6]
kth = 4

# basic loop over find the max and delete it and repeat kth last one is kth largest
def simple_loop(arr,kth):
  for i in range(kth-1): # O(k)
    arr.remove(max(arr)) # remove O(n) + max O(n)
  return max(arr) # max O(n)

sl = arr.copy()
print(simple_loop(sl,kth)) # time complexity O(k*n)

# another way is sort the arr return n-k index
def sort_kth(arr,kth): 
  sort_arr = sorted(arr) # O(nlog(n)) for sorting
  return sort_arr[len(arr) - kth] # O(1)

sortkth = arr.copy()
print(sort_kth(arr,kth)) # time complexity O(nlog(n))

# another a more efficient is using heap (I still don't understand concept)
import heapq

def heap_way(arr,kth):
  # in heapq consist on only min heap there for we are extraction into negative sign
  new_arr = [-e for e in arr] # O(n)
  
  heapq.heapify(new_arr) # O(n)
  for i in range(kth-1): # O(k)
    heapq.heappop(new_arr) # O(log(n))
  return -heapq.heappop(new_arr)
  
print(heap_way(arr,kth)) # time complexity O(klog(n)) if n is large and k also large then O(nlog(n))
