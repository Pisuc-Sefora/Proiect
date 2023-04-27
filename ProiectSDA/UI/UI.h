#pragma once
#include "../Service/Service.h"

class UI {
private:
    Service service;
public:
    UI();
    UI(const Service &service);
    void startMenu();
    void userMenu();
    void friendshipMenu();
    void runApp();
    void showAllUsersUI();
    void addUserUI();
    void deleteUserUI();
    void loginUI();
    void showAllFriendsUI();
    void addFriendUI();
    void removeFriendUI();
    void selectFriendUI();
    void updatePasswordUI();
    void showAllMessagesUI();
    void sendMessageUI();
    void deleteMessageUI();
};


