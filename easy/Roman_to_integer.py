class Solution:
    def romanToInt(self, s: str) -> int:
        numeros_romanos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s) - 1):
            letra_atual = s[i]
            letra_seguinte = s[i + 1]

            if numeros_romanos[letra_atual] < numeros_romanos[letra_seguinte]:
                total -= numeros_romanos[letra_atual]
            else:
                total += numeros_romanos[letra_atual]

        total += numeros_romanos[s[-1]]
        return total


sol = Solution()

example_1 = sol.romanToInt("III")
print(example_1)

example_1 = sol.romanToInt("LVIII")
print(example_1)

example_1 = sol.romanToInt("MCMXCIV")
print(example_1)
