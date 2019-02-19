class Solution {
public:
    int findNthDigit(int n) {
        if(n <= 9) return n;
        n -= 9;
        int left=10, right=99;
        int numLen = 2;
        int result=0;
        while(true)
        {
            if(numLen<9 && n>(right-left+1)*numLen)
            {
                n-=(right-left+1)*numLen;
                left *= 10;
                right = right*10+9;
                numLen += 1;
            }
            else
            {
                int loc = left + n/numLen;
                int digit = n%numLen;
                if(digit == 0)
                    loc -= 1;
                else
                {
                    for(int i=numLen;i>digit;i--)
                        loc /= 10;
                }
                result = loc%10;
                break;
            }
        }
        return result;
    }
};