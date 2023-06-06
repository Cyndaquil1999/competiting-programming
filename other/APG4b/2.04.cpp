#include <bits/stdc++.h>
using namespace std;

int main(){
    int a = 123;
    int &b = a;  // 変数aへの参照
    int &c = a;  // 変数aへの参照

    cout << c << endl;
}