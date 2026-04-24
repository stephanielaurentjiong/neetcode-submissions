class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')':'(',
        ']':'[',
        '}':'{'
        }

        stack =[]
        for i in s:
            # If the character is a closing bracket
            if i in dict:
                #Check if there is an opening bracket in stack and check if the top most is the pairings
                if stack and stack[-1] == dict[i]:
                    #If so, popped
                    stack.pop()
                else:
                    #If not match, the string has a not matching valid parantheses
                    return False
             # If it's an opening bracket, push it onto the stack
            else:
                stack.append(i)

        return True if not stack else False