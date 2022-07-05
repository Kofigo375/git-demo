class customer:
    def __init__(self, name, age, gender):
       self.name = name
       self.age = age
       self.gender = gender 

 #creating a customer
customer_1 = customer("Ephraim", "22", "male")
print(customer_1.age, customer_1.gender)

customer_2 = customer("Mensah", "14", "female")
print(customer_2.name, customer_2.age)

#creating a list of customers
customers = [
    customer("Isaac", "76", "male"),
    customer("musah", "90", "woman"),
    customer("Newton","24","male"),
    customer("keren","28","female")
]
print(customers[2].gender)
