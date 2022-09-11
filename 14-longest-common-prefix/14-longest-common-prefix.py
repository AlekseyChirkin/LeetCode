class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''

        if strs[0] == '':
            return ''

        if len(strs[0]) == 1 and len(strs) == 1:
            return strs[0]

        similar_word = strs[0]
        all_words_same = True
        for word in strs:
            if similar_word != word:
                all_words_same = False
        if all_words_same:
            return strs[0]

        first_word = strs[0]
        for i in range(len(first_word)):
            common_prefix = first_word[:i + 1]
            for word in strs:
                if not word.startswith(common_prefix):
                    return common_prefix[:-1]

        return common_prefix