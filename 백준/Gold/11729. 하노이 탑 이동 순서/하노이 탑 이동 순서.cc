#include <bits/stdc++.h>
using namespace std;

void Hanoi(int a, int b, int n){
    if(n == 1) {
        cout << a << ' ' << b << '\n';
        return;
    }
    Hanoi(a, 6-a-b, n-1);
    cout << a <<' ' << b <<'\n';
    Hanoi(6-a-b, b, n-1);
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int k;
    cin >> k;
    cout << (int)pow(2,k) -1 << '\n';
    Hanoi(1, 3, k);
}