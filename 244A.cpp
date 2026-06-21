#include <bits/stdc++.h>
using namespace std;

// Macros
#define ll long long
#define vi vector<int>
#define vvi vector<vector<int>>
#define vl vector<ll>
#define vvl vector<vector<ll>>
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pb push_back
#define F first
#define S second
#define all(x) (x).begin(), (x).end()
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define endl '\n'

// Pair I/O
template <typename T, typename U>
istream &operator>>(istream &in, pair<T, U> &p) {
  return in >> p.first >> p.second;
}
template <typename T, typename U>
ostream &operator<<(ostream &out, const pair<T, U> &p) {
  return out << p.first << ' ' << p.second;
}

// Vector I/O
template <typename T> istream &operator>>(istream &in, vector<T> &v) {
  for (auto &x : v)
    in >> x;
  return in;
}
template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  for (auto &x : v)
    out << x << ' ';
  return out;
}

// Constants
const int MOD = 1e9 + 7;
const ll INF = 1e18;

void solve() {
  ll n;
  cin >> n;
  vi v(n);
  cin >> v;
  ll sum = 0, count = 0;
  rep(i, 0, n) {
    sum = sum + v[i];
    if (sum < 0) {
      count++;
      sum = 0;
    }
  }
  cout << count << endl;
}

int main() {
  // Fast I/O
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int t = 1;
  // cin >> t; // Remove this line if there is only 1 test case
  while (t--) {
    solve();
  }

  return 0;
}
