def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(data, i, swaps)
    return swaps

def min_heapify(data, i, swaps):
    n = len(data)
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and data[left_child] < data[smallest]:
        smallest = left_child

    if right_child < n and data[right_child] < data[smallest]:
        smallest = right_child

    if i != smallest:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]
        min_heapify(data, smallest, swaps)

def main(): 
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
