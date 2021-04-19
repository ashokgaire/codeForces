#include<bits/stdc++.h>


using namespace std;

int main() {
  string a;
  vector<int> mas, b;
    cin >> a;
    for (int i = 0; i < a.size(); i += 2) {
        mas.push_back(a[i]-48);
        
    }
    sort(mas.begin(), mas.end());
    cout << mas[0] ;
    for (int i = 1; i < a.size()/2+1; i++) {
        cout << "+" << mas[i];
    }

    return 0;
}