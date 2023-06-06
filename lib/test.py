from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Create the engine and session
engine = create_engine("sqlite:///db/restaurants.db")
Session = sessionmaker(bind=engine)
session = Session()


# START TESTING
#############################################################################
# - `Review customer()`
#   - should return the `Customer` instance for this review
# - `Review restaurant()`
#   - should return the `Restaurant` instance for this review


# # Fetch a review from the database
# review = session.query(Review).first()

# # Get the associated customer and restaurant
# customer = review.customer
# restaurant = review.restaurant

# # Print the customer and restaurant information
# print("Customer:", customer)
# print("Restaurant:", restaurant)

# # Close the session
# session.close()
##############################################################


####################################################################

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

#########################################################################
# # Get a restaurant from the database
# restaurant_name = "Mckinney, Hardin and Vaughn"
# restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()

# # Get all the reviews for the restaurant
# reviews = restaurant.reviews

# # Print the reviews
# print("Reviews for", restaurant.name)
# for review in reviews:
#     print("Review:", review.review)

#     # Get all the customers who reviewed the restaurant
#     customers = restaurant.customers

# # Print the customers
# for customer in customers:
#     print("Customer:", customer.first_name, customer.last_name)

# # # Close the session
# session.close()
################################################################
# `Restaurant reviews()`
#   - returns a collection of all the reviews for the `Restaurant`
# - `Restaurant customers()`
#   - returns a collection of all the customers who reviewed the `Restaurant


# # Get a customer from the database
# customer_id = 5
# customer = session.get(Customer, customer_id)

# # Get all the reviews left by the customer
# reviews = customer.customer_reviews

# # Print the reviews
# for review in reviews:
#     print("Review:", review.review)

# # Get all the restaurants reviewed by the customer
# restaurants = customer.get_restaurants()

# # Print the restaurants
# for restaurant in restaurants:
#     print("Restaurant:", restaurant.name)  #
######################################################################
# Customer reviews()`
#   - should return a collection of all the reviews that the `Customer` has left
# - `Customer restaurants()`
#   - should return a collection of all the restaurants that the `Customer` has
#     reviewed


# Fetch a customer from the database (replace <customer_id> with the desired customer's ID)
# customer = session.query(Customer).get(<customer_id>)
# customer_id = 5
# customer = session.get(Customer, customer_id)

# # Test the full_name() method
# print("Customer Full Name:", customer.full_name())

# # Test the favorite_restaurant() method
# favorite_restaurant = customer.favorite_restaurant()
# if favorite_restaurant:
#     print("Favorite Restaurant:", favorite_restaurant.name)
#     max_rating = max(
#         favorite_restaurant.reviews, key=lambda r: r.star_rating
#     ).star_rating
#     print("Star Rating:", max_rating)
###################################################################
# Customer full_name()`
#   - returns the full name of the customer, with the first name and the last name
#     concatenated

# Customer favorite_restaurant()`
#   - returns the restaurant instance that has the highest star rating from this customer

# Fetch a customer from the database
# customer_id = 5
# customer = session.get(Customer, customer_id)

# # Test the full_name() method
# print("Customer Full Name:", customer.full_name())

# # Test the favorite_restaurant() method
# favorite_restaurants = []
# max_rating = 0

# for review in customer.reviews:
#     if review.star_rating > max_rating:
#         favorite_restaurants = [review.restaurant]
#         max_rating = review.star_rating
#     elif review.star_rating == max_rating:
#         favorite_restaurants.append(review.restaurant)

# if favorite_restaurants:
#     print("Favorite Restaurants:")
#     for restaurant in favorite_restaurants:
#         print("Name:", restaurant.name)
#         print("Star Rating:", max_rating)
#         print()

############################################################
# `Customer add_review(restaurant, rating)`
#   - takes a `restaurant` (an instance of the `Restaurant` class) and a rating
#   - creates a new review for the restaurant with the given `restaurant_id`
# customer_id = 5
# customer = session.get(Customer, customer_id)

# # Fetch a restaurant from the database
# restaurant = session.query(Restaurant).first()

# # Fetch the existing reviews for the restaurant by the customer
# existing_reviews = []
# for review in customer.reviews:
#     if review.restaurant == restaurant:
#         existing_reviews.append(review)

# # Print the customer's existing reviews for the restaurant
# print("Existing Reviews:")
# for review in existing_reviews:
#     print("Review:", review.review)
#     print("Rating:", review.star_rating)
#     print()

# # Add a new review for the restaurant
# customer.add_review(session, restaurant, 4)

# # Print the customer's updated reviews for the restaurant
# print("Updated Reviews:")
# for review in customer.reviews:
#     if review.restaurant == restaurant:
#         print("Review:", review.review)
#         print("Rating:", review.star_rating)
#         print()
##############################################################################
# Customer delete_reviews(restaurant)`
#   - takes a `restaurant` (an instance of the `Restaurant` class) and
#   - removes **all** their reviews for this restaurant
#   - you will have to delete rows from the `reviews` table to get this to work!
# # Fetch a restaurant from the database
# customer_id = 4
# customer = session.get(Customer, customer_id)
# restaurant = session.query(Restaurant).first()

# # Get the customer's existing reviews for the restaurant
# existing_reviews = customer.get_reviews()
# print("Existing Reviews:")
# for review in existing_reviews:
#     print("Review:", review.review)
#     print("Rating:", review.star_rating)
#     print()

# # Delete the customer's reviews for the restaurant
# customer.delete_reviews(session, restaurant)
# session.expire_all()  # Refresh the session to reflect the changes

# # Get the updated reviews after deletion
# updated_reviews = customer.get_reviews()
# print("Updated Reviews:")
# for review in updated_reviews:
#     print("Review:", review.review)
#     print("Rating:", review.star_rating)
#     print()


# # Check if the reviews have been deleted
# if len(updated_reviews) == 0:
#     print("Reviews have been successfully deleted.")
# else:
#     print("Reviews were not deleted.")
#############################################################

# - `Review full_review()`
#   - should return a string formatted as follows:

# ```txt
# Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
# ```

# Fetch a customer from the database
customer_id = 4
customer = session.get(Customer, customer_id)

# Print all the customer's reviews
reviews = customer.get_reviews()
for review in reviews:
    print(review.full_review())

# Close the session
session.close()
