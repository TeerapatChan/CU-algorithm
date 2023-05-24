#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int n,s1,s2,s3,m;
vector<int> a,b,c;

void printvector(vector<int> v){
    for (auto x: v)
        cout << x << " ";
}

vector<int> bfs(vector<vector<int>> adjList, int s){
    vector<int> d(n,INT_MAX);
    d[s] = 0;
    queue<int> q;
    q.push(s);

    while(!q.empty()){
        int u;
        u = q.front();
        q.pop();
        for(auto v: adjList[u]){
            if (d[v] == INT_MAX){
                d[v] = d[u]+1;
                q.push(v);
            }
        }
    }
    return d;
}
int main()
{
    cin >> n;
    cin >> s1 >> s2 >> s3;
    s1--;
    s2--;
    s3--;
    vector<vector<int>> adjList;
    for(int i=0;i<n;i++){
        int m,x;
        cin >> m;
        vector<int> temp;
        for(int j=0;j<m;j++){
            cin >> x;
            temp.push_back(x-1);
        }
        adjList.push_back(temp);
    }
    a = bfs(adjList,s1);
    b = bfs(adjList,s2);
    c = bfs(adjList,s3);
    m = INT_MAX;
    for(int i=0;i<n;i++){
        m = min(max(max(a[i],b[i]),c[i]),m);
    }
    cout << m;
}
