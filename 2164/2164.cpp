#include<iostream>
#include<queue>
using namespace std;

int main() {
	queue<int> q;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		q.push(i + 1);
	}
	while (!(q.size() == 1)) {
		q.pop();
		int temp = q.front();
		q.pop();
		q.push(temp);
	}
	cout << q.front();
}