class Solution:
    def longestCommonPrefix(self, strings):
        if not strings or strings == [""]:
            return ""
        if len(strings) == 1:
            return strings[0]
        length = min(len(string) for string in strings)
        if length == 0:
            return ""
        for i in range(length):
            character = strings[0][i]
            for string in strings[1:]:
                if character != string[i]:
                    return strings[0][:i]
            i +=1
        return strings[0][:i]