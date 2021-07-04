#!/usr/bin/env python
# coding: utf-8

# In[46]:


class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
        self.fuel_capacity = 15
        self.fuel_level = 0
    
    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")
    
    def drive(self):
        print("The car is moving.")
    
    def add_fuel(self):
        print('How many fuel did you add?/n Please input amount!')
        amount = int(input())
        try:
            if amount + self.fuel_level > self.fuel_capacity:
                print(f'Imposible! We can add less than {self.fuel_capacity}')
            else:
                self.fuel_level += amount
                print(f'We added {amount}')
        except:
            print('Please input only number!')


class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        
        self.battery = Battery()
        
        self.battery_size = 75
        self.charge_level = 0
        
    def charge(self):
        self.battery.charge_level = 100
        print("The vehicle is fully charged.")

class Battery:
    def __init__(self,size = 75):
        self.size = size
        self.chage_level = 0
    
    def get_range(self):
        if self.size == 75:
            return 260
        elif self.size == 100:
            return 315


# In[47]:


my_ecar = Electric_car('tesla','model s',2019)


# In[48]:


my_ecar.battery.size


# In[49]:


my_ecar.battery.get_range()


# In[ ]:




