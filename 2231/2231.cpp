//20220303
#include<iostream>
#include<math.h>
#include<string>
//각 자리수 파악을 위해 string으로 바꾸기
using namespace std;
int main() {
	int input;
	cin >> input;
	int count = 1;
	int divsum = 0;
	while (divsum == 0) {
		
		int temp = 0;
		string str1 = to_string(count);
		for (int i = 0; i < str1.length(); i++) {
			temp = temp + str1[i] - '0';
		}
		
		temp = temp + count;

		if (temp == input) {
			divsum = count;
			break;
		}
		if (count > input) {
			count = 0;
			break;
		}
		count++;
	}
	cout << count;
}