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

bool freq_compare(pair<int, int> p1, pair<int, int> p2) {
    // Check the frequency 
    // if frequency is same, check the values of pairs
    return(p1.second > p2.second || (p1.second == p2.second && p1.first < p2.first));
}

void sort_by_frequency(int arr[], int n) {
    unordered_map<int, int> hash;
    int i;

    // Creating frequency map in hash 
    for(i=0; i<n; i++) {
        if(hash.find(arr[i]) != hash.end())
            hash[arr[i]]++;
        else
            // hash.insert(make_pair(arr[i], 1));
            hash[arr[i]] = 1;
    }

    // For sorting the map - copy it to vector
    vector <pair<int, int>> freq;
    for(auto it=hash.begin(); it != hash.end(); it++)
        freq.push_back(make_pair(it->first, it->second));
    // sorting the new vector
    sort(freq.begin(), freq.end(), freq_compare);
    // Rearranging array elements
    int k=0;
    for(int i=0; i<freq.size(); i++) {
        for(int j=0; j<freq[i].second; j++)
            arr[k++] = freq[i].first;
    }
}