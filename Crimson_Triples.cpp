//Crimson Triples codeforces 2238/B
#include <bits/stdc++.h>
#include <string>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    
    long long ans = 0; 
        for (int b = 1; b <= n; b++) {
        long long multiples = n / b; 
        ans += multiples * multiples;
    }
    
    cout << ans;
}

int main()
{
    // Fast I/O
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
