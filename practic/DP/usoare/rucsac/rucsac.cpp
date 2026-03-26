#include <bits/stdc++.h>
using namespace std;

ifstream fin("rucsac.in");
ofstream fout("rucsac.out");

int main() {
    int n, g;
    fin >> n >> g;

    vector<int> w(n), p(n);
    for (int i = 0; i < n; i++)
        fin >> w[i] >> p[i];

    vector<vector<int>> dp(n + 1, vector<int>(g + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= g; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j >= w[i - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i - 1]] + p[i - 1]);
        }
    }

    fout << dp[n][g];
}
