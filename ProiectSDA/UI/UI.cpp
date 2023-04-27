
#include <cstring>
#include "UI.h"
#include "iostream"

UI::UI() {
    this->service=Service();

}

void UI::startMenu() {
    cout<<"Menu"<<endl;
    cout<<"1.Show all users"<<endl;
    cout<<"2.Add user"<<endl;
    cout<<"3.Delete user"<<endl;
    cout<<"4.Login"<<endl;
    cout<<"0.Exit"<<endl;
}

void UI::userMenu() {
    cout<<"Menu"<<endl;
    cout<<"1.Show all users"<<endl;
    cout<<"2.Show all friends"<<endl;
    cout<<"3.Add friend"<<endl;
    cout<<"4.Remove friend"<<endl;
    cout<<"5.Select friend"<<endl;
    cout<<"6.Update password"<<endl;
    cout<<"0.Exit"<<endl;
}

void UI::friendshipMenu() {
    cout<<"Menu"<<endl;
    cout<<"1.Show all messages"<<endl;
    cout<<"2.Send message"<<endl;
    cout<<"3.Delete message"<<endl;
    cout<<"0.Exit"<<endl;
}

void UI::runApp() {
    cout<<"Hello 2 ";
    startMenu();
    int opt;
    cout<<"Give option number: "<<endl;
    cin >> opt;
    while (opt) {
        switch (opt) {
            case 1: {
                showAllUsersUI();
                break;
            }
            case 2: {
                addUserUI();
                break;
            }
            case 3: {
                deleteUserUI();
                break;
            }
            case 4: {
                loginUI();
                break;
            }
            default:
                cout << "Wrong option! Try again!" << endl;
        }
        startMenu();
        cout << "Give option number: " << endl;
        cin >> opt;

    }
}

void UI::showAllUsersUI() {
    List<User> u;
    u=this->service.getAllUsers();
    for(int i=0;i<u.get_size();i++)
        cout<<"Username: "<<u.get_elem(i).getNume()<<endl;
}

void UI::addUserUI() {
    char* username = new char[20];
    char *password = new char[20];
    cout<<"Username: ";
    cin>>username;
    cout<<"Password: ";
    cin>>password;
    this->service.addNewUserCtrl(username,password);
}

void UI::deleteUserUI() {
    char*username = new char[20];
    cout<<"Username: ";
    cin>>username;
    this->service.removeUserCtrl(username);
}

void UI::loginUI() {
    char* username = new char[20];
    char* password = new char[20];
    cout<<"Username: ";
    cin>>username;
    cout<<"Password: ";
    cin>>password;
    bool login = false;
    login = this->service.selectUserCtrl(username,password);
    if(login==false){
        cout<<"Login failed"<<endl;
    }
    else{
        userMenu();
        int opt;
        cout<<"Give option number: "<<endl;
        cin >> opt;
        while (opt) {
            switch (opt) {
                case 1: {
                    showAllUsersUI();
                    break;
                }
                case 2: {
                    showAllFriendsUI();
                    break;
                }
                case 3: {
                    addFriendUI();
                    break;
                }
                case 4: {
                    removeFriendUI();
                    break;
                }
                case 5: {
                    selectFriendUI();
                    break;
                }
                case 6: {
                    updatePasswordUI();
                    break;
                }
                default:
                    cout << "Wrong option! Try again!" << endl;
            }
            userMenu();
            cout << "Give option number: " << endl;
            cin >> opt;

        }
    }
}

void UI::showAllFriendsUI() {
    List<User> u;
    u = this->service.getAllFriends();
    for(int i=0;i<u.get_size();i++)
        cout<<"Username: "<<u.get_elem(i).getNume()<<endl;
}

void UI::addFriendUI() {
    int id;
    char* username = new char[20];
    cout<<"ID: ";
    cin>>id;
    cout<<"Add friend: ";
    cin>>username;
    this->service.addFriendshipCtrl(username,id);
}

void UI::removeFriendUI() {
    char*username = new char[20];
    cout<<"Username: ";
    cin>>username;
    this->service.removeFriendshipCtrl(username);
}

void UI::selectFriendUI() {
    char*username = new char[20];
    cout<<"Give the username of the friend you want to select ";
    cin>>username;
    this->service.selectFriendshipCtrl(username);
    friendshipMenu();
    int opt;
    cout<<"Give option number: "<<endl;
    cin >> opt;
    while (opt) {
        switch (opt) {
            case 1: {
                showAllMessagesUI();
                break;
            }
            case 2: {
                sendMessageUI();
                break;
            }
            case 3: {
                deleteMessageUI();
                break;
            }
            default:
                cout << "Wrong option! Try again!" << endl;
        }
        friendshipMenu();
        cout << "Give option number: " << endl;
        cin >> opt;

    }
}

void UI::updatePasswordUI() {
    char *password;
    cout<<"give new password ";
    cin>>password;
    this->service.updateUserCtrl(password);
}

void UI::showAllMessagesUI() {
    Dictionary<char*,char*> u;
    u = this->service.getAllMessagesCtrl();
    int i = 0;
    int len = u.get_size();
    if (len != 0) {

        u.getFirst();
        while (i!=len) {
            cout<<"Time: "<<u.getCurrentKey()<<" Message: "<<string(u.getCurrentValue())<<endl;
            u.getNext();
            i++;
        }
    }
}

void UI::sendMessageUI() {
    string message;
    cout<<"Enter message: ";

//    cin.ignore();
//    std::getline(std::cin,message);
//    char msg[message.length() + 1];
    cin >> message;
//    strcpy(msg,message.c_str());
//    cout << &message[0]<<endl;
//    char * val = &msg[0];
    char* messageChar = const_cast<char*>(message.c_str());
    cout << messageChar;
    this->service.sendMessageCtrl(messageChar);
}

void UI::deleteMessageUI() {
    char *time;
    cout<<"Enter time: ";

    cin.ignore();
    cin.getline(time,256);
    this->service.removeMessageCtrl(time);
}

UI::UI(const Service &service) : service(service) {}


