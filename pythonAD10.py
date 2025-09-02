#Python Mathematical expression Parsing and Evaluation Library

#Write a Python library for parsing and evaluating mathematical expressions.
# Import the Abstract Syntax Tree (AST) module
import ast

# Import the math module for mathematical functions and constants
import math

# Define a class for evaluating mathematical expressions
class MathExpressionEvaluator:
    def __init__(self):
        pass

    # Method to evaluate mathematical expressions
    def evaluate(self, expression):
        try:
            # Parse the expression into an Abstract Syntax Tree (AST)
            parsed_expression = ast.parse(expression, mode='eval')

            # Define the allowed names (functions and constants) for evaluation
            allowed_names = {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log,
                'sqrt': math.sqrt,
                **vars(math)  # Include all functions and constants from the math module
            }

            # Evaluate the AST using a custom namespace that includes the allowed names
            result = eval(compile(parsed_expression, filename='', mode='eval'), {}, allowed_names)
            return result
        except SyntaxError:
            print("Invalid expression syntax.")
            return None
        except Exception as e:
            print("Error:", e)
            return None

# Example usage
if __name__ == "__main__":
    evaluator = MathExpressionEvaluator()

    # Evaluate mathematical expressions
    print("Evaluation Results:")
    print("10 + 12 * 4 =", evaluator.evaluate("10 + 12 * 4"))
    print("(12 + 13) * 4 =", evaluator.evaluate("(12 + 13) * 4"))
    print("sin(0.5) =", evaluator.evaluate("sin(0.5)"))
    print("log(10) =", evaluator.evaluate("log(10)"))

