#include<iostream>
#include<string>
using namespace std;
int main() {
	int N;
	cin >> N;
	int min = 665;
	int cnt = 0;
	while(cnt!=N){
		min++;
		string str_min = to_string(min);
		for (int i = str_min.length() - 1; i > 1; i--) {
			if (str_min[i] == str_min[i - 1] && str_min[i - 1] == str_min[i - 2]) {
				if (str_min[i] == '6') {
					cnt++;
					break;
				}
			}
		}
	}
	cout <<min;
}