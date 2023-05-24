#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> col;

bool isValid(int depth){
    for(int i=0;i<depth;i++){
        if ((col[i]==col[depth]) || (abs(i-depth) == abs(col[i]-col[depth]))){
            return false;
        }
    }
    return true;
}

int queen(int depth, int &count){
    if (depth == n){
        count++;
    }
    else{
        for(int i = 0;i<n;i++){
            col.push_back(i);
            if (isValid(depth)){
                queen(depth+1,count);
            }
            col.pop_back();
        }
    }
    return count;
}

int main()
{
    cin >> n;
    int count = 0;
    cout << queen(0,count);
}
