from queue import PriorityQueue

def parallel_processing(n, m, data):
    output = []
    next_thread = 0
    threads = PriorityQueue()

    for i in range(n):
        threads.put((0, i))

    for i in range(m):
        time_required = data[i]
        thread_start_time, thread_number = threads.get()

        output.append((thread_number, thread_start_time))

        thread_finish_time = thread_start_time + time_required
        threads.put((thread_finish_time, thread_number))

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
