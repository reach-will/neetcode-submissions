class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            while numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            j -= 1
        return [0, 0]