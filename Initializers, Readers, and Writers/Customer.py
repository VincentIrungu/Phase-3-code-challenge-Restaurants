class Customer:
    # Class variable to store all instances of customers
    customers_all = []

    def __init__(self, customer_given_name, customer_family_name):
        self.customer_given_name = customer_given_name
        self.customer_family_name = customer_family_name

        # Add the created instance to the list of all customers
        Customer.customers_all.append(self)

    def get_customer_given_name(self):
        return self.customer_given_name

    def set_given_name(self, customer_given_name):
        self.customer_given_name = customer_given_name

    def get_customer_family_name(self):
        return self.customer_family_name

    def set_customer_family_name(self, family_name):
        self.family_name = family_name

    def customer_full_name(self):
        return f"{self.customer_given_name} {self.customer_family_name}"

    @classmethod
    def get_customers_all(cls):
        return cls.customers_all

'''
# Example usage:

# Creating customer instances
customer1 = Customer("George","Washington")
customer2 = Customer("John","Adams")

print(Customer("George", "Washington"))

#Getting given name

print(customer1.get_customer_given_name()) # Ouput George
print(customer2.get_customer_given_name()) #Output John

#Getting family name
print(customer1.get_customer_family_name()) #Output Washington
print(customer2.get_customer_family_name()) # Output  Adams

#Getting fullname
print(customer1.customer_full_name()) #Output  George Washington
print(customer2.customer_full_name())  #Output Jogn Adams


#Getting instances of all customers
customers_all = Customer.get_customers_all()
print(customers_all)   # Ouput __main__.Customer object at 0x7ff49c663fa0>, <__main__.Customer object at 0x7ff49c663c40>, <__main__.Customer object at 0x7ff49c663be0>]'''



