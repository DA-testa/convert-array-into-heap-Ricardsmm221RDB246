def heapify(data, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] < data[smallest]:
        smallest = left

    if right < n and data[right] < data[smallest]:
        smallest = right

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        swaps.append((i, smallest))
        heapify(data, n, smallest, swaps)


def build_heap(data, n):
    swaps = []
    for i in range(n // 2, -1, -1):
        heapify(data, n, i, swaps)
    return swaps


def main():
    try:
        n = int(input())
        data = list(map(int, input().split()))

        assert len(data) == n

        swaps = build_heap(data, n)

        print(len(swaps))
        for swap in swaps:
            print(swap[0], swap[1])

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
