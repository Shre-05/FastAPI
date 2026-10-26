# path parameter used to add multiple variables in a single endpoint
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Path parameter
@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {
        "student": student_id
    }


customers = {
    101: {"name": "Ravi", "risk": "high"},
    102: {"name": "Om", "risk": "low"},
    103: {"name": "Raj", "risk": "med"},
}


@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):
    if customer_id not in customers:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    profile = customers[customer_id]

    return {
        "customer_id": customer_id,
        "name": profile["name"],
        "risk": profile["risk"]
    }