
class customer:
    def __init__(self, name, age, gender):
       self.name = name
       self.age = age
       self.gender = gender 

    def update_age(self, new_age):
        print("calculating your new age")
        self.age = new_age
        # print(customer.age)

    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)

# an example of a static method
# static methods are applied on the class itself
    def output_sometext():
        print("welcome customer")

#the string method allows us to print our customer object as a string
    def __str__(self):
        return self.name + " " + self.age + " " + self.gender
# a method to display all customers objects
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

# the equal method 
# to check if two customers are equal
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False



#creating a list of customers
customers = [
    customer("Isaac", "670", "male"),
    customer("musah", "90", "woman"),
    customer("Newton","24","male"),
    customer("keren","28","female")
]
#print(customers[2].gender)

# updating a customer age with my update_age method
customers[2].update_age("670") 
print(customers[2].age) 

#printing customer at index position 1 using my display method
customers[1].display()

#printing "some text" using a static method
customer.output_sometext()

#printing some customer object as a string
print(customers[2])

# printing all the customers using my print_all_costomers method
customer.print_all_customers(customers)

#checking if two customers are equal
print(customers[0] == customers[2])
