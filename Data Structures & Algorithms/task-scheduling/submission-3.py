from operator import itemgetter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_wait_list_queue = deque()
        task_frequencies = Counter(tasks)
        task_priority_queue = [(-count, task) for task, count in task_frequencies.items()]
        heapq.heapify(task_priority_queue)

        cycle = 0
        while task_priority_queue:
            if task_wait_list_queue and cycle >= task_wait_list_queue[0][2] + n + 1:
                count, task, _ = task_wait_list_queue.popleft()
                heapq.heappush(task_priority_queue, (-count, task))

            negative_count, task = heapq.heappop(task_priority_queue)
            if negative_count != -1:
                task_wait_list_queue.append((-negative_count - 1, task, cycle))

            cycle += 1

        while task_wait_list_queue:
            count, _, timestamp = task_wait_list_queue.popleft()
            cycle = max(cycle, count * (n + 1) + timestamp + 1)

        return cycle
