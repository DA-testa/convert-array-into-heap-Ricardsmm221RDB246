import heapq as hq

def assign_jobs(n, jobs):
    assigned_workers = []
    start_times = []
    next_free_time = [(0, i) for i in range(n)]
    hq.heapify(next_free_time)
    for job in jobs:
        next_worker = hq.heappop(next_free_time)
        start_time = next_worker[0]
        worker_index = next_worker[1]
        assigned_workers.append(worker_index)
        start_times.append(start_time)
        hq.heappush(next_free_time, (start_time + job, worker_index))
    return assigned_workers, start_times


def main():
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert m == len(jobs)

    assigned_workers, start_times = assign_jobs(n, jobs)

    for i in range(m):
        print(assigned_workers[i], start_times[i])


if __name__ == '__main__':
    main()

