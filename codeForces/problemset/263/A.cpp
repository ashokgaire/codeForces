#include <bits/stdc++.h>

using namespace std;


int main()
{

  int mat[5][5];
  pair<int, int> index;

  for(int i = 0; i < 5; i++){
    for(int j = 0; j < 5; j++){
        int val;
        cin >> val;
        mat[i][j] = val;

        if(val == 1){
            index.first= i;
            index.second = j;
        }
    }
}

int moves = abs(2 - index.first) + abs(2 - index.second);
cout << moves;
    return 0;
}