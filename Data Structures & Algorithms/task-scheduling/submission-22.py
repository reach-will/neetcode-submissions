from typing import NamedTuple

class CooldownEntry(NamedTuple):
    remaining_count: int
    task: str
    next_available_cycle: int

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
            if task_cooldown_queue:
                remaining_count, task, next_available_cycle = task_cooldown_queue[0]

                # cooldowns are FIFO in order of next_available_cycle,
                # so only front can become available next
                if cycle >= next_available_cycle:
                    task_cooldown_queue.popleft()
                    heapq.heappush(task_priority_queue, (-remaining_count, task))

            neg_count, task = heapq.heappop(task_priority_queue)
            count = -neg_count
            if count > 1:
                task_cooldown_queue.append(CooldownEntry(count - 1, task, cycle + n + 1))

            cycle += 1

        finish_cycle = cycle
        while task_cooldown_queue:
            remaining_count, _, next_available_cycle = task_cooldown_queue.popleft()

            # remaining occurrences execute every n + 1 cycles
            finish_cycle = max(finish_cycle, next_available_cycle + (remaining_count - 1) * (n + 1) + 1)

        return finish_cycle
