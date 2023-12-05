class Review:

    review_all = []
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        Review.review_all.append(self)

    def get_review_rating(self):
        print(f"{self.rating}")

    def set_review_rating(self, rating):
        if (type(rating)== (int or float) and (0 <= rating <=7)):
            print(f"{rating}") 
            self.set_review_rating = rating
        else:
            print("Rating must be an integer or a decimal.")
         
    @classmethod
    def get_review_all(cls):
        return cls.review_all
    
# Creating instances
print(Review("Vincent Irungu", "Moringa Lagoon", 6)) #Output <__main__.Review object at 0x7f04c8787dc0>
print(Review("Emmah", "Burj Khalfa", 5)) # Output <__main__.Review object at 0x7fa98d2a3d60>

# Review rating
review1 = Review("Vincent Irungu", "Moringa Lagoon", 6)
review2 = Review("Emmah", "Burj Khalfa", 5)

print(review1.get_review_rating()) #Output 6
print(review2.get_review_rating()) #Output 5


# Returning all of the reviews
review_all = Review.get_review_all
print(review_all) # Output <bound method Review.get_review_all of <class '__main__.Review'>>


