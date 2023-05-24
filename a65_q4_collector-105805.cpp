#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int n,k;
int ans = INT_MAX;

void solve(int idx, int minimum, vector<bool> &bought,vector<pair<float,pair<int,vector<int>>>> &seller){
    if (minimum >= ans) return;
    int s = 0;
    for(int i=1;i<=n;i++){
        if(bought[i] == 1) {
            s++;
            //cout << i << " ";
        }
        else break;
    }

    if(s == n){
        ans = minimum;
        return;
    }

    if(idx == k) return;

    queue<int> q;
    for(int i=0;i<seller[idx].second.second.size();i++){
        //cout << idx << "->" << seller[idx].second[i] << endl;
        if(bought[seller[idx].second.second[i]] == false){
            bought[seller[idx].second.second[i]] = true;
            q.push(seller[idx].second.second[i]);
            //cout << seller[idx].second[i]<< " ";
        }
    }
    int cost = seller[idx].second.first;
    solve(idx+1, minimum + cost, bought, seller);
    while(!q.empty()){
        bought[q.front()] = false;
        q.pop();
    }
    solve(idx+1, minimum, bought, seller);

}

int main()
{
    cin >> n >> k;
    vector<pair<float,pair<int,vector<int>>>> seller(k);
    vector<bool> bought(n+1,false);

    for(int i=0;i<k;i++){
        float m,price;
        cin >> price >> m;
        vector<int> books(m,0);
        for(int j=0;j<m;j++){
            cin >> --books[j];
        }
        seller[i] = make_pair(price/m,make_pair(price,books));
    }

    sort(seller.begin(), seller.end());
    solve(0,0,bought,seller);
    cout << ans;
}
