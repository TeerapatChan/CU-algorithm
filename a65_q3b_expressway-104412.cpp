#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int y,cost;
int adjMat[700][700];

vector<int> dijkstra(){
    vector<int> dist(y,INT_MAX);
    dist[0] = 0;
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    pq.push({0,0});
    while(!pq.empty()){
        int du = pq.top().first, u = pq.top().second;
        pq.pop();
        for(int i=0;i<y;i++){
            int dv = adjMat[u][i];
            if (dv > 0 && dv+dist[u] < dist[i]){
                dist[i] = dv+dist[u];
                pq.push({dist[i],i});
            }
        }
    }
    return dist;
}

int main()
{
    cin >> y >> cost;
    adjMat[0][1] = cost;
    adjMat[1][0] = cost;
    for(int i=2;i<y;i++){
        int m;
        cin >> m;
        for(int j=0;j<m;j++){
            int v,c;
            cin >> v >> c;
            v--;
            adjMat[v][i] = c;
            adjMat[i][v] = c;
        }
        cout << dijkstra()[1] << " ";
    }/*
    for(int i =0;i<y;i++){
        for(int j=0;j<y;j++){
            cout << adjMat[i][j] << " ";
        }
        cout << endl;
    }*/
}
