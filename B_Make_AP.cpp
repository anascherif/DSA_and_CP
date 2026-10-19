//B. Make AP problem from codeforces
//https://codeforces.com/problemset/problem/1624/B
#include <bits/stdc++.h>
#include <string>

using namespace std;

void solve()
{
    int a, b, c;
    cin >> a >> b >> c;
    if ((a + c) % 2b == 0 or ((2b - c) >= 0 and (2b - c) % a == 0) or ((2b - a) >= 0 and (2b - a) % c == 0))
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        solve();
        cout << "\n";
    }

    return 0;
}
