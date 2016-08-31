#2, Return k biggest numbers in a unsorted array 
#(both heap and partition select)

import heapq
#inorder  
class Solution(object):
    #O(nlogn)
    def k_biggest(self, list1, k):
        heap = []
        list1 = [-i for i in list1]
        
        for item in list1:
            heapq.heappush(heap, item)
        
        for i in range(0, k):
            print - heapq.heappop(heap)

    
    def maxHeapify(self, list1, i):
        left = 2*i
        right = 2*i + 1
        
        largest = i
        if left < len(list1) and list1[left] > list1[largest]:
            largest = left
        
        if right < len(list1) and list1[right] < list1[largest]:
            largest = right
        
        #current item does not have the largest value
        if largest != i:
            list1[i], list1[largest] = list1[largest], list1[i]
            #keep swimming down the element
            self.maxHeapify(list1, largest)
    
    #O(n)
    def k_biggest2(self, list1, k):
        for i in range(len(list1)//2, -1, -1):
            self.maxHeapify(list1, i)
        
        print "news", list1
        #O(k)
        for i in range(k):
            if k-1 == i:
                print heapq.heappop(list1)
            else:
                heapq.heappop(list1)
    

if __name__ == "__main__":
    #list1 = [11, 2, 1, 0]
    lst = [4, 5, 6, 7, 8, 9, 10]
    k = 4
    Solution().k_biggest2(lst, k)
    #print lst
