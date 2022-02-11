import random

#Part A
weeks = 16
print("Weeks:", weeks)
classes = 5
print("Classes:", classes)
tuition = 6000
print("Tuition:", tuition)
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:",cost_per_week)
# 2 MWF classes and 3 TR classes
classes_per_week = 12
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)

#Part B
my_list = [1,2,3,4,5,6,7,8,9,10]
years = random.choice(my_list)
print("Years:", years)
