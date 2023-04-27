#pragma once

#include "User.h"
#include <iostream>
#include "Dictionary.h"
#include <ctime>

using namespace std;

class Friendship {
private:
    int id;
    User one;
    User two;
    Dictionary<char*,char*> messages;
public:
    Friendship();
    Friendship(User, User, int);
    Friendship(User&, User&, int, Dictionary<char*,char*>);
    Friendship(const Friendship&);
    friend ostream& operator<<(ostream&, Friendship& );
    void addMessage(char*);
    void removeMessage(char*);
    Dictionary<char*,char*> getAllMessages();
    char* getAllMessagesStr();
    ~Friendship();
    int getId() const;
    User getOne();
    User getTwo();
    const Dictionary<char *, char *> &getMessages() const;
    void setId(int id);
    void setOne(const User &one);
    void setTwo(const User &two);
    void setMessages(const Dictionary<char *, char *> &messages);
    bool operator==(const Friendship&);

};
