#include <iostream>
#include <string.h>


using namespace std;

struct temp {
    int len;
    char ch[1];
};
int main(int argc, char *args[]) {
    cout << "File name: " << args[0] << endl;
    if(argc == 1) {
        cout << "No extra arguments\n";
    }
    else {
        for(int i=1; i<argc; i++) {
            cout << args[i] << '\t';
        }        
    }
}