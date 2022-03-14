#include<iostream>
#include<stack>
using namespace std;
int main() {
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		stack<int> st;
		string s;
		bool flag = false;
		cin >> s;
		for (int j = 0; j < s.size(); j++) {
			if (s[j]=='(') {
				st.push(0);
			}
			else{
				if (!st.empty()) {
					st.pop();
				}
				else {
					flag = true;
					break;
				}
			}
		}
		if (!st.empty() || flag) {
			cout << "NO" << "\n";
		}
		else {
			cout << "YES" << "\n";
		}
	}
}