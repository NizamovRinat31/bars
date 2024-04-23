
from dataclasses import dataclass


@dataclass
class BasketItem:
    product_id: int
    quantity: int