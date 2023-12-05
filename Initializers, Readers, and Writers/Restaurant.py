class Restaurant:


    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
    
    def get_restaurant_name(self):
        return self.restaurant_name
    
    def set_restaurant_name(self, restaurant_name):
        self.set_restaurant_name = restaurant_name
pass

#Creating 
restaurant1 = Restaurant("Moringa Lagoon")
print(restaurant1.get_restaurant_name()) # Output Moringa Lagoon


#Changing restaurant name
restaurant1.set_restaurant_name("Ol-Pejeta")
print(restaurant1.set_restaurant_name("Olpejeta")) # Output 






