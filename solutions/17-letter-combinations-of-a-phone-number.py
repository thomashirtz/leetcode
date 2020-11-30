class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return ""
        dictionnary = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                       '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                       '8':['t','u','v'],'9':['w','x','y','z']}
        digits = str(digits)
        table = dictionnary[digits[0]]
        for digit in digits[1:]:
            table_ = []
            for char in dictionnary[digit]: #3
                for string in table:
                    table_.append(string+char)
            table = table_
        return table