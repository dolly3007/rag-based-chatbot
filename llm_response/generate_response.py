# llm_response/generate_response.py
from rag_engine1.query_rag_with_groq import run_rag_with_groq
from tools.physics_solver import solve_physics_equation

def generate_answer(question):
    if "solve" in question.lower() and "=" in question:
        return solve_physics_equation(question)
    return run_rag_with_groq(question)
