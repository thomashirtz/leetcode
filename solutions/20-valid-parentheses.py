class Solution:
    def isValid(self, characters):
        length = len(characters)
        if len(characters) % 2 == 1:
            return
        for i in range(length//2):
            characters = characters.replace('[]', '').replace('{}', '').replace('()', '')
        return len(characters) <= 0
