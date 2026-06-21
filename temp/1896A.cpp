/**
 *    author: Yash Gupta
 *    created: 12.03.2026 20:09:36
 **/

#include <bits/stdc++.h>
#include <cstdio>

// --- Debugging ---
#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif

using namespace std;

// --- Core Types ---
#define ll long long int
#define ull unsigned long long
#define ld long double

// --- Container Typedefs (ll-based) ---
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef vector<int> vint;
typedef pair<ll, ll> ii;
typedef pair<int, int> pii;
typedef vector<ii> vp;

// --- Shorthand Macros ---
#define pb push_back
#define F first
#define S second
#define all(v) (v).begin(), (v).end()
#define srt(v) sort(all(v))
#define rsrt(v) sort((v).rbegin(), (v).rend())
#define rep(i, a, b) for (ll i = (a); i < (b); ++i)
#define per(i, a, b) for (ll i = (b) - 1; i >= (a); --i)
#define endl '\n'

// --- Constants ---
const ll INF = 1e18;
const int INF32 = 1e9;
const int MOD = 1e9 + 7;

// --- Pair I/O ---
template <typename T, typename U>
istream &operator>>(istream &in, pair<T, U> &p) {
  return in >> p.first >> p.second;
}
template <typename T, typename U>
ostream &operator<<(ostream &out, const pair<T, U> &p) {
  return out << p.first << ' ' << p.second;
}

// --- Vector I/O ---
template <typename T> istream &operator>>(istream &in, vector<T> &v) {
  for (auto &x : v)
    in >> x;
  return in;
}
template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  for (size_t i = 0; i < v.size(); i++)
    out << v[i] << (i + 1 < v.size() ? ' ' : '\n');
  return out;
}

// --- I/O Helpers (safe, explicit) ---
void vin(vi &a, ll n) {
  a.resize(n);
  for (ll i = 0; i < n; i++)
    cin >> a[i];
}
void pin(const vi &a) {
  for (size_t i = 0; i < a.size(); i++)
    cout << a[i] << (i + 1 < a.size() ? ' ' : '\n');
}
void vin2(vvi &g, ll n, ll m) {
  g.assign(n, vi(m));
  rep(i, 0, n) rep(j, 0, m) cin >> g[i][j];
}

// --- Utility Templates ---
template <typename T> bool chmin(T &a, T b) {
  return b < a ? (a = b, true) : false;
}
template <typename T> bool chmax(T &a, T b) {
  return b > a ? (a = b, true) : false;
}

// --- Solve ---
void solve() {
  int n;
  cin >> n;
  vi v;
  vin(v, n);
  if (v[0] != 1) {
    cout << "NO" << endl;
    return;
  }
  cout << "YES" << endl;
}

// --- Main ---
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int t = 1;
  cin >> t; // remove if single test case
  while (t--)
    solve();

  return 0;
}
