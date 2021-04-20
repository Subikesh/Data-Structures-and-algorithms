#include <bits/stdc++.h>

using namespace std;

/*
for n=3
    1
  2 3 2
4 5 6 5 4
*/
void pyramid(int n) {
    int num = 1, i, j, temp;
    for(i=0; i<n; i++) {
        for(j=0; j<n-i-1; j++) cout << "  ";

        for(j=0; j<(2*i+1)/2; j++) {
            cout << num++ << ' ';
        }
        // cout << num << ' ';
        temp = num++;
        for(; j<(2*i+1); j++) {
            cout << temp-- << ' ';
        }
        cout << endl;
    }
}

/*
for n = 6
1	7	12	16	19	21
2	8	13	17	20
3	9	14	18	
4	10	15
5	11	
6 
*/
void reverse_pattern(int n) {
    int i, j, k = 1;
    int arr[n][n];
    for(i=0; i<n; i++) {
        for(j=0; j<n-i; j++) {
            arr[j][i] = k++;
        }
    }
    for(i=0; i<n; i++) {
        for(j=0; j<n-i; j++) {
            cout << arr[i][j] << ' ';
        }
        cout << endl;
    }
}

int main() {
    int n;
    cin >> n;
    // pyramid(n);
    reverse_pattern(n);
}