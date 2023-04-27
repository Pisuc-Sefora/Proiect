#pragma once

#include "../Domain/List.h"
#include "../Domain/Friendship.h"
#include "../Domain/User.h"
#include "../Domain/Dictionary.h"

using namespace std;

class Repository{
private:
    List<User> users;
    List<Friendship> friendships;
    User currentUser;
    Friendship currentFriendship;
public:
    Repository();
    List<User> getAllUsers();
    List<User> getAllFriends();
    void addFriendship(char* username,int id);
    void removeFriendship(char* username);
    void addNewUser(char*,char*);
    void removeUser(char*);
    void updateUser(char*);
    void sendMessage(char*);
    void removeMessage(char*);
    void selectFriendship(char*);
    bool selectUser(char*,char*);
    User getUserByUsername(char*);
    Dictionary<char*,char*> getAllMessages();
    ~Repository();
    const User &getCurrentUser() const;
    const Friendship &getCurrentFriendship() const;
    void read_users_csv();

};