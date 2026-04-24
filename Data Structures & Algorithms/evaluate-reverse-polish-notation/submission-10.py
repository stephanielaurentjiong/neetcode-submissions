class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #If there are only 1 element and that element is a digit, return that token
        if len(tokens) == 1 and tokens[0].isdigit():
            return int(tokens[0])

        queue = deque()
   

        for token in tokens:
            if (token == "+"):
                a, b = queue.pop(), queue.pop()
                queue.append(a + b)
            elif (token == "-"):
                a, b = queue.pop(), queue.pop()
                queue.append(b - a)
            elif (token == "*"):
                a, b = queue.pop(), queue.pop()
                queue.append(a * b)
            elif (token == "/"):
                a, b = queue.pop(), queue.pop()
                queue.append(int(float((b) / a)))
            else:
                queue.append(int(token))

        return queue[0]       