#pragma once
#include <vector>
#include <algorithm>
#include "Friendship.h"

using namespace std;
template<typename T>
class List {
private:
    T *elems = new T[10];
    int size;
    int capacity;
public:
    List() {
        this->size = 0;
        this->capacity = 10;
    }

    void add(const T &elem) {
        if (this->size + 1 > this->capacity) {
            this->capacity = 2;
            T *new_elems = new T[this->capacity];
            for (int i = 0; i < this->size; i++)
                new_elems[i] = this->elems[i];
        }
        this->elems[this->size++] = elem;
    }

    void update(const T &elem, const T &new_elem) {
        for (int i = 0; i < this->size; i++)
            if (this->elems[i] == elem)
                this->elems[i] = new_elem;
    }

    void remove(T elem) {
        int pos = -1;
        for (int i = 0; i < this->size; i++)
            if (this->elems[i] == elem) pos = 1;
        if (pos != -1) {
            for (int i = pos; i < this->size - 1; i++)
                this->elems[i] = this->elems[i + 1];
            this->size--;
        }
    }

    int get_size() { return this->size; }

    T get_elem(int pos) { return this->elems[pos]; }

    T *getAll() { return elems; }

    ~List() {
        this->size = 0;
        this->capacity = 0;
    }
};