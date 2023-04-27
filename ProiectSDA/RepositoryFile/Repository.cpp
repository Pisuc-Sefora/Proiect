
#include "Repository.h"
#include<string.h>
#include<fstream>
#include<sstream>


using namespace std;

Repository::Repository() {
    this->friendships=List<Friendship>();
    this->users=List<User>();
    this->currentFriendship=Friendship();
    this->currentUser=User();

    read_users_csv();
}

List<User> Repository::getAllUsers() {
    return this->users;
}

List<User> Repository::getAllFriends() {
    List<User> friends=List<User>();
    for(int i=0;i<=this->friendships.get_size();i++)
    {
        if(this->friendships.get_elem(i).getOne()==this->currentUser)
            friends.add(this->friendships.get_elem(i).getTwo());
        if(this->friendships.get_elem(i).getTwo()==this->currentUser)
            friends.add(this->friendships.get_elem(i).getOne());
    }
    return friends;
}

void Repository::addFriendship(char* username,int id) {
    bool isFriend= false;
    for(int i=0;i<this->friendships.get_size();i++)
    {
        if(this->friendships.get_elem(i).getOne()==this->currentUser and this->friendships.get_elem(i).getTwo().getNume()==username)
            isFriend= true;
        if(this->friendships.get_elem(i).getTwo()==this->currentUser and this->friendships.get_elem(i).getOne().getNume()==username)
            isFriend=true;
    }
    if(isFriend==false)
    {
        this->friendships.add(Friendship(this->currentUser, getUserByUsername(username),id));
    }

}

void Repository::removeFriendship(char* username) {
    for(int i=0;i<this->friendships.get_size();i++){
        if((this->friendships.get_elem(i).getTwo().getNume(),username) == 0 && strcmp(this->friendships.get_elem(i).getOne().getNume(),this->currentUser.getNume()) == 0)
        {
            this->friendships.remove(this->friendships.get_elem(i));
        }
        if((this->friendships.get_elem(i).getOne().getNume(),username) == 0 && strcmp(this->friendships.get_elem(i).getTwo().getNume(),this->currentUser.getNume()) == 0)
        {
            this->friendships.remove(this->friendships.get_elem(i));
        }

    }
}

void Repository::addNewUser(char* username, char*password) {
    bool isUser=false;
    for(int i=0;i<this->users.get_size();i++)
    {
        if(strcmp(this->users.get_elem(i).getNume(),username) == 0)
            isUser=true;
    }
    if(isUser==false)
        this->users.add(User(username,password));
}

void Repository::removeUser(char* username) {
    for(int i=0;i<this->users.get_size();i++){
        if(strcmp(this->users.get_elem(i).getNume(),username) == 0)
            this->users.remove(this->users.get_elem(i));
    }
}

void Repository::updateUser(char* password) {
    this->currentUser.setPassword(password);
}

void Repository::sendMessage(char* text) {
    this->currentFriendship.addMessage(text);
}

void Repository::removeMessage(char* time) {
    this->currentFriendship.removeMessage(time);
}

void Repository::selectFriendship(char* username) {
    for(int i=0;i<=this->friendships.get_size();i++)
    {
        if(this->friendships.get_elem(i).getOne()==this->currentUser and this->friendships.get_elem(i).getTwo().getNume()==username)
            this->currentFriendship=this->friendships.get_elem(i);
        if(this->friendships.get_elem(i).getTwo()==this->currentUser and this->friendships.get_elem(i).getOne().getNume()==username)
            this->currentFriendship=this->friendships.get_elem(i);
    }
}

Dictionary<char*, char*> Repository::getAllMessages() {
    return this->currentFriendship.getAllMessages();
}

Repository::~Repository() {

}
User Repository::getUserByUsername(char * username) {
    for(int i=0;i<this->users.get_size();i++){
        if(strcmp(this->users.get_elem(i).getNume(),username) == 0)
            return this->users.get_elem(i);
    }
}

bool Repository::selectUser(char *username,char *password) {
    for(int i=0;i<this->users.get_size();i++){
        if(strcmp(this->users.get_elem(i).getNume(),username) == 0 and strcmp(this->users.get_elem(i).getPassword(),password) == 0)
            this->currentUser = this->users.get_elem(i);
        return true;
    }
    return false;
}
const User &Repository::getCurrentUser() const {
    return currentUser;
}

const Friendship &Repository::getCurrentFriendship() const {
    return currentFriendship;
}

void Repository::read_users_csv() {
    std::ifstream file("../users.csv");
    std::string line = "", word;
    vector<string> row;
    // Iterate through each line and split the content using delimeter
    while (getline(file, line))
    {
        row.clear();
        stringstream str(line);
        while(getline(str, word, ','))
            row.push_back(word);

        this->users.add(User(row[0].c_str(),row[1].c_str()));
    }
}
