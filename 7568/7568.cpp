//20220303
#include<iostream>
using namespace std;
int main() {
	int N;
	cin >> N;
	int* x = new int[N];
	int* y = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> x[i];
		cin >> y[i];
	}
	int* score = new int[N];
	for (int z = 0; z < N; z++) {
		score[z] = 1;
	}
	for (int j = 0; j < N; j++) {
		for (int k = 0; k < N; k++) {
			if (k != j) {
				if (x[k] > x[j] && y[k] > y[j]) {
					score[j]++;
				}
			}
		}
	}
	for (int h = 0; h < N; h++) {
		cout << score[h] << " ";
	}
	
}