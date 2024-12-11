#include <iostream>
using namespace std;

class node{
    public:
        int data;
        int priority;
        node* next;

        node(int data, int priority){
            this->data = data;
            this->priority = priority;
            next = nullptr;
        }
};

class priorityQueue{
    node* head;
    public:
        priorityQueue(){
            head = nullptr;
        }

        void addData(int d, int p){
            node* newnode = new node(d, p);
            if(head == nullptr || head->priority <= p){
                newnode -> next = head;
                head = newnode;
            }else{
                node* temp = head;
                while(temp->next != nullptr && temp ->next->priority >= p){
                    temp = temp -> next;
                }

                newnode -> next = temp -> next;
                temp -> next = newnode;

            }
        }
        
        bool isempty(){
            return head == nullptr;
        }

        void remove(){
            if(isempty()){
                cout << "empty\n";
                return;
            }else{
                node* temp = head;
                head = head->next;
                delete temp;
            }
        }

        void display(){
            if(isempty()){
                cout << "empty\n";
            }else{
                node* temp = head;
                while(temp != nullptr){
                    cout << temp -> data << " -> ";
                    temp = temp -> next;
                }
            }
        }
};


int main(){
    priorityQueue q;
    q.addData(5,3);
    q.addData(10,1);
    q.addData(15,2);
    q.addData(20,4);
    q.display();


    return 0;
}