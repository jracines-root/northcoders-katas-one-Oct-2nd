def count_veg(veg_list, target_match):
    count = 0
    for veg in veg_list:
        if veg['type'] == target_match:
            count += veg['quantity']
    return count

print(f"test type:= root we expect answer to be 9, we got {count_veg([
  {"name": "Parsnip", "type": "root", "quantity": 4},
  {"name": "Broccoli", "type": "brassica", "quantity": 1},
  {"name": "Carrot", "type": "root", "quantity": 5},
  {"name": "Onion", "type": "bulb", "quantity": 3},
  {"name": "Chard", "type": "leaf", "quantity": 3},
  {"name": "Runner beans", "type": "legume", "quantity": 8}
], "root")}")



"""
count_veg([
  {"name": "Parsnip", "type": "root", "quantity": 4},
  {"name": "Broccoli", "type": "brassica", "quantity": 1},
  {"name": "Carrot", "type": "root", "quantity": 5},
  {"name": "Onion", "type": "bulb", "quantity": 3},
  {"name": "Chard", "type": "leaf", "quantity": 3},
  {"name": "Runner beans", "type": "legume", "quantity": 8}
], "root")
  --> 9
"""