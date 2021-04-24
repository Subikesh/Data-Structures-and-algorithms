#include <iostream>
#include <conio.h>
#include <fstream>
#include <string.h>
#define USER_FILE "users.bin"
#define ENTER           13
#define BACKSPACE        8

using namespace std;

class User {
    private:
    char *password;
    bool loggedIn;

    public:
    char *username;
    char *fullname;
    int age;

    User() {
        username = (char *)malloc(sizeof(20));
        password = (char *)malloc(sizeof(20));
        fullname = (char *)malloc(sizeof(50));
        age = 0;
        loggedIn = false;
    }

    // User(User obj) {
    //     strcpy(username, obj.username);
    //     strcpy(fullname, obj.fullname);
    //     age = obj.age;
    //     loggedIn = false;
    // }
	char *GetPassword() {
		return password;
	}

    void InputPassword(char *password) {
        int pos = 0;
        char ch;
        while(true)
        { 
            ch=getch();
            if(ch==ENTER) break;  /* User have pressed ENTER*/
            
            else if(ch==BACKSPACE)  /* BACKSPACE was pressed*/
                {
                cout <<"\b \b";   
                password[--pos]='\0';
                }
            else/* A..Z a...z  BUG: I forgot what... */
                {
                cout <<"*";
                password[pos++]=ch;
                password[pos]='\0';
                }
            if(pos<=0) pos=0;
        }
        cout << endl;
    }
	
    bool FindUser(char *username, char *password) {
        User user;
        ifstream fin;
        fin.open(USER_FILE, ios::in | ios::binary);
        if(!fin) {
            return false;
        }
        else {
            while(fin.read((char *)&user, sizeof(user))) {
                if(strcmp(user.username, username)==0 && strcmp(user.GetPassword(), password)==0) {
                    age = user.age;
                    fullname = user.fullname;
                    return true;
                }
            }
            fin.close();
        }
        return false;
    }

    bool IsLoggedIn() {
        return loggedIn;
    }

    void SignUp() {
        char ch;
        char retype[20];
        User user;
        cout << "Enter username: ";
        cin >> username;
        cout << "Enter full name: ";
        cin.ignore();
        cin.getline(fullname, 50);
        cout << "Enter Age: ";
        cin >> age;
        cout << "Password: ";
        InputPassword(password);
        cout << "Retype password: ";
        // while((ch=getch())!= '\n') {
        //     retype += ch;
        //     cout <<'*';
        // }
        // retype += '\0';
        InputPassword(retype);
        if(strcmp(password, retype)==0) {
            if(FindUser(username, password)) {
                cout << "User already found! User logged in." << endl;
            }
            else {
                ofstream fout;
                fout.open(USER_FILE, ios::app|ios::binary);
                fout.write((char*)this, sizeof(this));
                fout.close();
            }
            loggedIn = true;
        }
        else {
            cout << "Entered passwords dont match." << endl;
        }
    }

    void LoginUser()   {
        char ch;
//        password = (char *)malloc(20);
        cout << "Enter username: ";
        cin >> username;
        cout << "Password: ";
        while((ch=getch())!= '\n') {
            password += ch;
            cout <<'*';
        }
        password += '\0';
        if(FindUser(username, password)) {
            loggedIn = true;
            cout << "User logged in!" << endl;
        }
        else {
            cout << "No users found in database! Try signing up."<< endl;
        }
    }

    void LogoutUser() {
        // username = "";
        // password = "";
        age = 0;
        // fullname = "";
        loggedIn = false;
        cout << "User Logged out";
    }
    void ViewDetails() {
        if(loggedIn) {
            cout << endl << username << ' ' << age << ' ' << fullname << endl;
        }
        else 
            cout << "User not logged in!" << endl;
    }
};

int main() {
    User newUser;
    
    newUser.SignUp();
    // newUser.LogoutUser();
    // // newUser.SignUp();
    // newUser.LoginUser();
    newUser.ViewDetails();
    return 0;
}
