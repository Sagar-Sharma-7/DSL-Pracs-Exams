#include <iostream>
#include <string>
using namespace std;

class node{
    public:
        int pnr;
        string name;
        node* next;

        node(int pnr, string name){
            this->pnr = pnr;
            this->name = name;
            next = nullptr;
        }
};

class club{
    node* head;
    node* tail;
    public:
        club(){
            head = nullptr;
            tail = nullptr;
        }

        void addPresident(int pnr, string name){
            node* newnode = new node(pnr, name);
            if(head == nullptr){
                head = newnode;
                tail = newnode;
            }else{
                node* temp = head;
                newnode -> next = temp;
                head = newnode;
            }
        }

        void addmember(int pnr, string name){
            node* newnode = new node(pnr, name);
            if(head == nullptr){
                head = newnode;
                tail = newnode;
            }else{
                node* temp = head;
                while(temp->next != tail){
                    temp = temp -> next;
                }
                temp-> next = newnode;
                newnode->next = tail;
            }
        }

        void addSec(int pnr, string name){
            node* newnode = new node(pnr, name);
            if(head == nullptr){
                head = newnode;
                tail = newnode;
            }else{
                tail -> next = newnode;
                tail = newnode;
            }
        }

        void deleteMember(string n){
            if(head -> name == n){
                node* temp = head;
                head = head -> next;
                delete temp;
                cout << "Deleted\n";
            }else{
                node* temp = head;
                while(temp ->next-> name != n && temp -> next != nullptr){
                    temp = temp -> next;
                }

                if(temp -> next == nullptr){
                    cout << "Not found \n";
                }else{
                    node* toDelete = temp -> next;
                    temp -> next = toDelete -> next;
                    delete toDelete;
                    cout << "Deleted \n";
                }
            }
        }

        void display(){
            node* temp = head;
            while(temp != nullptr){
                cout << "Name: " << temp -> name << ", PNR: " << temp-> pnr << " -> ";
                temp = temp -> next;
            }
            cout << "null";
        }

};

int main(){
    club club;
    club.addPresident(0, "President");
    club.addSec(-1, "Sec");
    club.addmember(1, "sagar");
    club.addmember(2, "raghav");
    club.display();

}