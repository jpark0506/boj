#include<iostream>
#include<stack>
#include<string>
using namespace std;
int main() {
	string s;
	while (true){
		getline(cin, s, '.');
		if (s == "") { 
			break; 
		}
		stack<int> st;
		bool flag = false;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '(') {
				st.push(0);
			}
			else if (s[i] == '[') {
				st.push(1);
			}
			else if (s[i] == ')') {
				
				if (!st.empty()) {
					if (st.top() == 1) {
						flag = true;
						break;
					}
					st.pop();
					
				}
				else {
					flag = true;
					break;
				}
			}
			else if (s[i] == ']') {
				
				if (!st.empty()) {
					if (st.top() == 0) {
						flag = true;
						break;
					}
					st.pop();
				}
				else {
					flag = true;
					break;
				}
			}
		}
		cin.ignore();
		if (flag == true || !st.empty()) {
			cout << "no" << "\n";
		}
		else {
			cout << "yes" << "\n";
		}
	}
}