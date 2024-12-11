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

class complement{
    node* head;
    node* tail;
    public:
        complement(){
            head = nullptr;
            tail = nullptr; 
        }

        void convertTobinary(int num){
            if(num == 0){
                addDigit(0);
                return;
            }
            while(num > 0){
                addDigit(num % 2);
                num /= 2;
            }
        }

        void addDigit(bool bit){
            node* newnode = new node(bit);
            if(head == nullptr){
                head = newnode;
                tail = newnode;
            }else{
                tail -> next = newnode;
                newnode -> prev = tail;
                tail = newnode;
            }
        }

        void display(){
            node* temp = head;
            while(temp != nullptr){
                cout << temp-> data << " -> ";
                temp = temp -> next;
            }
            cout << "NULL\n";
        }

        void onesComplement(){
            node* temp = head;
            cout << "1's: ";
            while(temp != nullptr){
                cout << !temp->data;
                temp = temp -> next;
            }
        }

        void twosComplement(){
            node* temp = head;
            bool carry = true;
            
            while(temp != nullptr){
                temp -> data = !temp-> data;
                temp = temp -> next;
            }

            temp = tail;
            while(temp != nullptr){
                if(carry){
                    if(temp -> data == 0){
                        temp -> data = 1;
                        carry = false;
                        break;
                    }else{
                        temp -> data = 0;
                    }
                }
                temp = temp -> prev;
            }
            if(carry){
                addDigit(1);
            }

            cout << "\n2s: ";
            display();
        }
};

int main(){

 complement num;
    int number;
    cout << "Enter a number: ";
    cin >> number;

    num.convertTobinary(number);
    cout << "Binary: ";
    num.display();

    num.onesComplement();
    num.twosComplement();

    return 0;
}