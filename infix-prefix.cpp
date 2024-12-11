#include <iostream>
#include <string>
#include <stack>
#include <algorithm>
using namespace std;

class convertprefix{
    string infix;
    string prefix;

    int precedence(char ch){
        if(ch == '+' || ch == '-') return 1;
        if(ch == '*' || ch == '/') return 2;
        return 0;
    }

    string reverseExpression(const string& exp){
        string reversed = exp;
        reverse(reversed.begin(), reversed.end());
        for(char& ch: reversed){
            if(ch == '(') ch = ')';
            else if (ch == ')') ch = '(';
        }
        return reversed;
    }

    public:
        convertprefix(string infix){
            this->infix = infix;
            prefix = "";
        }

        void convert(){
            string reversedInfix = reverseExpression(infix);
            string postfix = "";
            stack<char> s;
            for(char ch: reversedInfix){
                if(isalpha(ch)){
                    postfix += ch;
                }else if(ch == '('){
                    s.push(ch);
                }else if(ch == ')'){
                    while(!s.empty() && s.top() != '('){
                        postfix += s.top();
                        s.pop();
                    }
                    s.pop();
                }else{
                    while(!s.empty() && precedence(ch) < precedence(s.top())){
                        postfix += s.top();
                        s.pop();
                    }
                    s.push(ch);
                }
            }

            while(!s.empty()){
                postfix+= s.top();
                s.pop();
            }

            prefix = string(postfix.rbegin(), postfix.rend());
        }

        string getPrefix(){
            return prefix;
        }
};

int main(){

    string infix;
    cout << "Enter infix expression: ";
    cin >> infix;

    convertprefix converter(infix);
    converter.convert();

    cout << "Prefix Expression: " << converter.getPrefix() << endl;

    return 0;
}