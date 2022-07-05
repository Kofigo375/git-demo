
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


 #creating a customer
customer_1 = customer("Ephraim", "22", "male")
#print(customer_1.age, customer_1.gender)

#customer_2 = customer("Mensah", "14", "female")
#print(customer_2.name, customer_2.age)

#creating a list of customers
customers = [
    customer("Isaac", "76", "male"),
    customer("musah", "90", "woman"),
    customer("Newton","24","male"),
    customer("keren","28","female")
]
#print(customers[2].gender)





customers[2].update_age("670") 
print(customers[2].age) 
#customer_1.update_age("99")
#print(customer_1.age)
#customers[1].update_age("45")
#  print(customers[1].update_age)
customers[1].display()