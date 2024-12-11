#include <iostream>
#include <cmath>
using namespace std;

class node{
    public:
        int coeff;
        int exp;
        node* next;

        node(int c, int e){
            coeff = c;
            exp = e;
            next = nullptr;
        }
};

class polynomial{
    node* head;

    public:
        polynomial(){
            head = nullptr;
        }


        void insertTerm(int c, int e){
            node* newnode = new node(c, e);
            if(head == nullptr || head -> exp < e){
                newnode -> next = head;
                head = newnode;
            }else{
                node* temp = head;
                while(temp-> next != nullptr && temp -> next ->exp > e){
                    temp = temp -> next;
                }
                if(temp -> exp == e){
                    temp->coeff += c;
                    delete newnode;
                }
                else{
                    newnode->next = temp->next;
                    temp->next = newnode;
                }
            }
        }

        void display(){
            if(head == nullptr){
                cout << "0" << endl;
                return;
            }

            node* temp = head;
            while(temp != nullptr){
                cout << temp->coeff << "x^" << temp->exp << " + ";
                temp = temp->next;
            }
            cout << "0" << endl;
        }

        int evaluate(int x){
            node* temp = head;
            int result = 0;

            int term_value = 1;

            while(temp != nullptr){
                result += temp->coeff * pow(x, temp->exp);
                temp = temp -> next;
            }
            return result;
        }

        polynomial add(polynomial& other){
            polynomial result;
            node* p1 = head;
            node* p2 = other.head;

            while(p1 || p2){
                if(p1 && (!p2 || p1->exp > p2->exp)){
                    result.insertTerm(p1->coeff, p1->exp);
                    p1 = p1 -> next;
                }
                else if(p2 && (!p1 || p1->exp < p2->exp)){
                    result.insertTerm(p2->coeff, p2->exp);
                    p2 = p2 -> next;
                }else{
                    result.insertTerm(p1->coeff + p2->coeff,  p1->exp);
                    p1 = p1-> next;
                    p2 = p2-> next;
                }
            }
            return result;
        }
};


int main(){
    polynomial p1, p2;
    int terms;
    cout << "Enter the number of terms for the first polynomial: ";
    cin >> terms;
    cout << "Enter the terms as coefficient and exponent pairs:\n";
    for (int i = 0; i < terms; ++i) {
        int coeff, exp;
        cin >> coeff >> exp;
        p1.insertTerm(coeff, exp);
    }

    cout << "Enter the number of terms for the second polynomial: ";
    cin >> terms;
    cout << "Enter the terms as coefficient and exponent pairs:\n";
    for (int i = 0; i < terms; ++i) {
        int coeff, exp;
        cin >> coeff >> exp;
        p2.insertTerm(coeff, exp);
    }

    cout << "First Polynomial: ";
    p1.display();
    cout << "Second Polynomial: ";
    p2.display();

    polynomial sum = p1.add(p2);
    cout << "sum: ";
    sum.display();


    return 0;
}