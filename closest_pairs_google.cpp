''' https : //discuss.codechef.com/t/google-online-coding-challenge-internship-2021-cutoff-score-how-many-question-req/75163
'''

/* Closest pair problem solution Google*/

#include <bits/stdc++.h>
using namespace std;

int n;
vector g[10000 + 5];
int val[10000 + 5];
int vis[10000 + 5] = {0};
int ans[10000 + 5] = {100};
vector inside;

void dfs(int v, vector &inside)
{
    vis[v] = 1;
    int in = inside.size();
    int flag = 1;
    for (int i = in - 1; i >= 0; i--)
    {
        if (__gcd(val[v], val[inside[i]]) == 1)
        {
            ans[v] = inside[i];
            flag = 0;
            break;
        }
    }
    if (flag)
    {
        ans[v] = -1;
    }
    inside.push_back(v);
    for (int i = 0; i < g[v].size(); i++)
    {
        if (vis[g[v][i]] == 0)
            dfs(g[v][i], inside);
    }
    inside.pop_back();
}

int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        int x;
        cin >> x;
        val[i] = x;
    }
    for (int i = 1; i <= n - 1; i++)
    {
        int x, y;
        cin >> x >> y;
        g[x].push_back(y);
        g[y].push_back(x);
    }
    dfs(1, inside);
    for (int i = 1; i <= n; i++)
    {
        cout << ans[i] << " ";
    }
    cout << endl;
}