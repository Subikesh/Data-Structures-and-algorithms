#include<stdio.h>
#include "utilities.c"

int main() {
    // int n=10;
    // printf("Enter your number: ");
    // scanf("%d", &n);
    // printf((is_prime(n))?"True": "False");


    // int ar[10] = {[0 ... 1]=-1, [3]=10, [5]=20};
    // int n=sizeof(ar)/sizeof(int);
    int ar[10], n, i, j;
    scanf("%d", &n);
    // Get array input
    for (i = 0; i < n; i++)
        scanf("%d", &ar[i]);
    // print array elements
    for (i = 0; i < n; i++)
        printf("%d ", ar[i]);
    
    // Size allocation chart
    // printf("int: %d\nfloat: %d\ndouble: %d", sizeof(int), sizeof(float), sizeof(double));
    // printf("us int: %d\nshort int: %d\ndouble: %d", sizeof(unsigned int), sizeof(short int), sizeof(double));
    reverse(ar, n);
    printf("After : \n");
    for (i = 0; i < n; i++)
        printf("%d ", ar[i]);
}
