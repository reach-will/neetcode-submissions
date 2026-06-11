class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        descending_height_indexes = sorted(range(len(heights)), key=heights.__getitem__, reverse=True)
        lens = Counter()
        max_area = 0
        for ind in descending_height_indexes:
            if ind - 1 in lens and ind + 1 in lens:
                left_border = ind - 1 - lens[ind - 1] + 1
                right_border = ind + 1 + lens[ind + 1] - 1
                lens[right_border] = lens[left_border] = lens[left_border] + lens[right_border] + 1
                max_area = max(max_area, heights[ind] * lens[right_border])
                continue
            if ind - 1 in lens:
                left_border = ind - 1 - lens[ind - 1] + 1
                lens[left_border] += 1
                lens[ind] = lens[left_border]
                max_area = max(max_area, heights[ind] * lens[ind])
                continue
            if ind + 1 in lens:
                right_border = ind + 1 + lens[ind + 1] - 1
                lens[right_border] += 1
                lens[ind] = lens[right_border]
                max_area = max(max_area, heights[ind] * lens[ind])
                continue
            lens[ind] = 1
            max_area = max(max_area, heights[ind])
        return max_area
