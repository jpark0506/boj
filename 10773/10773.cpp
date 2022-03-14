#include<iostream>
#include<stack>
using namespace std;
int main() {
	int n;
	cin >> n;
	stack<int> s;
	for (int i = 0; i < n; i++) {
		int ex;
		cin >> ex;
		if (ex == 0) {
			s.pop();
		}
		else {
			s.push(ex);
		}
		
	}
	int sum = 0;
	while (!s.empty()) {
		sum = sum + s.top();
		s.pop();
	}
	cout << sum;
}