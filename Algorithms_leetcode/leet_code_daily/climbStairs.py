class Solutions:
    def climbStair(self,n):
        a,b = 1,1
        for i in range(1,len(n)):
            a,b = a+b,b
        return a