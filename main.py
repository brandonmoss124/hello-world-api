from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    """Show that the calculator API is running."""
    return {"message": "Calculator API is running"}

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    """Return the sum of two numbers."""
    return {"operation": "add", "a": a, "b": b, "result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    """Return the difference of two numbers."""
    return {"operation": "subtract", "a": a, "b": b, "result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    """Return the product of two numbers."""
    return {"operation": "multiply", "a": a, "b": b, "result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    """Return the quotient of two numbers."""
    if b == 0:
        raise HTTPException(status_code=422, detail="Division by zero is not allowed.")
    return {"operation": "divide", "a": a, "b": b, "result": a / b}

@app.get("/power/{a}/{b}")
def power(a: float, b: float):
    """Raise a to the power of b."""
    return {"operation": "power", "a": a, "b": b, "result": a ** b}

@app.get("/percent/{a}/{b}")
def percent(a: float, b: float):
    """Return a as a percent of b."""
    if b == 0:
        raise HTTPException(status_code=422, detail="Cannot divide by zero.")
    return {"operation": "percent", "a": a, "b": b, "result": (a / b) * 100}

@app.get("/average/{a}/{b}/{c}")
def average(a: float, b: float, c: float):
    """Return the average of three numbers."""
    return {"operation": "average", "numbers": [a, b, c], "result": (a + b + c) / 3}
    