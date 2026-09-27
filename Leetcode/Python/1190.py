class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in s:
            if i == ')':
                tempString = ""
                while st[-1] != '(' and len(st) > 0:
                    tempString += st[-1]
                    st.pop()
                if st[-1] == '(' and len(st) > 0:
                    st.pop()
                for ch in tempString:
                    st.append(ch)
            else:
                st.append(i)
            
        return "".join(st)