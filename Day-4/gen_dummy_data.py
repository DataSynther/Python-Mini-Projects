from faker import Faker

import pandas as pd
import random
from faker import Faker
from random import randrange
from datetime import datetime

nr_of_customers = 10000

fake = Faker('en_US')

customers = []

for customers_id in range(nr_of_customers):

    # Create transaction date 
    d1 = datetime.strptime(f'1/1/2021', '%m/%d/%Y')
    d2 = datetime.strptime(f'8/10/2021', '%m/%d/%Y')
    transaction_date = fake.date_between(d1, d2)

    #create customer's name
    name = fake.name()

    # Create gender
    gender = random.choice(["M", "F"])

    # Create email 
    email = fake.ascii_email()

    #Create city
    city = fake.city()

    #create product ID in 8-digit barcode
    product_ID = fake.ean(length=8)
    
    #create amount spent
    amount_spent = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=100)

    customers.append([transaction_date, name, gender, email, city, product_ID, amount_spent])

customers_df = pd.DataFrame(customers, columns=['Transaction_date','Name', 'Gender','Email', 'City','Product_id', 'Amount_spent']) 
                
pd.pandas.set_option('display.max_columns', None)
print(customers_df)