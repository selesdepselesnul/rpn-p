from builtins import print
import re


class Stack(list):
    def push(self, value):
        self.append(value)

    def peek(self):
        return self[len(self) - 1]

    def is_empty(self):
        return len(self) == 0


class RpnParser(object):
    def __init__(self, arit_expr):
        self.infix_list = arit_expr
        self.operator_stack = Stack()
        self.postfix_list = []

    def parse(self):
        for i in self.infix_list:
            if self.is_operand(i):
                self.postfix_list.append(i)
            elif self.is_operator(i):
                if self.operator_stack.is_empty():
                    self.operator_stack.push(i)
                elif i == '(':
                    self.operator_stack.push(i)
                elif i == ')':
                    self.pop_operator_to_end_expr()
                elif self.is_greater(i, self.operator_stack.peek()):
                    self.operator_stack.push(i)
                else:
                    self.pop_until_greater(i)
                    self.operator_stack.push(i)
            else:
                return ''

        self.fill_postfix_stack()

        return str(self.postfix_list)

    def fill_postfix_stack(self):
        while not self.operator_stack.is_empty():
            self.postfix_list.append(self.operator_stack.pop())

    def pop_operator_to_end_expr(self):
        while self.operator_stack.peek() != '(':
            self.postfix_list.append(self.operator_stack.pop())
        self.operator_stack.pop()

    def pop_until_greater(self, i):
        while not self.operator_stack.is_empty():
            if self.is_greater(i, self.operator_stack.peek()):
                break
            self.postfix_list.append(self.operator_stack.pop())

    def is_greater(self, op1, op2):
        def is_lower_op(op):
            return op == '+' or op == '-'

        def is_mid_op(op):
            return op == '*' or op =='/'

        return ( op1 == '(' or op2 == '(' ) \
               or ( (op1 == '^') and (is_mid_op(op2) or is_lower_op(op2)) ) \
               or ( is_mid_op(op1) and is_lower_op(op2) )

    def is_operand(self, any_string):
        return re.search('\\w', any_string)

    def is_operator(self, any_string):
        return re.search('[\+\-\*\/\^\(\)]', any_string)


if __name__ == '__main__':
    parser = RpnParser('(A+B)*C+(A+B)')
    print(parser.parse())
