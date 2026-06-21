// Problem: Sequence Game
// Contest: 2164 | Index: A
// URL: https://codeforces.com/contest/2164/problem/A
// Rating: 800 | Tags: brute force, sortings, *800
// Memory: 256 megabytes | Time: 1 second
// Author:

/**
 *    author: Yash Gupta
 *    created: 11.03.2026 22:54:43
 **/

#include <bits/stdc++.h>
#include <cstdio>

// --- For Debugging ---
#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif
// -------------------

using namespace std;

#define ll long long int
#define endl '\n'

// --- Type Definitions ---
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef pair<ll, ll> ii;
typedef vector<ii> vp;

// --- Shorthand Macros ---
#define all(v) v.begin(), v.end()
#define srt(v) sort(all(v))
#define pb push_back

// --- I/O Helper Functions ---
void vin(vi &a, ll n) {
  a.resize(n);
  for (ll i = 0; i < n; i++)
    cin >> a[i];
}

void pin(const vi &a) {
  for (size_t i = 0; i < a.size(); i++) {
    cout << a[i] << (i == a.size() - 1 ? "" : " ");
  }
  cout << endl;
}

// --- Main Solve Function ---
void solve() {
  ll n;
  cin >> n;
  vi v;
  vin(v, n);
  vi ans;
  ans.push_back(v[0]);
  for (int i = 1; i < n; i++) {
    if (v[i - 1] <= v[i]) {
      ans.push_back(v[i]);
    } else {
      ans.push_back(v[i]);
      ans.push_back(v[i]);
    }
  }
  cout << ans.size() << endl;
  pin(ans);
}

// --- Main Function ---
int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int t = 1;
  cin >> t;
  while (t--) {
    solve();
  }

  return 0;
}
