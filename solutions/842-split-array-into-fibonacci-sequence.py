class Solution:
    def splitIntoFibonacci(self, S):
        for i in range(len(S)-2):
            for j in range(i+1, len(S)-1):
                if (i > 0 and S[0] == '0') or (j > i+1 and S[i] == '0'):
                    continue
                F1, F2, string = int(S[0:i+1]), int(S[i+1:j+1]), S[j+1:]
                answer = [F1, F2]
                while len(string) != 0:
                    if string.startswith(str(F1+F2)):
                        F1, F2, string = F2, F1+F2, string[len(str(F1+F2)):]
                        answer.append(F2)
                    else:
                        break
                if len(string) == 0:
                    if answer[-1] < 2**31 - 1:
                        return answer
        return []
