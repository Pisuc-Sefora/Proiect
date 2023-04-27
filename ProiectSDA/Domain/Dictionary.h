#pragma once
#include "Node.h"

template<class K, class V>
class Dictionary{
private:
    Node<K, V>* first;
    int size;
    Node<K,V>* iterator;
public:
    Dictionary(){
        this->first = nullptr;
        this->iterator = nullptr;
        size = 0;
    }
    void put(K key, V value){

        if(first == nullptr){
            first = new Node<K,V>(key, value);
            this->size++;
        }
        else {
            Node<K,V>* p = first;
            while (p->next != nullptr && p->key != key) {
                p = p->next;
            }
            if (p->key == key) p->value = value;
            else p->next = new Node<K,V>(key, value), this->size++;;
        }
        this->size++;
    }

    void remove(K key){

        if(first == nullptr){
            return;
        }
        else {
            Node<K,V>* p = first;
            while (p->next != nullptr && p->key != key) {
                p = p->next;
            }
            if (p->key == key)
            {
                delete p;
                this->size--;
            }

        }

    }

    V cauta(K key){
        Node<K,V>* p = first;
        while(p != nullptr){
            if(p->key == key) return p->value;
            p = p->next;
        }
        return {};
    }

    int get_size(){
        return this->size;
    }

    // Iterator functions
    void getFirst()
    {
        this->iterator = this->first;
    }

    void getNext(){
        this->iterator = this->iterator->next;
    }

    bool valid() const{
        return this->iterator->next != nullptr;
    }

    K getCurrentKey() const{
       return this->iterator->key;
    }

    V getCurrentValue() const{
        return this->iterator->value;
    }
};
