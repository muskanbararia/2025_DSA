'''
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    memo={}
    def climbStairs(self, n: int) -> int:
        '''
         n=1, 1
         n=2, 2
         n=3, 3
         n=4, 3+ 2
         n=5, 5+3
         n=6, 8+5
         n=7, 13+8

        '''
        print(n, self.memo)
        if n <=0:
            return 0
        if n==1:
            ans= 1
        elif n==2:
            ans= 2
        else:
            p1=None
            p2=None
            if (n-1) in self.memo :
                p1 = self.memo[n-1]
            if (n-2) in self.memo:
                p2 = self.memo[n-2]
            if p1:
                if p2:
                    ans= p1+p2
                else:
                    ans= p1+self.climbStairs(n-2)
            else:
                if p2:
                    ans = p2+self.climbStairs(n-1)
                else:
                    ans = self.climbStairs(n-2)+ self.climbStairs(n-1)
        self.memo[n]=ans
        return ans
        