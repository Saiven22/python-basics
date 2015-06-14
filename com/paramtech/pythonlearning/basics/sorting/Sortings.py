'''
Created on May 12, 2015

@author: bisdallas
'''
def selection_sort(unsorted_list):
    '''
    SELECT least item and move it to first 
    and repeat it until unsorted portion is left
    '''
    top_index = 0
    list_size = len(unsorted_list)
    
    while top_index < list_size:
        inner_index = min_index = top_index
        swap = False
        while inner_index < list_size:
            if unsorted_list[min_index] > unsorted_list[inner_index]:
                print min_index, inner_index
                min_index = inner_index
                
                swap = True    
            inner_index += 1
        (unsorted_list[min_index], unsorted_list[top_index]) = (unsorted_list[top_index], unsorted_list[min_index])        
        print "after index", top_index, unsorted_list
        if not swap:
            print swap
            print 'swap is not happened in last iteration and return here'
            print unsorted_list
            return unsorted_list
        top_index += 1
    print unsorted_list
    return unsorted_list
def bubble_sort(unsorted_list):
    '''
    compare next two items swap them if left one is greater than right one
    and repeat it for n=size of array.
    moving highest  element to end
    '''
    top_index = 0
    list_size = len(unsorted_list)
    while top_index < list_size:
        for x in range(list_size - top_index - 1) :
            if x < list_size - top_index:  # this condition is irrelevant as we reduce range
                if unsorted_list[x] > unsorted_list[x + 1]:
                    print 'swamping', x, x + 1
                    (unsorted_list[x + 1], unsorted_list[x]) = (unsorted_list[x ], unsorted_list[x + 1])
            else: 
                print 'remaining portion is already sorted', unsorted_list[x:]
                break        
        print "index ", top_index, unsorted_list
        top_index += 1
    print unsorted_list
    return unsorted_list
def insertion_sort(unsorted_list):
    ''' iterate over the elements and put each element in correct position in sorted portion of list
    '''
    list_size = len(unsorted_list)
    top_index = 0
    while top_index < list_size:
        for x in range(top_index):
            if unsorted_list[x] > unsorted_list[top_index]:
                current_value = unsorted_list.pop(top_index)
                print current_value
                print unsorted_list
                unsorted_list.insert(x, current_value)
                print "inserting..", x, current_value, unsorted_list
        print "after index ", top_index, unsorted_list
        top_index += 1
    print unsorted_list
    return unsorted_list
def merge_sort(unsorted_list):
    ''' 
    divered list into two portions and left,right  if size is 1,return that list as its sorted form,once call recursive both left and right arrays
    and merge sorted lists into single 
    '''
    list_size = len(unsorted_list)
    if list_size == 1:
        print unsorted_list
        return unsorted_list
    l_unsorted = unsorted_list[:list_size / 2]
    r_unsorted = unsorted_list[list_size / 2:]
    l_list = merge_sort(l_unsorted)
    r_list = merge_sort(r_unsorted)
    merged_sort = merge(l_list, r_list)
    print merged_sort
    return merged_sort

def merge(l_list, r_list):
    merge_list = []
    l_index = r_index = 0
    while l_index < len(l_list) and r_index < len(r_list):
        if l_list[l_index] < r_list[r_index]:
            merge_list.append(l_list[l_index])
            l_index += 1
        else:
            merge_list.append(r_list[r_index])
            r_index += 1
    while l_index < len(l_list) :
            merge_list.append(l_list[l_index])
            l_index += 1
    while  r_index < len(r_list):
            merge_list.append(r_list[r_index])
            r_index += 1
    return merge_list

def quick_sort(unsorted_list , start_index=0, end_index=None):
    ''' 
    divered list into two portions and left,right  if size is 1,return that list as its sorted form,once call recursive both left and right arrays
    and merge sorted lists into single 
    '''
    if end_index == None:
        end_index = len(unsorted_list)
    
    print 'quick sort', unsorted_list, start_index, end_index
    if(start_index < end_index):
        pivort_index = get_pivot_index(unsorted_list, start_index, end_index) 
#         print "pivot index", pivort_index, unsorted_list
        quick_sort(unsorted_list, 0, pivort_index - 1)
        quick_sort(unsorted_list, pivort_index + 1, end_index)
    print unsorted_list

def get_pivot_index(unsorted_list, start_index, end_index):
    pivort_index = start_index
    pivort_value = unsorted_list[end_index - 1]
    print "got pivort_index..", pivort_index, unsorted_list[start_index:end_index - 1]
    for temp_index in range(start_index, end_index - 1):
        # assume pivot index as startinde and pivot value as last index value 
        # iterate from start_index 2 end_index index if value is less than pivot value, swap current index value with Pivot_index value
        # and increase pivot_index
        # swap last element value and pivot index value
        if unsorted_list[temp_index] <= pivort_value:
            print "swaping..", unsorted_list[temp_index], unsorted_list[pivort_index]
            (unsorted_list[temp_index], unsorted_list[pivort_index]) = (unsorted_list[pivort_index], unsorted_list[temp_index])
            pivort_index += 1
    print "final Swaping..", unsorted_list[end_index - 1], unsorted_list[pivort_index]         
    (unsorted_list[end_index - 1], unsorted_list[pivort_index]) = (unsorted_list[pivort_index], unsorted_list[end_index - 1])
    
    print "got pivort_index..", pivort_index, unsorted_list[start_index:end_index - 1]
    return pivort_index
            
            
if __name__ == '__main__':
    unsorted_list = [2, 3, 7, 1, 4, 9, 3, 1, 4]
    unsorted_list = [2, 58, 2, 9934, 56, 3, 77, 8, 33, 909, 34, 67845, 3, 7, 1, 4, 9, 3, 1, 4]
#     selection_sort([3, 1, 5, 6, 4, 2])
#     bubble_sort([3, 2, 5, 6, 4, 1, 1])
#     insertion_sort(unsorted_list)
#     merge_sort(unsorted_list)
    quick_sort(unsorted_list)
