# models.py

import os
import sys
from sqlalchemy.orm import relationship
sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey  )

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)


class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    review = Column(String())
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    restaurant = relationship('Restaurant', backref='reviews')
    customer = relationship('Customer', backref='reviews')

    def __repr__(self):
        return f'Review(id={self.id}, review={self.review}, star_rating={self.star_rating})'
    
    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant
    
    def get_reviews(self):
        return self.reviews

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)
    
    restaurant_reviews = relationship('Review', back_populates='restaurant', overlaps="reviews")
    
    def get_reviews(self):
        return self.restaurant_reviews
    
    @property
    def customers(self):
        return list({review.customer for review in self.restaurant_reviews})


    def __repr__(self):
        return f'Restaurant(id={self.id}, name={self.name}, price={self.price})'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name}) '

      