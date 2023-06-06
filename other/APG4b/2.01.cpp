#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> data(5);
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
  }

  int memo = data.at(0);
  bool flg = false;
    
  for (int i = 1; i < 5; i++){

    if (memo == data.at(i)){
        cout << "YES" << endl;
        flg = true;
        break;
    }

    memo = data.at(i);

  }

  if (flg == false){
    cout << "NO" << endl;
  }
}
