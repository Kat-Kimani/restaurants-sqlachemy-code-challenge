# seeds.py

from faker import Faker
import random 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review




if __name__ == '__main__':
    engine = create_engine('sqlite:///db/restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    fake = Faker()
    
    def create_restaurants(num_restaurants):
         for _ in range(num_restaurants):
            name = fake.company()
            price = fake.random_int(min=2000, max=10000)
            restaurant = Restaurant(name=name, price=price)
            session.add(restaurant)
        
    def create_customers(num_customers):
        for _ in range(num_customers):
            first_name = fake.first_name()
            last_name = fake.last_name()
            customer = Customer(first_name=first_name, last_name=last_name)
            session.add(customer)
        
        
    def create_reviews(num_reviews):
        restaurants = session.query(Restaurant).all()
        customers = session.query(Customer).all()

        for _ in range(num_reviews):
            review = fake.text(max_nb_chars=50)
            star_rating = fake.random_int(min=1, max=5)
            restaurant = fake.random_element(restaurants)
            customer = fake.random_element(customers)

            review = Review(review=review, star_rating=star_rating)
            review.restaurant = restaurant
            review.customer = customer
            session.add(review) 
            
    # Generate the fake data
    create_restaurants(5)
    create_customers(10)
    create_reviews(40)
    
    # Commit the changes to the database
    session.commit()              

