
#include <sstream>
#include "Friendship.h"
#include "Dictionary.h"

Friendship::Friendship() {
    this->id= 0;
    this->one=User();
    this->two=User();
    this->messages= Dictionary<char*,char*>();

}

Friendship::Friendship(User one, User two, int id) {
    this->one = one;
    this->two = two;
    this->id = id;
    this->messages = Dictionary<char*,char*>();

}

ostream &operator<<(ostream &os, Friendship &f) {
    os << f.id << ',' << f.one << ','<<f.two<< '\n';
    return os;
}

void Friendship::addMessage( char *msg) {
    time_t ttime = time(0);

    char* dt = ctime(&ttime);

    this->messages.put(dt,msg);


}

void Friendship::removeMessage(char *tstmp) {
    this->messages.remove(tstmp);
}

Friendship::~Friendship() {
}

int Friendship::getId() const {
    return id;
}

User Friendship::getOne() {
    return one;
}

void Friendship::setId(int id) {
    Friendship::id = id;
}

void Friendship::setOne(const User &one) {
    Friendship::one = one;
}

void Friendship::setTwo(const User &two) {
    Friendship::two = two;
}

void Friendship::setMessages(const Dictionary<char *, char *> &messages) {
    Friendship::messages = messages;
}

User Friendship::getTwo(){
    return two;
}

const Dictionary<char *, char *> &Friendship::getMessages() const {
    return messages;
}

Friendship::Friendship(User &one, User &two, int id, Dictionary<char *, char *> dict) {
    this->one = one;
    this->two = two;
    this->id = id;
    this->messages = dict;
}

Dictionary<char *, char *> Friendship::getAllMessages() {
    return this->messages;
}

Friendship::Friendship(const Friendship & friendship) {
    this->id = friendship.id;
    this->one = friendship.one;
    this->two = friendship.two;
    this->messages = friendship.messages;
}

char *Friendship::getAllMessagesStr() {
    ostringstream os;
    os << this->one << "\n";
    char * msg_time, * msg_text;

    if (this->messages.get_size() != 0) {
        os << msg_time << ": " << msg_text << "\n";
        this->messages.getFirst();
        while (this->messages.valid()) {
            msg_time = this->messages.getCurrentKey();
            msg_text = this->messages.getCurrentValue();

            os << msg_time << ": " << msg_text << "\n";
            this->messages.getNext();
        }

        msg_time = this->messages.getCurrentKey();
        msg_text = this->messages.getCurrentValue();

        os << msg_time << ": " << msg_text << "\n";
    }
    return const_cast<char *>(os.str().c_str());
}

bool Friendship::operator==(const Friendship& f) {
    if (f.id == this->id)
        return true;
    return false;
}
