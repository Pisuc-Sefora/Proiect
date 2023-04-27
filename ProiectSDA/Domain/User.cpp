
#include "User.h"

#include <cstring>

#include <iostream>

using namespace std;

User::User() {
    this->nume = nullptr;
    this->password = nullptr;
}

User::User(const char* nume, const char* password){

    this->nume = new char[strlen(nume) + 1];
    strcpy_s(this->nume, strlen(nume) + 1, nume);
    this->password = new char[strlen(password) + 1];
    strcpy_s(this->password, strlen(password) + 1, password);


}

User::User(const User& utilizator){
    this->nume = new char[strlen(utilizator.nume) + 1];
    strcpy_s(this->nume,strlen(utilizator.nume) + 1, utilizator.nume);
    this->password = new char[strlen(utilizator.password) + 1];
    strcpy_s(this->password,strlen(utilizator.password) + 1, utilizator.password);
}

char *User::getNume() {
    return this->nume;
}

char *User::getPassword() {
    return this->password;
}


void User::setNume(const char *nume) {
    if (this->nume)
        delete[] this->nume;
    this->nume = new char[strlen(nume) + 1];
    strcpy_s(this->nume, strlen(nume) + 1, nume);
}
void User::setPassword(const char *) {
    if (this->password)
        delete[] this->password;
    this->password = new char[strlen(password) + 1];
    strcpy_s(this->password, strlen(password) + 1, password);
}


User &User::operator=(const User& utilizator) {
    if (this != &utilizator){
        if (this->nume and this->password){
            delete[] this->nume;
            delete[] this->password;
        }
    }
    this->nume = new char[strlen(utilizator.nume) + 1];
    strcpy_s(this->nume,strlen(utilizator.nume) + 1,utilizator.nume);
    this->password = new char[strlen(utilizator.password) + 1];
    strcpy_s(this->password,strlen(utilizator.password) + 1, utilizator.password);
    return *this;
}

bool User::operator==(const User& utilizator) {
    return strcmp(this->nume,utilizator.nume) == 0 && strcmp(this->password,utilizator.password) == 0;
}

bool User::operator!=(const User &utilizator) {
    return (strcmp(this->nume,utilizator.nume) != 0 || (strcmp(this->password,utilizator.password) != 0));
}

ostream& operator<<(ostream& os, User& utilizator){
    os << utilizator.nume << ',' << utilizator.password << '\n';
    return os;
}

User::~User() {
    if (this->nume){
        delete[] this->nume;
        delete[] this->password;
    }
}
