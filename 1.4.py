orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

for order_num in orders:
    if order_num[2] > 1:
      b = str(order_num[1]) + "s"
      print(f"{order_num[0]} placed an order for {order_num[2]} {b}") 
    else:
        print(f"{order_num[0]} placed an order for {order_num[2]} {order_num[1]}")
    
