import random


class Operation:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.result = 0


    def get_numbers(self):
        digits_map = {
            1: 10,
            2: 20,
            3: 40,
            4: 100
        }

        return [random.randint(0, digits_map.get(self.difficulty)), random.randint(0, digits_map.get(self.difficulty))]

    
    def get_operation_sign(self):
        sign_map = {
            1: ['+', '-'],
            2: ['+', '-'],
            3: ['+', '-', '*', '/'],
            4: ['+', '-', '*', '/'],
        }

        return sign_map.get(self.difficulty)[random.randint(0, len(sign_map.get(self.difficulty)) - 1)]
    

    def get_operation_string(self):
        numbers = self.get_numbers()

        sign = self.get_operation_sign()

        operation = f"{numbers[0]} {sign} {numbers[1]}"

        return operation
    

    def get_operation_result(self, operation_string):

        return eval(operation_string)

    
    def operation_manager(self):

        operation_string = self.get_operation_string()

        self.result = round(self.get_operation_result(operation_string), 2)

        return operation_string