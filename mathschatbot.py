import streamlit as st
import sympy as sp
import numpy as np
from sympy import symbols, solve, diff, integrate

# Natural Language Processing (optional for handling user input more flexibly)
import spacy

# Load the English NLP model (for text understanding, optional)
nlp = spacy.load('en_core_web_sm')

def evaluate_expression(expr):
    try:
        result = sp.sympify(expr)
        return result
    except Exception as e:
        return f"Error: {e}"

def solve_equation(equation, var):
    try:
        solution = solve(equation, var)
        return solution
    except Exception as e:
        return f"Error: {e}"

def differentiate_expression(expr, var):
    try:
        derivative = diff(expr, var)
        return derivative
    except Exception as e:
        return f"Error: {e}"

def integrate_expression(expr, var):
    try:
        integral = integrate(expr, var)
        return integral
    except Exception as e:
        return f"Error: {e}"

def process_math_query(query):
    doc = nlp(query)
    math_operation = None

    if "solve" in query.lower():
        math_operation = "solve"
    elif "differentiate" in query.lower() or "derivative" in query.lower():
        math_operation = "differentiate"
    elif "integrate" in query.lower() or "integral" in query.lower():
        math_operation = "integrate"
    else:
        math_operation = "evaluate"

    return math_operation

def math_chatbot(query):
    x = symbols('x')
    math_operation = process_math_query(query)

    # Get the mathematical expression from the query
    expression = query.split()[-1]  # Simple heuristic to extract the expression

    if math_operation == "solve":
        return solve_equation(expression, x)
    elif math_operation == "differentiate":
        return differentiate_expression(expression, x)
    elif math_operation == "integrate":
        return integrate_expression(expression, x)
    else:
        return evaluate_expression(expression)

# Streamlit Interface
st.title("Mathematics Solver Chatbot")

st.write("This chatbot can solve, differentiate, integrate, and evaluate math expressions!")

user_input = st.text_input("Enter your math question here (e.g. solve x^2 + 2x - 3 = 0, differentiate x^2, etc.)")

if user_input:
    result = math_chatbot(user_input)
    st.write(f"Result: {result}")
