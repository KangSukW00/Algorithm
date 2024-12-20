#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int N;
    cin >> N;
    for(int i=1; i<N; i++){
        int sum = i;
        int tmp = i;
        while(tmp > 0){
            sum += tmp%10;
            tmp /= 10;
        }
        if(sum==N){
            cout<<i;
            return 0;
        }
    }
    cout << 0;
    return 0;
}