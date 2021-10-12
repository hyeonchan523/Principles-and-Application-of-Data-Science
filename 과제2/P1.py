"""
**Instruction**
Please see instruction document.

"""
def P1(parentheses: str) -> bool:        
    stack = []
    for char in parentheses:
        
        if char in ['[', '(', '{']:
            stack.append(char)
        elif char in [']', ')', '}'] :
            if len(stack) ==0:
                return False
            temp = stack.pop()
            if temp == '[' and char == ']':
                pass
            elif temp == '(' and char == ')':
                pass                
            elif temp == '{' and char == '}':
                pass
            else :
                return False
        else :
            pass
    return True


if __name__ == '__main__':
    print(P1('()'))
    print(P1('()[]{}'))
    print(P1('(([)])'))


    

