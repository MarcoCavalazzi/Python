"""
A/B Testing for ShoeFly.com
Our favorite online shoe store, ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. We will analyze the data using aggregate measures.
"""

import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print ad_clicks.head()

#print ad_clicks.groupby(['utm_source']).user_id.count().reset_index() # We want to know the number of clicks on ads from each utm_source.

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) * 100 # Was there a difference in click rates for each source?
#print clicks_pivot

testab = ad_clicks.groupby(['experimental_group']).user_id.count().reset_index() # Were approximately the same number of people shown ads A and B?
#print testab
testab_greater = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index() # check to see if a greater percentage of users clicked on Ad A or Ad B.
#print testab_greater

# The Product Manager for the A/B test thinks that the clicks might have changed by day of the week. Let's check that.
a_clicks = ad_clicks[ ad_clicks.experimental_group == 'A' ]
b_clicks = ad_clicks[ ad_clicks.experimental_group == 'B' ]
print a_clicks

# Calculating the percentage of users who clicked on the ad by day
a_clicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
 # .pivot(columns='is_click', index='day', values='user_id')
total = a_clicks.groupby('day')['user_id'].sum().reset_index()['user_id'] #finding the total number of users who clicked and not clicked (necessary to calculate the percentages).
total = total.append(total, ignore_index=True) #ignore_index is necessary to avoid error raised by duplicate values.
a_clicks['total'] = total
lam = lambda x: '%f %%'%(x.user_id/x.total *100)
a_clicks['percentage'] = a_clicks['user_id'] / a_clicks['total'] * 100

print "\n a_clicks: \n"
print a_clicks

b_clicks = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
  #.pivot(columns='is_click', index='day', values='user_id')
b_clicks['total'] = total
b_clicks['percentage'] = b_clicks['user_id'] / b_clicks['total'] * 100

print "\n b_clicks: \n"
print b_clicks


"""
Which is best? Ad A or Ad B?
Comparing the results for A and B, I recommend that the company uses Ad A, since the numbers show a higher percentage of clicks on that ad. While Ad A has percentages of clicks always above 38% throughout the week, Ad B shows percentages as low as 25% and never as high as in the Ad A case.
"""