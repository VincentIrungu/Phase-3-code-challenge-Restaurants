class Review:
    def __init__(self, rating):
        self.rating = rating



class Customer:
        def __init__(self, full_name):
             self.full_name = full_name
             self.reviews = []
             pass
        
        def num_reviews(self):
             return len(self.reviews)
        
        @classmethod
        def find_by_name(cls, name, customers):
             for customer in customers:
                  if customer.full_name == name:
                       return customer
             return None
        
        
        
        @classmethod
        def find_all_by_given_name(cls, name, customers):
                                   return [customer for customer in customers if customer.full_name.split() [0] == name ]

class Restaurant:
        def __init__(self, name):
                self.name = name
                self.reviews = []
                pass
        
        def average_star_rating(self):
                if not self.reviews:
                        return 0.0
                

                total_ratings = sum(review.rating for review in self.reviews)
                return total_ratings / len(self.reviews) if len(self.reviews) != 0 else 0.0

        pass

# Using the code with examples

# Creating instances of customer, restaurant and customer list
customer1 = Customer("Britney Irungu")
print(Customer("Britney Irungu")) # Output <__main__.Customer object at 0x7f92e2096f80>


customer2 = Customer("Britney Nyambura")
print(Customer("Britney Nyambura")) #Output <__main__.Customer object at 0x7f92e2096f20>


customer3 = Customer("Felister Njeri")
print(Customer("Felister Njeri")) #Output <__main__.Customer object at 0x7f92e2096ec0>

customers = [customer1, customer2,customer3]
print(customers) #Output [<__main__.Customer object at 0x7f92e2096fe0>, <__main__.Customer object at 0x7f92e2096f80>, <__main__.Customer object at 0x7f92e2096f20>]

restaurant = Restaurant("Moringa Lagoon")
print(Restaurant("Moringa Lagoon")) # Output <__main__.Restaurant object at 0x7f367159ae90>


#Addition of reviews for Moringa Lagoon
restaurant.reviews.append(Review(5))
restaurant.reviews.append(Review(4))
restaurant.reviews.append(Review(6))

# Adding reviews for customers
customer1.reviews.append(Review(5))
customer1.reviews.append(Review(6))
customer1.reviews.append(Review(4))

customer2.reviews.append(Review(4))
customer2.reviews.append(Review(6))

customer3.reviews.append(Review(6))



#Checking out workability of method that Returns the total number of reviews that a customer has authored
print(customer1.num_reviews()) # Output 3 from three  review ratings 5,6,4
print(customer2.num_reviews()) # Output 2 from two review ratings 4,6
print(customer3.num_reviews()) # Output 1 from one rating 6

#given a string of a **full name**, returns the **first customer** whose full name matches
find_customer1 = Customer.find_by_name("Britney Nyambura", customers)
print(find_customer1.full_name) # Output Britney Nyambura

find_customer2 = Customer.find_by_name("Felister Njeri", customers)
print(find_customer2.full_name) # Output Felister Njeri


#given a string of a given name, returns an **list** containing all customers with that given name
customers_with_first_name = Customer.find_all_by_given_name("Britney", customers)

for customer in customers_with_first_name:
        print(customer.full_name) 

        # Ouput:
        # Britney Irungu
        # Britney Nyambura


#returns the average star rating for a restaurant based on its reviews
print(restaurant.average_star_rating()) # Output 5.0


