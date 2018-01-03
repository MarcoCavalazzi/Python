"""
Petal Power is a chain of gardening stores. We help them analyze their inventory.
"""

import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory.head(10) # The first 10 rows represent data from your Staten Island location.

product_request = staten_island['product_description'] # What products are sold at your Staten Island location?

seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == "seeds")] # What types of seeds are sold at the Brooklyn location?

lam = lambda inventory: True if inventory['quantity'] > 0 else False
inventory['in_stock'] = inventory.apply(lam, axis=1)

inventory['total_value'] = inventory.price * inventory.quantity # Petal Power wants to know how valuable their current inventory is.

# The Marketing department wants a complete description of each product for their catalog.
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print inventory