#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <utility>

using namespace std;


int main()
{
    int n,c,m,give, i = 0;
    string s;
    vector<string> v;
    map<string, int> nmap;
    while(scanf("%d", &n) != EOF) {
        if(i++) cout << endl;

        nmap.clear();
        v.clear();
        for(int i = 0; i < n; i++) {
            cin >> s;
            v.push_back(s);
            nmap.insert(make_pair(s,0));
        }

        while(n--) {
            cin >> s >> c >> m;
            if(m) {
                give = c/m;
                nmap[s] -= give * m;
            }
            while(m--) {
                cin >> s;
                nmap[s] += give;
            }
        }

        for(auto s : v)
            cout << s << " " << nmap[s] << endl;
    }
}
