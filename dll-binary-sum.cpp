#include <iostream>
using namespace std;

class node{
    public:
    bool data;
    node* next;
    node* prev;
    node(bool data){
        this -> data = data;
        next = nullptr;
        prev = nullptr;
    }
};

class binary{
    node* head;
    node* tail;
    public:
        binary(){
            head = nullptr;
            tail = nullptr;
        }

        void addDigit(bool bit){
            node* newnode = new node(bit);
            if(head == nullptr){
                head = newnode;
                tail = newnode;
            }else{
                tail->next = newnode;
                newnode -> prev = tail;
                tail = newnode;
            }
        }

        void display(){
            node* temp = tail;
            while(temp != nullptr){
                cout << temp -> data;
                temp = temp-> prev;
            }
            cout << endl;
        }

        binary add(binary& other){
            binary result;
            node* ptr1 = tail;
            node* ptr2 = other.tail;
            bool carry = 0;

            while(ptr1 != nullptr || ptr2 != nullptr || carry){
                int bit1 = (ptr1 != nullptr) ? ptr1 -> data : 0;
                int bit2 = (ptr2 != nullptr) ? ptr2->data : 0;

                int sum = bit1 + bit2 + carry;
                result.addDigit(sum%2);
                carry = sum / 2;

                if(ptr1 != nullptr) ptr1 = ptr1->prev;
                if(ptr2 != nullptr) ptr2 = ptr2->prev;
            }

            return result;
        }

};

int main(){
    binary b1, b2;
    cout << "Enter first binary: ";
    string input1;
    cin >> input1;
    for(char ch: input1){
        b1.addDigit(ch - '0');
    }

    cout << "Enter second binary: ";
    string input2;
    cin >> input2;
    for(char ch: input2){
        b2.addDigit(ch - '0');
    }

    binary result = b1.add(b2);

    cout << "Sum: ";

}