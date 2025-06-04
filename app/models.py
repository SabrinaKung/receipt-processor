from pydantic import BaseModel, Field
from typing import List


class Item(BaseModel):
    shortDescription: str = Field(
        ...,
        pattern=r"^[\w\s\-]+$",
        description="The Short Product Description for the item.",
    )
    price: str = Field(
        ..., pattern=r"^\d+\.\d{2}$", description="The total price paid for this item."
    )


class Receipt(BaseModel):
    retailer: str = Field(
        ..., pattern=r"^[\w\s\-&]+$", description="The name of the retailer or store."
    )
    purchaseDate: str = Field(
        ...,
        pattern=r"^\d{4}-\d{2}-\d{2}$",
        description="Purchase date in YYYY-MM-DD format.",
    )
    purchaseTime: str = Field(
        ...,
        pattern=r"^\d{2}:\d{2}$",
        description="Purchase time in 24-hour HH:MM format.",
    )
    items: List[Item]
    total: str = Field(
        ..., pattern=r"^\d+\.\d{2}$", description="The total amount paid (e.g., 6.49)."
    )


class ReceiptResponse(BaseModel):
    id: str


class PointsResponse(BaseModel):
    points: int
