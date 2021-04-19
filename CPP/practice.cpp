#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <math.h>
#include <string.h>
#include <fstream>

using namespace std;

vector<int> insertion_sort(vector<int> ar) {
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
    return ar;
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

class some_class {
    private:
        int id;
        int cl_id;
    public:
        char name[50];
        float mark;
        some_class() {
            id=0;
            cl_id = 0;
            strcpy(name,"h");
            mark = 0;
        }
        some_class(int id, int cl_id, float mark):id(id), cl_id(cl_id), mark(mark) {
            cout << "Enter name :";
            cin.getline(name, 50);
        }
        void get_data() {
            cout << id << ' ' << cl_id << ' ' << name << ' ' << mark << endl;
        }
};

void file_read() {
    ifstream fin;
    fin.open("new_text.txt", ios::in | ios::binary);
    some_class cls;
    while(fin.read((char *)&cls, sizeof(cls))) {
        // cout << line << " s" << endl;
        cout << "read\t";
        cls.get_data();
    }
    fin.close();
}

void file_write() {
    ofstream fout;
    string line;
    some_class cls1(1, 10, 94.32), cls2(3, 28, 38.3429);
    fout.open("new_text.txt", ios::out | ios::binary);
    cls1.get_data();
    cls2.get_data();
    // for(int i=0; i<5; i++) {
    //     getline(cin, line);
    //     fout << line << endl;
    // }
    fout.write((char *)&cls1, sizeof(cls1));
    fout.write((char *)&cls2, sizeof(cls2));
    fout.close();
}

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

int main() {
    // vector<int> arr;
    int arr[20];
    int n, input;
    cin >> n;

    // // Get the max value of unsigned int
    // // cout << UINT_MAX+1;

    // for(int i=0; i<n && cin >> input; i++) {
    //     // arr.push_back(input);
    //     arr[i] = input;
    // }
    // // arr = insertion_sort(arr);
    // // sort(arr, arr+n);
    // sort_by_frequency(arr, n);
    // cout << endl;
    // cout << *max_element(arr, arr+3);
    // cout << endl;
    // // for(auto it=arr.begin(); it != arr.end(); it++) {
    // //     cout << *it << ' ';
    // // }
    // for(int i=0; i< n; i++) 
    //     cout << arr[i] << ' ';
    
    /*// File read write
    file_write();
    file_read(); */

    // Print pyramid pattern
    pyramid(n);
}