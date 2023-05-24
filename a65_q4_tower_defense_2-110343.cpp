#include <iostream>
#include<bits/stdc++.h>
#define vi vector<int>

using namespace std;
int n,m,k,w;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m >> k >> w;
    vi hp(m);
    vi pos(m);
    vector<bool> tower(n,false);
    for(int i=0;i<m;i++){
        cin >> --pos[i];
    }
    for(int i=0;i<m;i++){
        cin >> hp[i];
    }

    for(int i=0;i<m;i++){
        for(int low = max(0,pos[i]-w); low <= min(pos[i]+w,n-1); low++){
            if (k==0) break;
            if (tower[low] == false && hp[i] > 0){
                hp[i]--;
                tower[low] = true;
                k--;
            }
            if (hp[i] == 0) break;
        }
        if (k==0) break;
    }
    int sum = 0;
    for(int i =0;i<m;i++){
        sum += hp[i];
    }
    cout << sum;
}
