// ask for a person's name, and generate a framed greeting
#include <iostream>
#include <string>

using namespace std;

int main()
{
    cout << "Please enter your first name: ";
    string name;
    cin >> name;
    // build the message that we intend to write
    const string greeting = "Hello, " + name + "!";
    
    // For more string initialization types - https://www.geeksforgeeks.org/c-string-class-and-its-applications/
    // build the second and fourth lines of the output
    const string spaced(greeting.size(), ' ');
    const string second = "* " + spaced + " *";
    // build the first and fifth lines of the output
    const string first(second.size(), '*');
    // write it all
    cout << endl;
    cout << first << endl;
    cout << second << endl;
    cout << "* " << greeting << " *" << endl;
    cout << second << endl;
    cout << first << endl;
    return 0;
}
