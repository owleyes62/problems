class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0
        original_x = x

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

        return reversed_number == original_x


sol = Solution()


result1 = sol.isPalindrome(+1212)
print(result1)


result2 = sol.isPalindrome(121)
print(result2)


result3 = sol.isPalindrome(+101)
print(result3)
