#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int n,m;
int adjMat[1001][1001];
bool visited[1001]={0};
void dfs(int u){
    visited[u] = true;
    for(int v = 0;v<n;v++){
        if (!visited[v] && adjMat[u][v]){
            dfs(v);
        }
    }
    cout << u << " ";
}
int main()
{
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> m;
        for(int j=0;j<m;j++){
            int tmp;
            cin >> tmp;
            adjMat[i][tmp] = 1;
        }
    }
    for(int i=0;i<n;i++){
        if (!visited[i])
            dfs(i);
    }
}
