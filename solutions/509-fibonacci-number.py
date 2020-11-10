class Solution:
    def fib(self, N):
        if N < 2: return N
        fibonacci = [0]*(N+1)
        fibonacci[1]=1
        for i in range(2, N+1):
            fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
        return fibonacci[N]
