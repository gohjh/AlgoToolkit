"""
Sort a given sequence of numbers (that
may contain duplicates) using a modification of RandomizedQuickSort that works in
O(nlogn) expected time.

input: integer arr with n elements (may have rep)
output: sorted arr (by quicksort) in O(nlogn) runtime

QuickSort--------------------
- worst case: O(n^2)
- avg case: O(nlogn)

# Tail recursion elimination ---------------
while l < r:
    m<-partition(A,l,r)
    QuickSort(A,l,m-1)
    l <- m + 1
    
Partition with deterministic pivot selection heuristic
Algo:
1. random select element x
2. get set of elem < x --> cSmall
3. get set of elem > x --> cLarge
4. randomquicksort(cSmall)
5. randomquicksort(cLarge)
6. combine both sorted sets and return as arr


"""
from random import randint


def partition3(array, left, right):
    # if all elements are same, split the set c into 2.
    # write your code here
    
    pivot_value = array[left]
    # Initialize pointers
    p_less = left
    curIndex = left
    p_greater = right
    
    while curIndex <= p_greater:
        if array[curIndex] < pivot_value:
            # swap values
            array[curIndex], array[p_less]= array[p_less], array[curIndex]
            p_less +=1
            curIndex+=1
        elif pivot_value == array[curIndex]:
            curIndex+=1
        else:
            array[curIndex], array[p_greater] =array[p_greater], array[curIndex]
            p_greater-=1  
    return p_less,p_greater                            
    """                
    m1 = left
    for i in range(left+1,m1):
        if array[i] <= array[left]
        
    m2 = left
    for i in range(left,m2):
        if array[i] <= array[left]    
    return m1,m2
    """
def randomized_quick_sort(array, left, right):
    if len(array) == 1:
        return array
    if left >= right:
        return
    k = randint(left, right) # random pivot num
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right) # Pivot indexes
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
