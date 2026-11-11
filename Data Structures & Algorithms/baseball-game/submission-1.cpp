#include <stack>
class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<string> st;

        for (int i = 0; i < operations.size(); i++){
            if (operations[i] == "+"){
                int x = stoi(st.top());
                st.pop();
                int y = stoi(st.top());
                st.pop();
                int z = x + y;
                st.push(to_string(y));
                st.push(to_string(x));
                st.push(to_string(z));
            }
            else if (operations[i] == "C"){
                st.pop();
            }
            else if (operations[i] == "D"){
                int x = stoi(st.top());
                st.push(to_string(x * 2));
            }
            else{
          
                st.push(operations[i]);
            }
        } 


        int sum = 0;
        while(!st.empty()){
            cout << st.top() << " " << endl;
            sum += stoi(st.top());
            st.pop();
        }
        return sum;
    }
};