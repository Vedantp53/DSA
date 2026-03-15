class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # 0 is also a palindrome
        if x == 0:
            return True

        div = 1
        while x >= 10 * div:
            div *= 10

        while div > 0:
            right = x % 10
            left = x // div

            if left != right:
                return False

            x = (x % div) // 10
            div //= 100

        return True