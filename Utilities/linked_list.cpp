#include <bits/stdc++.h>

using namespace std;

// Contains data for a single node in linked list
class Node {
    public: 
    int data;
    Node *next;
    Node() {
        data = 0;
        next = NULL;
    }
    Node(int n) {
        data = n;
        next = NULL;
    }
};

// Linked list implementation class
class SinglyLinkedList {
    public:
    Node *head;
    int size;

    SinglyLinkedList() {
        size = 0;
        head = NULL;
    }
    SinglyLinkedList(int data) {
        size = 1;
        head = new Node(data);
    }
    SinglyLinkedList(Node *node) {
        size = 1;
        head = node;
    }
    
    // Insert a data at end
    void PushBack(int data) {
        Node *newNode = new Node(data);
        if(head == NULL) {
            head = newNode;
        }
        else {
            Node *temp = head;
            while(temp->next != NULL) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
        size++;
    }

    // Add a new node to the front of the list
    void PushFront(int data) {
        Node *newNode = new Node(data);
        newNode->next = head;
        head = newNode;
        size++;
    }

    // Pop the last node
    int PopLast() {
        Node *temp = head;
        Node *delNode;
        int deleted;
        while(temp->next->next != NULL) {
            temp = temp->next;
        }
        delNode = temp->next;
        temp->next = NULL;
        deleted = delNode->data;
        // free memory
        delete delNode;
        size--;
        return deleted;
    }

    // Pop node at index - index is 0 based
    int PopAt(int index) {
        if(index >= size) {
            return;
        }
        Node *temp = head;
        Node *delNode;
        int deleted;
        for(int i=0; i<index; i++) {
            temp = temp->next;
        }
        delNode = temp->next;
        temp->next = temp->next->next;
        deleted = delNode->data;
        delete delNode;
        size--;
        return deleted;
    }

    // Print the linked list
    void PrintList() {
        Node *temp = head;
        while(temp != NULL) {
            cout << temp->data << ' ';
            temp = temp->next;
        }
        cout << endl;
    }
};

int main() {
    int n, data;
    cin >> n;
    SinglyLinkedList list;
    for(int i=0; i<n; i++) {
        cin >> data;
        list.PushBack(data);
    }
    list.PrintList();
    list.PushFront(-3);
    cout << list.PopLast() << endl;
    list.PrintList();
}