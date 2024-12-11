#include <iostream>
using namespace std;

class deque{
    int* arr;
    int front;
    int rear;
    int size;
    int capacity;

    public:
        deque(int capacity){
            this->capacity = capacity;
            arr = new int[capacity];
            front = -1;
            rear = -1;
            size = 0;
        }

        ~deque(){
            delete[] arr;
        }

        bool isempty(){
            return size == 0;
        }
        bool isfull(){
            return size == capacity;
        }

        void insertFront(int value){
            if(isfull()){
                cout << "Full\n";
                return;
            }
            if(isempty()){
                front = rear = 0;
            }else{
                front = (front - 1 + capacity) % capacity;
            }

            arr[front] = value;
            size++;
        }

        void insertRear(int value){
            if(isfull()){
                cout << "full\n";
                return;
            }

            if(isempty()){
                front =rear = 0;
            }else{
                rear = (rear + 1) % capacity;
            }

            arr[rear]= value;
            size++;
        }

        void deletefront(){
            if(isempty()){
                cout << "empty\n";
                return;
            }

            if(front == rear){
                front = rear = -1;
            }else {
                front = (front + 1) % capacity;
            }
            size--;
        }

        void deleterear(){
             if(isempty()){
                cout << "empty\n";
                return;
            }

            if(front == rear){
                front = rear = -1;
            }else {
                rear = (rear - 1 + capacity) % capacity;
            }

            size--;
        }

        void display(){
            if(isempty()){
                cout << "empty\n";
                return;
            }

            cout << "deque: ";
            int i = front;
            while(true){
                cout << arr[i] << " ";
                if(i == rear) break;
                i = (i + 1) % capacity;
            }
        }
};

int main(){
    int capacity;
    cout << "Enter the capacity of the deque: ";
    cin >> capacity;

    deque dq(capacity);
    dq.insertRear(10);
    dq.insertRear(20);
    dq.insertFront(30);
    dq.display();


    return 0;
}