class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = True
        s = s.strip()
        print(s)
        op = ["[", "{", "("]
        inv = ["]", "}", ")"]

        for i in s:
            if i in op:
                stack.append(i)
                continue
            if stack:
                if i == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                    continue
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    print("Here 1")
                    return False
            if i in inv and not stack:
                print(f"Here 2 this is i {i}")

                return False
        if stack:
            print("Here 3")

            return False
        return True                   

            