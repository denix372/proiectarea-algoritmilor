#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;

int alee(int n, const vector<pair<int,int>>& trees,
         int x1, int x2, int y1, int y2)
{
    vector<vector<int>> a(n + 1, vector<int>(n + 1, 0));
    for (auto &p : trees) {
        int x = p.first;
        int y = p.second;
        a[x][y] = 1;
    }

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    queue<pair<int,int>> q;

    dist[x1][x2] = 1;
    q.push({x1, x2});

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        int moves[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};

        for (auto &mv : moves) {
            int nx = x + mv[0];
            int ny = y + mv[1];

            if (nx < 1 || nx > n || ny < 1 || ny > n)
                continue;

            if (a[nx][ny] == 1)
                continue;

            if (dist[x][y] + 1 < dist[nx][ny]) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }

    return dist[y1][y2];
}

int main() {
    ifstream fin("alee.in");
    ofstream fout("alee.out");

    int n, m;
    fin >> n >> m;

    vector<pair<int,int>> trees;
    trees.reserve(m);

    for (int i = 0; i < m; i++) {
        int x, y;
        fin >> x >> y;
        trees.push_back({x, y});
    }

    int x1, x2, y1, y2;
    fin >> x1 >> x2 >> y1 >> y2;

    int res = alee(n, trees, x1, x2, y1, y2);
    fout << res;

    return 0;
}
