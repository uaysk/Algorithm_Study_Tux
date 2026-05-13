class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        # 시간 복잡도: O(n)
        # left는 오른쪽으로, right는 왼쪽으로만 이동하며 이미 검사한 문자는 다시 검사하지 않는다.
        # 안쪽 while문들이 특수문자를 건너뛰더라도 각 문자는 포인터에 의해 최대 한 번씩만 지나간다.
        # 문자 검사(isalnum), 소문자 변환(lower), 비교는 모두 O(1)이므로 전체는 O(n)이다.
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
