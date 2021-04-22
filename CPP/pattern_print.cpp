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

/* Print matrix in zigzag pattern :
Input:
1 2 3
4 5 6
7 8 9
10 11 12
Output :
1 2 4 7 5 3 6 8 10 11 9 12
*/
void matrix_zigzag(vector<vector<int>> mat, int n, int m) {
    vector<deque<int>> result(n+m-1);
    int i, j, sum;
    for(i=0; i<n; i++) {
        for(j=0; j<m; j++) {
            sum = i+j;
            if(sum%2==0) {
                result[sum].push_front(mat[i][j]);
            }
            else {
                result[sum].push_back(mat[i][j]);
            }
        }
    }
    for(i=0; i<n+m-1; i++) {
        for(j=0; j<result[i].size(); j++) {
            cout << result[i][j] << ' ';
        }
    }
}

/*
n=5
    *
   ***
  *****
   ***
    *
*/
void StarPyramid(int n) {
    int i, j;
    for(i=0; i<n; i++) {
        for(j=0; j<n-i-1; j++) {
            cout << ' ';
        }
        for(j=0; j<(i*2+1); j++) {
            cout << '*';
        }
        cout << endl;
    }
    for(i=n-1; i>0; i--) {
        for(j=0; j<=(n-i-1); j++) {
            cout << ' ';
        }
        for(j=0; j<(i*2-1); j++) {
            cout << '*';
        }
        cout << endl;
    }
}

int main() {
    int n, m, k=1;
    cin >> n >> m;
    // pyramid(n);
    // reverse_pattern(n);

    /* // Print matrix in zigzag pattern
    vector<vector<int>> mat(n, vector<int> (m));
    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            mat[i][j] = k++;
            cout << mat[i][j] << ' ';
        }
        cout << endl;
    }
    matrix_zigzag(mat, n, m); */
    StarPyramid(5);
}