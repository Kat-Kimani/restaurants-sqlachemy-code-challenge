# models.py

import os
import sys
from sqlalchemy.orm import relationship, backref

sys.path.append(os.getcwd)

from sqlalchemy import (
    create_engine,
    PrimaryKeyConstraint,
    Column,
    String,
    Integer,
    ForeignKey,
)

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine("sqlite:///db/restaurants.db", echo=True)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    review = Column(String())
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    restaurant = relationship("Restaurant", backref="reviews")
    customer = relationship("Customer", backref="reviews")

    def __repr__(self):
        return f"Review(id={self.id}, review={self.review}, star_rating={self.star_rating})"

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    def get_reviews(self):
        return self.reviews

    def full_review(self):
        customer_full_name = f"{self.customer.first_name} {self.customer.last_name}"
        return f"Review for {self.restaurant.name} by {customer_full_name}: {self.star_rating} stars."


#############################################


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    restaurant_reviews = relationship(
        "Review", back_populates="restaurant", overlaps="reviews"
    )

    def get_reviews(self):
        return self.restaurant_reviews

    @property
    def customers(self):
        return [review.customer for review in self.restaurant_reviews]

    def __repr__(self):
        return f"Restaurant(id={self.id}, name={self.name}, price={self.price})"
    
    @classmethod
    def fanciest(cls):
        return cls.query.order_by(cls.price.desc()).first()

    def all_reviews(self):
        reviews = self.reviews
        review_strings = [
            f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars."
            for review in reviews
        ]
        return review_strings


######################################


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    # customer_reviews = relationship("Review", backref="customer_backref")
    customer_reviews = relationship(
        "Review", back_populates="customer", overlaps="reviews"
    )

    def __repr__(self):
        return f"Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name}) "

    def get_reviews(self):
        return self.customer_reviews

    def get_restaurants(self):
        return [review.restaurant for review in self.customer_reviews]

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        favorite_review = max(self.reviews, key=lambda r: r.star_rating)
        return favorite_review.restaurant
        # return max(self.reviews, key=lambda r: r.star_rating).restaurant
        # return max(self.reviews, key=lambda r: r.rating).restaurant
        # return max(self.reviews, key=lambda r: r.restaurant.star_rating).restaurant

    def add_review(self, session, restaurant, rating):
        # Create a new Review instance
        review = Review(review="", star_rating=rating)

        # Associate the review with the restaurant and customer
        review.restaurant = restaurant
        review.customer = self

        # Add the review to the session and commit the changes
        session.add(review)
        session.commit()

    def delete_reviews(self, session, restaurant):
        reviews_to_delete = [
            review
            for review in self.customer_reviews
            if review.restaurant == restaurant
        ]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()
