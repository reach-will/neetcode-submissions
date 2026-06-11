class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        window = deque()
        for i, n in enumerate(nums[:k-1]):
            while window and nums[window[-1]] <= n:
                window.pop()
            window.append(i)
            if window[0] < i + 1 - k:
                window.popleft()
        ans = []
        for i, n in enumerate(nums[k-1:], start=k-1):
            while window and nums[window[-1]] <= n:
                window.pop()
            window.append(i)
            if window[0] < i + 1 - k:
                window.popleft()
            ans.append(nums[window[0]])
        return ans