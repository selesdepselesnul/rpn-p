import re


# author : Moch Deden (https://github.com/selesdepelesnul)
VALID_OPERAND = '[a-zA-Z]'
VALID_OPERATOR = '[\+\-\*/\^\(\)]'


class Stack(list):
    def push(self, value):
        self.append(value)

    def peek(self):
        return self[len(self) - 1]

    def is_empty(self):
        return len(self) == 0


class RpnParser(object):
    def __init__(self, arith_expr):
        self.infix_list = filter(lambda x: x != ' ', arith_expr)
        self.operator_stack = Stack()
        self.postfix_list = []

    def parse(self):
        for char in self.infix_list:
            if RpnParser.__is_operand(char):
                self.postfix_list.append(char)
            elif RpnParser.__is_operator(char):
                if self.operator_stack.is_empty():
                    self.operator_stack.push(char)
                elif char == '(':
                    self.operator_stack.push(char)
                elif char == ')':
                    self.__pop_operator_to_end_expr()
                elif self.__is_greater(char, self.operator_stack.peek()):
                    self.operator_stack.push(char)
                else:
                    self.__pop_until_greater(char)
                    self.operator_stack.push(char)
            else:
                return []

        self.__fill_postfix_stack()
        return self.postfix_list

    def __fill_postfix_stack(self):
        while not self.operator_stack.is_empty():
            self.postfix_list.append(self.operator_stack.pop())

    def __pop_operator_to_end_expr(self):
        while self.operator_stack.peek() != '(':
            self.postfix_list.append(self.operator_stack.pop())
        self.operator_stack.pop()

    def __pop_until_greater(self, i):
        while not self.operator_stack.is_empty():
            if RpnParser.__is_greater(i, self.operator_stack.peek()):
                break
            self.postfix_list.append(self.operator_stack.pop())

    @staticmethod
    def __is_greater(op1, op2):
        def is_lower_op(op):
            return op == '+' or op == '-'

        def is_mid_op(op):
            return op == '*' or op == '/'

        return (op1 == '(' or op2 == '(') or \
               ((op1 == '^') and (is_mid_op(op2) or is_lower_op(op2))) or \
               (is_mid_op(op1) and is_lower_op(op2))

    @staticmethod
    def __is_operand(any_string):
        return re.search(VALID_OPERAND, any_string)

    @staticmethod
    def __is_operator(any_string):
        return re.search(VALID_OPERATOR, any_string)
