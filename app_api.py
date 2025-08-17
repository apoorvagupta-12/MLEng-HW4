"""
This module contains the FastAPI application with endpoints for 
status, greeting, and summing numbers
"""

from fastapi import FastAPI
from pydantic import BaseModel
from .app import VERSION

app = FastAPI(
    title="Simple FastAPI Server",
    description="A FastAPI server with status and greeting endpoints.",
    version=VERSION
)

@app.get("/status")
def get_status() -> dict:
    """Returns the server status."""
    return {"status": "OK"}

@app.get("/version")
def get_version() -> dict:
    """Returns the server version."""
    return {"version": app.version}

@app.get("/sayhi/{name}")
def say_hi(name: str) -> dict:
    """Greets the user with their provided name."""
    return {"message": f"Hi, {name}!"}

class SumRequest(BaseModel):
    """Request model for summing two numbers."""
    a: int
    b: int

@app.post("/sum")
def sum_numbers(data: SumRequest) -> dict:
    """Returns the sum of two numbers using a POST request."""
    return {"sum": data.a + data.b}

# Run as `fastapi run app.py`