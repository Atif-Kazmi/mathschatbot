import streamlit as st
import sympy as sp
from sympy import symbols, solve, diff, integrate
import spacy

# Install spaCy model (if not already installed)
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    st.write("Downloading spaCy model...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load('en_core_web_sm')

# Define symbolic variable for math operations
x = symbols('x')

# Function to determine what the user wants to do
def parse_math_query(query):
    doc = nlp(query.lower())
    
    if "solve" in query:
        return "solve"
    elif "differentiate" in query or "derivative" in query:
        return "differentiate"
    elif "integrate" in query or "integral" in query:
        return "integrate"
    else:
        return "evaluate"

# Function to evaluate expressions like "x^2 + 2x"
def evaluate_expression(expr):
    try:
        result = sp.sympify(expr)
        return result
    except Exception as e:
        return f"Error: Invalid expression - {e}"

# Function to solve equations like "x^2 + 2x - 3 = 0"
def solve_equation(equation, var):
    try:
        equation = equation.replace("=", "-")  # Adjust the format for solving
        sol = solve(equation, var)
        return sol
    except Exception as e:
        return f"Error: Could not solve - {e}"

# Function to differentiate expressions like "x^2"
def differentiate_expression(expr, var):
    try:
        derivative = diff(expr, var)
        return derivative
    except Exception as e:
        return f"Error: Could not differentiate - {e}"

# Function to integrate expressions like "x^2"
def integrate_expression(expr, var):
    try:
        integral = integrate(expr, var)
        return integral
    except Exception as e:
        return f"Error: Could not integrate - {e}"

# Main chatbot function to handle user queries
def math_chatbot(query):
    math_operation = parse_math_query(query)
    
    # Extract the mathematical expression from the query (using simple split logic)
    expression = query.split(" ")[-1]  # Extract the last part of the query as the expression
    
    if math_operation == "solve":
        return solve_equation(expression, x)
    elif math_operation == "differentiate":
        return differentiate_expression(expression, x)
    elif math_operation == "integrate":
        return integrate_expression(expression, x)
    else:
        return evaluate_expression(expression)

# Streamlit UI Setup
st.title("Mathematics Solver Chatbot")
st.write("Ask me to solve, differentiate, integrate, or evaluate math expressions!")

# Input box for user queries
user_input = st.text_input("Enter your math problem (e.g., solve x^2 + 2x - 3 = 0)")

# When the user provides input, process the query
if user_input:
    st.write(f"Your query: {user_input}")
    result = math_chatbot(user_input)
    st.write(f"Result: {result}")
