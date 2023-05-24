#include <bits/stdc++.h>
using namespace std;

int n,k,mod = 100000007;
map<pair<int,int>, int> dp;

int solve(int idx, int prev_idx){
    if (idx == n){
        return 1;
    }
    pair<int,int> p = make_pair(idx,prev_idx);
    if (dp.find(p) != dp.end()){
        return dp[p];
    }

    int count;
    count = solve(idx+1,prev_idx) % mod;

    if (idx - prev_idx >= k){
        count += solve(idx+1,idx) % mod;
    }
    dp[p] = count % mod;
    return dp[p];
}

int main()
{
    cin >> n >> k;
    cout << solve(0,-1*k);
}