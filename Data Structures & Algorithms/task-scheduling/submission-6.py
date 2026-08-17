class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequencies = Counter(tasks)

        task_priority_queue = [(-count, task) for task, count in task_frequencies.items()]
        heapq.heapify(task_priority_queue)

        task_cooldown_queue = deque()

        cycle = 0

        # process while there are executable tasks off cooldown
        # remaining cooldowns are accounted for afterwards
        while task_priority_queue:
            # only need to check front of cooldown queue, since it is FIFO and
            # it is the possible next task to refresh cooldown
            if task_cooldown_queue:
                remaining_count, task, last_execution_cycle = task_cooldown_queue[0]

                if cycle >= last_execution_cycle + n + 1:
                    task_cooldown_queue.popleft()
                    heapq.heappush(task_priority_queue, (-remaining_count, task))

            neg_count, task = heapq.heappop(task_priority_queue)
            if -neg_count != 1:
                task_cooldown_queue.append((-neg_count - 1, task, cycle))

            cycle += 1

        while task_cooldown_queue:
            remaining_count, _, last_execution_cycle = task_cooldown_queue.popleft()

            # remaining occurrences execute every n + 1 cycles
            cycle = max(cycle, remaining_count * (n + 1) + last_execution_cycle + 1)

        return cycle
