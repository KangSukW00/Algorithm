#include <bits/stdc++.h>
using namespace std;

bool isused1[40];
bool isused2[40];
bool isused3[40];

int cnt = 0;
int n;
void Queen(int cur){
    if(cur == n){
        cnt ++;
        return;
    }
    for(int i=0; i < n; i++){
        if( isused1[i] || isused2[cur+i] || isused3[cur-i+n-1] == 1 ) continue;
        isused1[i] = 1;
        isused2[cur+i] = 1;
        isused3[cur-i+n-1] = 1;
        Queen(cur+1);
        isused1[i] = 0;
        isused2[cur+i] = 0;
        isused3[cur-i+n-1] = 0;
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    Queen(0);
    cout << cnt;
}