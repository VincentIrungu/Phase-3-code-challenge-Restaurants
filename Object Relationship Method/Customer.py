class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        pass


class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        pass


class Review: 
    def __init__(self, customer, restaurant, content=str, rating=int):
        self.customer = customer
        self.restaurant = restaurant
        self.content = content 
        self.rating = rating

    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant

        pass

# Use of The Code
# Creating instances of Customer, Restaurant and Review respectively
customer = Customer("Alex Kiragu")
print(Customer("Alex Kiragu")) # Output Returns a customer object  <__main__.Customer object at 0x7f7745e57bb0>

restaurant = Restaurant("Moringa Lagoon")
print(Restaurant("Moringa Lagoon"))# Output Returns a restaurant object <__main__.Restaurant object at 0x7f35c8bc3970>

review = Review(customer, restaurant,"Great food!", 4) # Can not print since review =.....is an invalid keyword , because of the sign

#Getting the affiliate customer and restaurant respectively
#Customer
review_customer = review.get_customer()

review_restaurant = review.get_restaurant()

#Outputting the affiliate customer and resturant
print(review.customer.customer_name) # Output Alex Kiragu
print(review.restaurant.restaurant_name) #Out Moringa Lagoon

# Creating another Review instance having diffrent coment and rating but not change the restaurant 
reviews = Review(customer, restaurant, "Beautiful Delivery", 7)
print(reviews.customer.customer_name) # Output Returns unchanged customer 
print(reviews.restaurant.restaurant_name) #Output returns unchanged restaurant 


