from dataclasses import dataclass
from enum import Enum

from click import BOOL



class Item(Enum):
    LAPTOP = 999.99
    MOUSE = 12.25


class Order:
    def __init__(self, order_id : int, customer_name : str, items : list[Item]):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items 


    def __str__(self) -> str:
        items_str = "\n".join([f"{item.name}: ${item.value}" for item in self.items])
        return f"Order ID: {self.order_id}\nCustomer: {self.customer_name}\nItems:\n{items_str}\nTotal: ${self._get_total_price()}"
        
        
    def _get_total_price(self) -> float:
        return sum([item.value for item in self.items])
        
        
    @classmethod
    def create_order(cls, order_id : int, customer_name : str, items : list[Item]):
        order = cls(order_id, customer_name, items)
        order._validate_order_id(order_id)
        order._validate_customer_name(customer_name)
        
        return order

    def _validate_order_id(self, order_id : int) -> None:
        if not isinstance(order_id, int) or order_id <= 0:
            raise ValueError("Order ID must be a positive integer.")
    
    def _validate_customer_name(self, customer_name : str) -> None:
        if not isinstance(customer_name, str) or not customer_name.strip():
            raise ValueError("Customer name must be a non-empty string.")
    
    
if __name__ == '__main__':
    order = Order.create_order(1, "Alice", [Item.LAPTOP, Item.LAPTOP, Item.MOUSE])

    print(order)