#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000000 + 5;
const int MAXM = 2000000 + 5;

int head[MAXN];
int nxt[MAXM];
int to[MAXM];
bool seen[MAXN];

// BFS multi-source separat
void bfs_multi_source(const vector<int> &sources) {
    queue<int> q;

    for (int s : sources) {
        if (!seen[s]) {
            seen[s] = true;
            q.push(s);
        }
    }

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int e = head[node]; e != -1; e = nxt[e]) {
            int nxtNode = to[e];
            if (!seen[nxtNode]) {
                seen[nxtNode] = true;
                q.push(nxtNode);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("berarii2.in", "r", stdin);
    freopen("berarii2.out", "w", stdout);

    int N, M, P;
    cin >> N >> M >> P;

    // initializam listele
    for (int i = 1; i <= N; i++)
        head[i] = -1;

    int edges = 0;

    // citim muchiile si construim graful invers
    for (int i = 0; i < M; i++) {
        int x, y;
        cin >> x >> y;
        to[edges] = x;
        nxt[edges] = head[y];
        head[y] = edges++;
    }

    vector<int> breweries(P);
    for (int i = 0; i < P; i++)
        cin >> breweries[i];

    // apelam BFS separat
    bfs_multi_source(breweries);

    // nodurile din care NU ajungi la berarii
    vector<int> result;
    result.reserve(N);

    for (int i = 1; i <= N; i++)
        if (!seen[i])
            result.push_back(i);

    cout << result.size() << "\n";
    for (int x : result)
        cout << x << "\n";

    return 0;
}
