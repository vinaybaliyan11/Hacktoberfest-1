// Reverse a linked list

#include<bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node* next;
    Node(int data) {
        this->data = data;
        next = NULL;
    }
};

struct LinkedList{
    Node* head;
    LinkedList() {
        head = NULL;
    }

    void reverse() {
        Node* current = head;
        Node *prev = NULL, *next = NULL;

        while(current != NULL) {
            next = current->next;
            current->next = prev;

            prev = current;
            current = next;
        }
        head = prev;
    }

    void printList() {
        struct Node* temp = head;
        while(temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
    }

    void push(int data) {
        Node* temp = new Node(data);
        temp->next = head;
        head = temp;
    }
};

int main() {
    LinkedList l;

    l.push(1561);
    l.push(1694);
    l.push(1998);
    l.push(2029);
    l.push(2157);
    l.push(2211);
    l.push(2268);

    cout << "Given Linked List:\n";
    l.printList();

    l.reverse();

    cout << "\nReverse Linked List:\n";
    l.printList();

    return 0;
}

