# python3


def sift_down(data, i, swaps):
    """Sifts the element down from the given index to its appropriate place."""
    min_index = i
    left_child = 2 * i + 1
    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    right_child = 2 * i + 2
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(data, min_index, swaps)

def build_heap(data):
    """Converts the given array to a heap using only 𝑂(𝑛) swaps."""
    swaps = []
    for i in range(len(data)//2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def main():
    # Reading input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # Checking if length of data is the same as the given length
    assert len(data) == n

    # Calls function to convert the array to heap and returns all swaps
    swaps = build_heap(data)

    # Output how many swaps were made, which should be less than 4n
    print(len(swaps))

    # Output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()```

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
