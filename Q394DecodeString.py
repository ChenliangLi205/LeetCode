class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        strStack = [""]
        timeStack = []
        numChars = []
        for c in s:
            if c == '[':
                strStack.append("")
                time = 0
                for num in numChars:
                    time *= 10
                    time += int(num)
                timeStack.append(time)
                numChars = []
            elif c == ']':
                Str = strStack.pop(-1)
                repeat = ""
                time = timeStack.pop(-1)
                for i in range(time):
                    repeat += Str
                strStack[-1] += repeat
            elif '0' <= c<= '9':
                numChars.append(c)
            else:
                strStack[-1] += c
        return strStack[-1]
# And a C++ version
# #include <stack>
# class Solution {
# public:
#     string decodeString(string s) {
#         if(s.empty()){
#             return s;
#         }
#         string newString;
#         stack<string> strStack;
#         strStack.push(*new string());
#         stack<int> times;
#         vector<char> numbers;
#         for(char c: s){
#             if(c == '['){
#                 int number = 0;
#                 for(int j=0;j<numbers.size();j++){
#                     number *= 10;
#                     number += numbers[j]-'0';
#                 }
#                 times.push(number);
#                 strStack.push(*new string());
#                 numbers.clear();
#                 continue;
#             }
#             if(c == ']'){
#                 int time = times.top();
#                 times.pop();
#                 string repeat = strStack.top();
#                 string out;
#                 strStack.pop();
#                 for(int i=0;i<time;i++)
#                     out += repeat;
#                 strStack.top() += out;
#                 continue;
#             }
#             if(c>='0' && c<='9'){
#                 numbers.push_back(c);
#                 continue;
#             }
#             strStack.top().append(1,c);
#         }
#         newString = strStack.top();
#         return newString;
#     }
# };
