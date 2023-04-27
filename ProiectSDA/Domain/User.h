#pragma once

#include <iostream>
using namespace std;

class User {
private:
    char* nume;
    char* password;
public:
    User();
    User(const char*, const char* );
    User(const User&);
    char* getNume();
    char* getPassword();
    void setNume(const char*);
    void setPassword(const char*);
    User& operator=(const User&);
    bool operator==(const User&);
    bool operator!=(const User&);
    friend ostream& operator<<(ostream&, User& );
    ~User();

};

