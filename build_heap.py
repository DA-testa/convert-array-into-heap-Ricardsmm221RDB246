import heapq

def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)]  # initialize each thread with start time 0
    heapq.heapify(threads)  # convert the list into a heap
    
    output = []
    for i in range(m):
        time, thread = heapq.heappop(threads)  # get the earliest available thread
        output.append((thread, time))
        heapq.heappush(threads, (time + data[i], thread))  # add the job duration to the thread's start time
    
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()

