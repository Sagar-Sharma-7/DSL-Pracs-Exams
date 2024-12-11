#include <iostream>
#include <stack>
#include <string>
using namespace std;

class converter{
    public:
        bool isOperator(char c){
            return (c == '+' || c == '-' || c == '*' || c == '/');
        }

        string postfixtToInfix(string postfix){
            stack<string> s;
            for(char c: postfix){
                if(!isOperator(c)){
                    s.push(string(1, c));
                }else{
                    string operand2 = s.top(); s.pop();
                    string operand1 = s.top(); s.pop();
                    string exp = "(" + operand1 + string(1, c) + operand2 + ")";
                    s.push(exp);
                }
            }
            return s.top();
        }

        string postfixToPrefix(string postfix){
            stack<string> s;

            for(char c: postfix){
                if(!isOperator(c)){
                    s.push(string(1, c));
                }else{
                    string operand2 = s.top(); s.pop();
                    string operand1 = s.top(); s.pop();

                    string exp = string(1,c) + operand1 + operand2;
                    s.push(exp);
                }
            }
            return s.top();
        }
};

int main(){
    string postfix;
    cout << "Enter Postfix Experssion: ";
    cin >> postfix;

    converter converter;
    string infix = converter.postfixtToInfix(postfix);
    cout << "Infix Expression: " << infix << endl;

    string prefix = converter.postfixToPrefix(postfix);
    cout << "Prefix Expression: " << prefix << endl;

    return 0;
}