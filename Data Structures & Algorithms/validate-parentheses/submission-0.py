class Solution:
    def isValid(self, s: str) -> bool:
        lista = []
        for char in s:
            if not lista:
                lista.append(char)
            else:
                if lista[-1]=='[' and char==']':
                    lista.pop()
                elif lista[-1]=='(' and char==')':
                    lista.pop()
                elif lista[-1]=='{' and char=='}':
                    lista.pop()
                else:
                    lista.append(char)
        if not lista:
            return True
        else:
            return False
