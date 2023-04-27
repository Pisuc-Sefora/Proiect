
#include "../RepositoryFile/Repository.h"
#include "../Service/Service.h"

Service::Service(const Repository &repo) : repo(repo) {}

Service::~Service() {

}

void Service::addFriendshipCtrl(char *username, int id) {
    this->repo.addFriendship(username,id);
}

void Service::removeFriendshipCtrl(char* username) {
    this->repo.removeFriendship(username);
}

void Service::addNewUserCtrl(char *username, char *password) {
    this->repo.addNewUser(username,password);
}

void Service::removeUserCtrl(char *username) {
    this->repo.removeUser(username);

}

void Service::updateUserCtrl(char *password) {
    this->repo.updateUser(password);
}

void Service::sendMessageCtrl(char *text) {
    this->repo.sendMessage(text);

}

void Service::removeMessageCtrl(char *text) {
    this->repo.removeMessage(text);
}

void Service::selectFriendshipCtrl(char *username) {
    this->repo.selectFriendship(username);
}

bool Service::selectUserCtrl(char *username, char *password) {
    return this->repo.selectUser(username,password);
}

Dictionary<char *, char *> Service::getAllMessagesCtrl() {
    return this->repo.getAllMessages();
}

List<User> Service::getAllFriends() {
    return this->repo.getAllFriends();
}

List<User> Service::getAllUsers() {
    return this->repo.getAllUsers();
}
