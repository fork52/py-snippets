

'''
References: https://stackoverflow.com/questions/25458879/algorithm-to-produce-all-partitions-of-a-list-in-order/25460561
'''

def partition_generator(arr):
    """
    Generates and returns all partitions of an array.
    Time Complexity:  O( 2 ^ (n - 1) * n)
    Space Complexity: O( 2 ^ (n - 1) * n)
    """
    partitions = []
    n = len(arr)

    lim = 1 << (n - 1)
    for mask in range(lim):
        current_partition = []
        current_subset = []
        for ind in range(n):
            current_subset.append(arr[ind])
            if mask & (1 << ind) or ind == n - 1:
                current_partition.append(current_subset)
                current_subset = []
        partitions.append(current_partition)

    return partitions


if __name__ == '__main__':
    arr = [1, 2, 3, 4]

    partitions = partition_generator(arr)

    print('The partitions are:')
    for current_partition in partitions:
        print(current_partition)
