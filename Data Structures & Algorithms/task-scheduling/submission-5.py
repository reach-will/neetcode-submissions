class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequencies = Counter(tasks)

        task_priority_queue = [(-count, task) for task, count in task_frequencies.items()]
        heapq.heapify(task_priority_queue)

        task_cooldown_queue = deque()

        cycle = 0
        while task_priority_queue:
            if task_cooldown_queue and cycle >= task_cooldown_queue[0][2] + n + 1:
                count, task, _ = task_cooldown_queue.popleft()
                heapq.heappush(task_priority_queue, (-count, task))

            neg_count, task = heapq.heappop(task_priority_queue)
            if neg_count != -1:
                task_cooldown_queue.append((-neg_count - 1, task, cycle))

            cycle += 1

        # remaining occurrences execute every n + 1 cycles
        while task_cooldown_queue:
            count, _, last_execution = task_cooldown_queue.popleft()
            cycle = max(cycle, count * (n + 1) + last_execution + 1)

        return cycle
