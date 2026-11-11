class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = True
        s = s.strip()
        print(s)
        op = ["[", "{", "("]
        inv = ["]", "}", ")"]
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in s:
            if i in op:
                stack.append(i)
                continue
            if i in pairs:
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
                 

            