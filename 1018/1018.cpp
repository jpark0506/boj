//20220305
#include<iostream>
using namespace std;
//W=-1, B=1
int main() {
	int m, n;
	cin >> m >> n;

	//�����迭 ���� �Ҵ�
	//���� m�� �迭�ε� for�� ���ʿ� i<n�̶�� �����Ͽ� pointer�� null�� ������ Ʋ���� ��
	int** input = new int* [m];
	for (int i = 0; i < m; i++) {
		input[i] = new int[n];
	}
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			input[i][j] = 0;
		}
	}
	for (int i = 0; i < m; i++) {
		string A;
		cin >> A;
		for (int z = 0; z < n; z++) {
			if (A[z] == 'W') {
				input[i][z] = -1;
			}
			else if (A[z] == 'B') {
				input[i][z] = 1;
			}
		}
		
	}
	//���� ü���� ����
	int** ex1 = new int* [8];
	for (int i = 0; i < 8; i++) {
		ex1[i] = new int[8];
	}
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			ex1[i][j] = 0;
		}
	}
	int** ex2 = new int* [8];
	for (int i = 0; i < 8; i++) {
		ex2[i] = new int[8];
	}
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			ex2[i][j] = 0;
		}
	}
	//2���� ����� ���� ����
	int outer_flag = 1;
	for (int j = 0; j < 8; j++) {
		int inner_flag = outer_flag;
		for (int k = 0; k < 8; k++) {
			ex1[j][k] = inner_flag;
			ex2[j][k] = -inner_flag;
			inner_flag = -inner_flag;
		}
		outer_flag = -outer_flag;
	}


	int cases = (n - 7) * (m - 7) * 2;
	int cnt = 0;
	int* diff = new int[cases];
	for (int i = 0; i < cases; i++) {
		diff[i] = 0;
	}
	//��� ����� ���� �˻�
	//���⼭ ���� �ݺ��� 2���� i++, j++�� �Ἥ ���
	for (int i = 0; i < m-7; i++) {
		for (int j = 0; j < n - 7; j++) {
			for (int k = i; k < i + 8; k++) {
				for (int z = j; z < j + 8; z++) {
					if (ex1[k-i][z-j] != input[k][z]) {
						diff[cnt]++;
					}
					if (ex2[k-i][z-j] != input[k][z]) {
						diff[cnt + 1]++;
					}
				}
			}
			cnt=cnt+2;
		}

	}
	int min = diff[0];
	for (int i = 1; i < cases; i++) {
		if (diff[i] < min) {
			min = diff[i];
		}
	}
	cout << min;

	
}