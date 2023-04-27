#pragma once
#include "../RepositoryFile/Repository.h"

class Service{
private:
    Repository repo;
public:
    ~Service();
    Service(){
        this->repo=Repository();
    }
    Service(const Repository &repo);
    void addFriendshipCtrl(char* username,int id);
    void removeFriendshipCtrl(char* username);
    void addNewUserCtrl(char*,char*);
    void removeUserCtrl(char*);
    void updateUserCtrl(char*);
    void sendMessageCtrl(char*);
    void removeMessageCtrl(char*);
    void selectFriendshipCtrl(char*);
    bool selectUserCtrl(char*,char*);
    List<User> getAllUsers();
    List<User> getAllFriends();
    Dictionary<char*,char*> getAllMessagesCtrl();
};