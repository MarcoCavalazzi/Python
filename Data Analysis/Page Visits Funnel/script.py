"""
Page Visits Funnel
Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.

In this case, our funnel is going to describe the following process:
-A user visits CoolTShirts.com
-A user adds a t-shirt to their cart
-A user clicks "checkout"
-A user actually purchases a t-shirt
"""
import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
print visits
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
print cart
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
print checkout
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print purchase

visits_cart = pd.merge(visits, cart, how='left') #Left merge
tot_visitors = len(visits_cart) #How long is the merged DataFrame?
print tot_visitors
null_cart = len( visits_cart[visits_cart.cart_time.isnull()] ) #How many of the timestamps are null for the column cart_time?
print null_cart
#What percentage of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
print "What percentage of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart? \n%f %%" %(float(null_cart) / tot_visitors * 100)

#What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = pd.merge(cart, checkout, how='left')
tot_cart = len(cart_checkout)
print tot_cart
null_checkout = len( cart_checkout[cart_checkout.checkout_time.isnull()] )
print null_checkout
print "What percentage of users put items in their cart, but did not proceed to checkout? \n%f %%" %(float(null_checkout) / tot_cart * 100)

#Let's merge all four steps of the funnel, in order, using a series of left merges.
all_data = pd.merge( pd.merge(visits_cart, checkout, how='left'), purchase, how='left')
print all_data.head()

#What percentage of users proceeded to checkout, but did not purchase a t-shirt? Note: the shop sells only t-shirts.
tot_checkout = len(all_data)
print tot_checkout
null_purchase = len( all_data[all_data.purchase_time.isnull()] )
print null_purchase
print "What percentage of users proceeded to checkout, but did not purchase a t-shirt? \n%f %%" %(float(null_purchase) / tot_checkout * 100)

#Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)? The first step, where visitors have to put a t-shirt in the cart: 80.5 % of people did not put anything in the cart.

#Let's calculate the average time from initial visit to final purchase.
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print all_data.time_to_purchase
print "Average time to purchase: %s"%(all_data.time_to_purchase.mean())