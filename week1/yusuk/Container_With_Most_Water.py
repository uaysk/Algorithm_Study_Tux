class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        # 시간 복잡도: O(n)
        # left와 right 두 포인터는 매 반복마다 둘 중 하나가 안쪽으로 한 칸 이동한다.
        # 포인터가 뒤로 돌아가지 않으므로 최대 n - 1번만 비교하고 반복이 끝난다.
        # 반복 안의 width, min, 곱셈, max, if 비교는 모두 O(1)이므로 전체는 O(n)이다.
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            result = max(result, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result
