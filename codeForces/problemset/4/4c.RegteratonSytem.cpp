#include <bits/stdc++.h>
using namespace std;


int main()
{
    int n;
    cin >> n;
    map<string, long> database; 
    while(n--)
    {
        string name;
        cin >> name;

        if(database.find(name) == database.end())
        {
            cout << "OK\n";
            database[name] =1;
        }
        else{
            cout << name << database[name] << endl;
            ++database[name];
        }


    }
}