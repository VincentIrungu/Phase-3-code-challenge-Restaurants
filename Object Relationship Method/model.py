class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self._reviews = []
        pass

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)

    def restaurants(self):
        five_star = set()
        for review in self._reviews:
            five_star.add_review(review)
        return list(five_star)

class Review: 
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating

    def get_customer(self):
        return self._customer
    
    def get_restaurant(self):
        return self.restaurant

        pass

class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self._reviews = []
        pass

    def add_review(self,review):
        self._reviews.append(review)
    
    def reviews(self):
        return self._reviews


    def customers(self):
        pleased_customers = set()
        for review in self._reviews:
            pleased_customers.add(review.customer())
        return list(pleased_customers)



# Use of The Code
# Creating instances of Customer, Restaurant and Review respectively
customer = Customer("Alex Kiragu")
print(Customer("Alex Kiragu")) # Output Returns a customer object  <__main__.Customer object at 0x7f7745e57bb0>

customer2= Customer("Aida Odinga")
print(Customer("Aida Odinga"))


restaurant = Restaurant("Moringa Lagoon")
print(Restaurant("Moringa Lagoon"))# Output Returns a restaurant object <__main__.Restaurant object at 0x7f35c8bc3970>

restaurant2 = Restaurant("Waterfront Thehub")
print(Restaurant("Waterfront Thehub"))

# Adding reviews for customers and restaurants
customer.add_review(restaurant, 6)
customer2.add_review(restaurant2, 2)
customer2.add_review(restaurant, 6)

#Getting the reviews for each restaurant
restaurant_reviews = restaurant.reviews()
restaurant2_reviews = restaurant2.reviews()


print("Reviews for", restaurant.restaurant_name + ":")
for review in restaurant_reviews:
    print(f"It was reviewed by {review.get_customer().customer_name}, Rating: {review.rating}")
    # Output is all the below form Review......Odinga, Rating:6(line 82 -line 84) a list of customers who reviewed Moringa Lagoon
    # Reviews for Moringa Lagoon:
    # It was reviewed by Alex Kiragu, Rating: 6 
    # It was reviewed by Aida Odinga, Rating: 6

print("Reviews for", restaurant2.restaurant_name + ":")
for review in restaurant2_reviews:
    print(f"It was reviewed by {review.get_customer().customer_name}, Rating: {review.rating}")
    # Output is line 90 -line 91 (Reviews for Water..........Rating: 2)
    # Reviews for Waterfront Thehub:
    # It was reviewed by Aida Odinga, Rating: 2


    
   






