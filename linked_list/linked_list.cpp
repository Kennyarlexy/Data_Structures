//wanna learn? start from the python file
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* next_node;

    //everytime you create a custom constructor, you need to explicitly create the default one, otherwise when a function wants to copy the an object argument to it's local variable, it can't.
    Node() {}
    
    Node(int data) {
        this->data = data;
        this->next_node = nullptr;
    }
};

ostream& operator << (ostream& output, Node node) {
    output << "<node data: " << node.data << ">";

    return output;
}

struct LinkedList {
    Node* head;

    //overload default constructor
    LinkedList() {
        this->head = nullptr;
    }

    bool isEmpty() {
        return this->head == nullptr;
    }

    void add(int data) {
        /*
        if you create a Node object for new_node (instead of pointer) which will be destroyed outside of this function, then when you access this new head pointer the next time, the address it points to no longer exists.
        */
        Node* new_node = new Node(data);
        new_node->next_node = this->head;
        this->head = new_node;
    }

    int size() {
        Node* current = this->head;
        int size = 0;
        while (current != nullptr) {
            size++;
            current = current->next_node;
        }

        return size;
    }

    bool search(int target) {
        Node* current = this->head;
        while (current != nullptr) {
            if (current->data == target) {
                return true;
            } else {
                current = current->next_node;
            }
        }

        return false;
    }

    void insert(int target_position, int data) {
        if (target_position == 0) {
            this->add(data);
        } else {
            Node* current_node = this->head;
            int current_position = 0;
            while (current_position < target_position - 1) {
                current_node = current_node->next_node;
                current_position++;
                if (current_node == nullptr) {
                    cout << "Index out of range!\n";
                    return;
                }
            }

            Node* new_node = new Node(data);
            new_node->next_node = current_node->next_node;
            current_node->next_node = new_node;
        }
    }

    Node* removeData(int data) {
        Node* current = this->head;
        Node* prev_node = nullptr;

        while (current != nullptr) {
            if (current->data == data) {
                if (current == this->head) {
                    this->head = current->next_node;
                } else {
                    prev_node->next_node = current->next_node;
                }
                return current;
            }
            prev_node = current;
            current = current->next_node;
        }
        
        return nullptr;
    }
};

ostream& operator << (ostream& output, const LinkedList& list) {
    Node* current = list.head;
    while (current != nullptr) {
        if (current == list.head) {
            output << "[Head: " << current->data << "] -> ";
        } else if (current->next_node == nullptr) {
            output << "[Tail: " << current->data << "]";
        } else {
            output << "[" << current->data << "] -> ";
        }
        current = current->next_node;
    }

    return output;
}


int main() {
    LinkedList list_A;
    list_A.add(10);
    list_A.add(20);
    list_A.add(30);
    list_A.add(40);
    list_A.add(50);
    cout << "Size: " << list_A.size() << endl;
    cout << list_A << "\n\n";
    int target;
    cout << "Enter target: "; cin >> target;
    if (list_A.search(target)) {
        cout << "Found " << target << "!\n\n";
    } else {
        cout << target << " not found!\n\n";
    }

    //insert() demo
    cout << "Inserting 222 to index 2\n";
    list_A.insert(2, 222);
    cout << list_A << "\n\n";

    cout << "Inserting 777 to index 7 <-- won't work\n";
    list_A.insert(7, 777);
    cout << list_A << "\n\n";

    //removeData() demo
    Node* removed = list_A.removeData(222);
    cout << "Removing ";
    if (removed == nullptr) {
        cout << "none\n";
    } else {
        cout << *removed << "\n";
    }
    cout << list_A << "\n";

    return 0;
}