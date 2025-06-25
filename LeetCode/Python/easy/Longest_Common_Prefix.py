class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefixo = strs[0]

        for palavra in strs[1:]:

            min_len = min(len(prefixo), len(palavra))
            novo_prefixo = ""

            for i in range(min_len):
                if prefixo[i] == palavra[i]:
                    novo_prefixo += prefixo[i]
                else:
                    break

            prefixo = novo_prefixo

            if not prefixo:
                break

        return prefixo


sol = Solution()

strs = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
example_1 = sol.longestCommonPrefix(strs)
print(example_1)

example_2 = sol.longestCommonPrefix(strs2)
print(example_2)
