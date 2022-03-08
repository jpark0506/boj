//20220308 
//queue 자료구조를 이용해 작성
#include<iostream>
#include<queue>
using namespace std;
int main() {
	queue<int> q;
	int n, c;
	cin >> n >> c;
	for (int i = 1; i <=n; i++) {
		q.push(i);
	}
	cout << "<";
	int cnt = 0;
	while (!q.empty()) {
		int temp = 0;
		for (int i = 0; i < c-1; i++) {
			temp = q.front();
			q.pop();
			q.push(temp);
		}
		cnt++;
		if (cnt < n) {
			cout << q.front() << ", ";
		}
		else {
			cout << q.front();
		}
		q.pop();
	}
	cout << ">";

}