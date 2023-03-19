import heapq

class Worker:
    def __init__(self, index):
        self.index = index
        self.next_free_time = 0

    def __lt__(self, other):
        return self.next_free_time < other.next_free_time

    def assign_job(self, job_duration, current_time):
        self.next_free_time = current_time + job_duration

def assign_jobs(n_workers, jobs):
    worker_queue = [Worker(i) for i in range(n_workers)]
    result = []
    for job_index, job_duration in enumerate(jobs):
        worker = heapq.heappop(worker_queue)
        result.append((worker.index, worker.next_free_time))
        worker.assign_job(job_duration, worker.next_free_time)
        heapq.heappush(worker_queue, worker)
    return result

n_workers, n_jobs = map(int, input().split())
jobs = list(map(int, input().split()))

assigned_jobs = assign_jobs(n_workers, jobs)

for job in assigned_jobs:
    print(job[0], job[1])

