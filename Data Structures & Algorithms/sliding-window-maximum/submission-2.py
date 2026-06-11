class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        window = deque()
        for i, n in enumerate(nums[:k-1]):
            while window and (window[0] < i + 1 - k or nums[window[0]] <= n):
                window.popleft()
            while window and nums[window[-1]] <= n:
                window.pop()
            window.append(i)
        ans = []
        for i, n in enumerate(nums[k-1:], start=k-1):
            print(window)
            while window and window[0] < i + 1 - k:
                window.popleft()
            while window and nums[window[-1]] <= n:
                window.pop()
            window.append(i)
            ans.append(nums[window[0]])
        return ans