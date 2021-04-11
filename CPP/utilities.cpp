/* 
    Basic Utility functions in c++
*/

#include <iostream>
#include <vector>

int is_prime(int n) {
    if(n == 1) return 0;
    if(n == 2) return 1;
    for (int i = 2; i*i <= n; i++)
        if (n%i == 0)
            return 0;
    return 1;
}

// swap two elements
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Reverse an array
void reverse(int arr[], int n) {
    for (int i = 0; i < n/2; i++)
        swap(arr[i], arr[n-i-1]);
}

int is_vowel(char c) {
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' || c=='U')
        return 1;
    else
        return 0;
}

void insertion_sort(vector<int> &ar) {
    int i, j, hole, curr;
    for(i=0; i<ar.size(); i++) {
        if(i == 0) continue;
        hole = i;
        curr = ar[hole];
        for(j=i-1; j>=0 && ar[j] >= curr; j--) {
            ar[j+1] = ar[j];
        }
        ar[j+1] = curr;
    }
}
