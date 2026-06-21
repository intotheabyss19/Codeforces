#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define pb push_back
#define fastread() (ios_base::sync_with_stdio(false), cin.tie(NULL));

int main() {
  fastread();
  ll n;
  cin >> n;
  cout << (n % 4 == 0 || n % 4 == 3 ? 0 : 1);
}
