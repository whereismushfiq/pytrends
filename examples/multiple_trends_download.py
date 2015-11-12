from pytrends.pyGTrends import pyGTrends
import time
from random import randint

google_username = "xxx@gmail.com"
google_password = "xxxx"
path = ""

# connect to Google
connector = pyGTrends(google_username, google_password)

# Put all of your wordlist here as many as you want

list = ['Ohio', 'washington', 'New york', 'California', 'florida' , 'georgia', 'north carolina']

count = 0

# it will download csv files for those words in different files

for q in list:    
    connector.request_report(q)
    # wait a random amount of time between requests to avoid bot detection
    i = randint(4, 9)
    time.sleep(randint(1*i, 2*i))
    # download file
    i = randint(4, 9)
    count += 1
    connector.save_csv(path, q)
    print (" %i files downloaded" % count )     
    time.sleep(randint(1*i, 2*i))
