#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, total = 0, ave = 0;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; i++){
        cin >> A.at(i);
        total += A.at(i);
    }

    ave = total / N;

    for (int i = 0; i < N; i++){
        cout << abs(A.at(i) - ave) << endl;
    }
}