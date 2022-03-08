#include<iostream>
using namespace std;
class Node {
public:
	int elem;
	Node* next;
};
class SL {
public:
	Node* head;
	Node* tail;
	int size;
	SL(int N) {
		size = N;
		for (int i = 1; i < N + 1; i++) {
			Node* v = new Node;
			if (i == 1) {
				head = v;
				tail = v;
			}
			v->elem = i;
			tail->next = v;
			tail = v;
		}
		tail->next = head;
	}
	void removeby(int K, int N) {
		Node* curr = head;
		Node* prev = tail;
		if (size == 1) {
			cout << "<1>";
		}
		else {
			while (size != 0) {
				for (int i = 0; i < K - 1; i++) {
					curr = curr->next;
					prev = prev->next;
				}
				Node* temp = curr;
				prev->next = curr->next;
				curr = curr->next;
				if (size == N) {
					cout << "<" << temp->elem << ", ";
				}
				else if (size == 1) {
					cout << temp->elem;
				}
				else {
					cout << temp->elem << ", ";
				}
				delete temp;
				size--;
			}
			cout << ">";
		}
	}
};
int main() {
	int n, m;
	cin >> n >> m;
	SL sl(n);
	sl.removeby(m, n);
}