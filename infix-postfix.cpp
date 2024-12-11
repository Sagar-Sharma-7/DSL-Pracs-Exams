#include <iostream>
#include <string>
#include <stack>
using namespace std;

class convertpostix{
    string infix;
    string postfix;

    int precedence(char ch){
        if(ch == '+' || ch == '-') return 1;
        if(ch == '*' || ch == '/') return 2;
        return 0;
    }

    public: 
        convertpostix(string infix){
            this->infix = infix;
            postfix = "";
        }

        void convert(){
            stack<char> s;
            for(char ch: infix){
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
                    while(!s.empty() && precedence(s.top()) >= precedence(ch)){
                        postfix+=s.top();
                        s.pop();
                    }
                    s.push(ch);
                }
            }

            while(!s.empty()){
                postfix += s.top();
                s.pop();
            }
        }

        string getpostfix(){
            return postfix;
        }
};


int main(){
 string infix;
    cout << "enter infix string: \n";
    cin >> infix;

    convertpostix converter(infix);
    converter.convert();

    cout << "experssion: " << converter.getpostfix() << endl;

    return 0;
}