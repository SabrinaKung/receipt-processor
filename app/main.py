from fastapi import FastAPI, HTTPException, Path
from uuid import uuid4
from app.models import Receipt, ReceiptResponse, PointsResponse
from app.logic import calculate_points

app = FastAPI()
db = {}


@app.post("/receipts/process", response_model=ReceiptResponse)
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid4())
    points = calculate_points(receipt)
    db[receipt_id] = points
    return {"id": receipt_id}


@app.get("/receipts/{receipt_id}/points", response_model=PointsResponse)
def get_points(
    receipt_id: str = Path(..., pattern=r"^\S+$", description="The ID of the receipt.")
):
    if receipt_id not in db:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    return {"points": db[receipt_id]}
