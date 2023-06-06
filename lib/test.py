from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Create the engine and session
engine = create_engine('sqlite:///db/restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

# # Fetch 5 reviews from the database
# reviews = session.query(Review).all()

# # Print the customer name and review for each review
# for review in reviews:
#     customer = review.customer
#     restaurant = review.restaurant
#     print("Customer:", customer.first_name, customer.last_name)
#     print("Restaurant:", restaurant.name)
#     print("Review:", review.review)
#     print()

# # Close the session
# session.close()

# Get a restaurant from the database
restaurant_name = "Mckinney, Hardin and Vaughn"
restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()

# Get all the reviews for the restaurant
reviews = restaurant.reviews

# Print the reviews
print("Reviews for", restaurant.name)
for review in reviews:
    print("Review:", review.review)
    
# Get all the customers who reviewed the restaurant
    customers = [review.customer for review in reviews]

    # Print the customers
    print("Customers who reviewed", restaurant.name)
    for customer in customers:
        print("Customer:", customer.first_name, customer.last_name)
else:
    print("Restaurant not found.")
   
    
    
    
# Close the session
session.close()    