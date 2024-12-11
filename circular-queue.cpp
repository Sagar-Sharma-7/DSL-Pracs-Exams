#include <iostream>
using namespace std;

class queue{
    public:
        int *arr;
        int size;
        int rear;
        int front;

        queue(int size){
            this->size = size;
            arr = new int[size];
            rear = -1;
            front = -1;
        }

        bool isempty(){
            return (front == -1);
        }

        bool isfull(){
            return ((rear + 1)%size == front);
        }

        void push(int value){
            if(isfull()){
                cout << "queue is full\n";
                return;
            }

            if(isempty()){
                front = 0;
            }

            rear = (rear + 1) %size;
            arr[rear] = value;
        }

        void pop(){
            if(isempty()){
                cout << "empty\n";
                return;
            }
            if(front == rear){
                front = rear = -1;
            }else{
                front = (front + 1) %size;
            }
        }

        int top(){
            if(isempty()){
                cout << "empty\n";
                return -1;
            }
            return arr[front];
        }

        void display(){
            if(isempty()){
                cout << "empty\n";
            }else{
                cout << "queue: ";
                int i = front;
                while(true){
                    cout << arr[i] << " ";
                    if(i == rear) break;
                    i = (i + 1) % size;
                }
                cout << endl;
            }
        }

};

int main(){



    return 0;
}