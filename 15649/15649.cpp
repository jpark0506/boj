#include<iostream>
#include<vector>
using namespace std;
int n, m;
bool visited[9];
vector<int> result;
void DFS() {
	if (result.size()==m) {
		for (int num : result) {
			cout << num << " ";
		}
		cout << "\n";
	}
	for (int i = 1; i <=n; i++) {
		if (!visited[i]) {
			visited[i] = true;
			result.push_back(i);
			DFS();
			result.pop_back();
			visited[i] = false;
		}
	}
}
int main() {
	cin >> n >> m;
	//n진수에서 m자리 수를 순서대로 출력
	//순열 출력
	DFS();
}