class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''

        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for word in strs:
                if len(word) < i + 1 or word[i] != current_char:
                    return common_prefix
            common_prefix += strs[0][i]

        return common_prefix