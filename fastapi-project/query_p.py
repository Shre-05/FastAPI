# query parameter:used to specify th varibels in the url,use for search,filter etc
from fastapi import FastAPI

app = FastAPI()

data = [
    {"id": 101, "name": "Shreya", "city": "pune", "risk": "low"},
    {"id": 102, "name": "ravi", "city": "mum", "risk": "low"},
    {"id": 103, "name": "om", "city": "goa", "risk": "high"},
]

@app.get("/customers")
def get_customer(city: str, risk: str):
    filtered = [
        c for c in data
        if c["city"] == city and c["risk"] == risk
    ]

    return {
        "city": city,
        "risk": risk,
        "count": len(filtered),
        "result": filtered
    }
