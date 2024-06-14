def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_operands = []
    second_operands = []
    operators = []
    widths = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must contain two operands and an operator."
        
        operand1, operator, operand2 = parts
        
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        first_operands.append(operand1)
        second_operands.append(operand2)
        operators.append(operator)
        widths.append(max(len(operand1), len(operand2)) + 2)
    
    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""
    
    for i in range(len(problems)):
        first = first_operands[i]
        second = second_operands[i]
        operator = operators[i]
        width = widths[i]
        
        first_line += first.rjust(width) + "    "
        second_line += operator + second.rjust(width - 1) + "    "
        dashes_line += "-" * width + "    "
        
        if show_answers:
            if operator == "+":
                answer = str(int(first) + int(second))
            elif operator == "-":
                answer = str(int(first) - int(second))
            answers_line += answer.rjust(width) + "    "
    
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes_line.rstrip()
    if show_answers:
        arranged_problems += "\n" + answers_line.rstrip()
    
    return arranged_problems

# Testing the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])) # Expected arranged problems without answers
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)) # Expected arranged problems with answers
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])) # Expected error: "Error: Numbers must only contain digits."