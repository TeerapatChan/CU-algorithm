#include <iostream>
#include <bits/stdc++.h>

typedef std::pair<int,int> p;

using namespace std;
bool isValid(vector<string> v,int r,int c){
    if (r < 0 || r >= v.size() ||
        c < 0 || c >= v[0].size()){
        return false;
    }
    if (v[r][c] == '#'){
        return false;
    }

    return true;
}

int BFS(vector<vector<int>> adjList, int start,int stop){
    vector<int> d(adjList.size()*adjList.size(), INT_MAX);
    queue<int> q;
    d[start] = 0;
    q.push(start);
    while(!q.empty()){
        int u = q.front();
        q.pop();
        for(int i=0;i<adjList[u].size();i++){
            int v = adjList[u][i];
            if (d[v] == INT_MAX){
                d[v] = d[u]+1;
                q.push(v);
            }
        }

    }
    if (d[stop] == INT_MAX) return -1;
    return d[stop];
}


int main()
{
    int r,c;
    string x;
    cin >> r >> c;
    vector<string> v;
    for(int i=0;i<r;i++){
        cin >> x;
        v.push_back(x);
    }
    vector<vector<int>> adjList(r*c,vector<int>());
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if (v[i][j] != '#'){
                if (isValid(v,i-1,j)){
                    adjList[i*c+j].push_back((i-1)*c+j);
                }
                if (isValid(v,i,j-1)){
                    adjList[i*c+j].push_back(i*c+j-1);
                }
                if (isValid(v,i,j+1)){
                    adjList[i*c+j].push_back(i*c+j+1);
                }
                if (isValid(v,i+1,j)){
                    adjList[i*c+j].push_back((i+1)*c+j);
                }
            }
        }
    }
    cout << BFS(adjList,0,r*c-1);

    /*for(int i=0;i<adjList.size();i++){
        for(int j=0;j<adjList[i].size();j++){
            cout << i << " " << adjList[i][j];
            cout << endl;
        }
        cout << "---------------"<< endl;
    }*/

}
