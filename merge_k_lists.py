import heapq

def merge_k_lists(array):
    result = []
    minHeap = []
    
    # Insert first elements of each subarray
    # Tuple = (value, subarray index, emelent index in subarray)
    for i in range(len(array)):
        heapq.heappush(minHeap, (array[i][0], i, 0))
    
    # Merge arrays until minHeap is empty
    while minHeap:
        value, subarray_index, value_index = heapq.heappop(minHeap)
        result.append(value)
        next_value_index = value_index + 1

        if next_value_index < len(array[subarray_index]):
            heapq.heappush(minHeap, (array[subarray_index][next_value_index], subarray_index, next_value_index))
    
    return result

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
