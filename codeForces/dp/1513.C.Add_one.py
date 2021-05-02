max_n = 200005
mod = 1000000007
dp = [0]*max_n

for i in range(9):
    dp[i] = 2

dp[9] = 3

for i in range(10,max_n):
    dp[i] = (dp[i-9] + dp[i-10])%mod





if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().split())
        ans = 0
        while(n>0):
            x = int(n%10)
            if m + x < 10:
                ans +=1
            else:
                ans += dp[m+x -10]
            ans %= mod
            n/=10
        
        