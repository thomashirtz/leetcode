class Solution:
    def romanToInt(self, string):
        value_previous_character = 1
        answer = 0
        dictionary = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for character in string[::-1]:
            if dictionary[character] >= value_previous_character:
                answer += dictionary[character]
                value_previous_character = max(dictionary[character],value_previous_character)
            else :
                answer -= dictionary[character]
        return answer
        

number = "MCMXCIV"
print(Solution().romanToInt(number))