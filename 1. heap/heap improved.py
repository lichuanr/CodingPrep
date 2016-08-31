#3. 定长数组 nums 中返回最大的两个数。Followup: 返回最大的 k 个数。 
def maxTwo(lst):
    #max array
    maxlst = [float("-inf"), float("-inf")]
    
    for item in lst:
        print item, maxlst
        if item > min(maxlst):
            if max(maxlst) == maxlst[0]:
                maxlst[1] = item
            else:
                maxlst[0] = item      
    print maxlst

import heapq

#build max heap
def maxheapify(i, lst):
    left = 2*i
    right = 2*i + 1
    
    length = len(lst)
    largest = i
    #find the index of the largest number
    if left < length and lst[largest] < lst[left]:
        largest = left
    if right < length and lst[largest] < lst[right]:
        largest = right
    
    #sink down
    if i != largest:
        lst[largest], lst[i] = lst[i], lst[largest]
        #largest is the lowest value, after swapping
        maxheapify(largest, lst)
    
def build_heap(lst, k):
    length = len(lst)
    for i in range(length//2, -1, -1):
        maxheapify(i, lst)
    
    #print lst
    index = 0
    while index < k:
        result = heapq.heappop(lst)
        maxheapify(0, lst)
        #print result, lst
        index += 1
    
    return result
        
if __name__ == "__main__":
    lst = [4, 5, 6, 7, 8, 9, 10]
    k = 3
    print build_heap(lst, k)
    
    lst1 = [7, 6, 4, 5]
    maxTwo(lst)


