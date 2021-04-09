/* 
Basic utility funcitons in c
*/

// Check prime number
int is_prime(int n) {
    if(n == 1) return 0;
    if(n == 2) return 1;
    for (int i = 2; i*i <= n; i++)
        if (n%i == 0)
            return 0;
    return 1;
}

// swap two elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Reverse an array
void reverse(int arr[], int n) {
    for (int i = 0; i < n/2; i++)
        swap(&arr[i], &arr[n-i-1]);
}

int is_vowel(char c) {
    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u' || c=='A' || c=='E' || c=='I' || c=='O' || c=='U')
        return 1;
    else
        return 0;
}