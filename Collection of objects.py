## Collection of objects
#TUPLES
person=("Amiina",19,"cs")
point=(3,5)
single=(42,)
empty=()
#unpacking
name, age, major = person
print(name)
#using indexing
print(point[0])
#RETURNING 2 VALUES FROM A FUNCTION
def min_max(numbers):
    return min(numbers),max(numbers)
lo,hi=min_max([3,5,1,9,2])
print(lo,hi)
#DICTIONARIES
student={ "name": "Alice", "age": 20, "major": "Computer Science" }
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 20
student["age"]=21
print(student["age"])  # Output: 21
student["year"]=2026 #adding a key
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'year': 2026}
#A dictionary with a dictionary in it

students={
    "student1": {#key
        "name": "Alice",
        "age": 20,
        "major": "Data Science"#values
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "major": "Computer Science"
    }
}     
print(students["student1"]["name"])  # Output: Alice
print(students["student2"]["major"])  # Output: Computer Science
print(len(students))  # Output: 2
print(students.values())  # Output: dict_values([...])
print(students.keys())  # Output: dict_keys(['student1', 'student2'])
#looping through a dictionary
for student_id, info in students.items():
    print(f"ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Major: {info['major']}")
#sets
colours={"red","green","blue"}
nums={1,2,2,3,3,3}
print(colours)  # Output: {'blue', 'green', 'red'}
print(nums)  # Output: {1, 2, 3}
a={1,2,3}
b={3,4,5}
print(a|b)  # Union: {1, 2, 3, 4, 5}
print(a&b)  # Intersection: {3}
print(a-b)  # Difference: {1, 2}
print(a^b)  # Symmetric Difference: {1, 2, 4, 5} or
print((a-b)|(b-a))  # Symmetric Difference: {1, 2, 4, 5}
#removing duplicates from a list using a set
numbers=[1,2,2,3,3,3]
unique_numbers=set(numbers)
print(unique_numbers)  # Output: {1, 2, 3}
#EXERCISE TWO SETS OF STUDENTIDS( PRINT INTERSECTION AND DIFFERENCE)
student_ids1 = {101, 102, 103, 104}
student_ids2 = {103, 104, 105, 106}
# Intersection
print(student_ids1 & student_ids2)  # Output: {103, 104}
# Difference
print(student_ids1 - student_ids2)  # Output: {101, 102}

#ASSIGNMENT1
stock={
    "w001":("Rolex Submariner",1500),
    "w002":("Casio G-shock",120),
    "s001":("Nike Air Max",90),
    "s002":("Adidas Yeezy",200),
    "s003":("Rolex Submariner",1500)
}
daily_orders=["w001","s001","w001","s002","s001","w002"]
#1.unpacking the tuple for s002 into variables name and price
name,price=stock["s002"]
print(f"Product: {name}, Price: {price}")

#incase i tried stock["w001"][0]="Rolex Daytona" 
# it would give an error because tuples are immutable

#2.Using set to find unique products ordered
# Convert the list into a hashable tuple right before looking it up
# Look up each item code one-by-one from daily_orders to get its product details
unique_products = set(stock[code][0] for code in daily_orders)
print(f"Unique Products Ordered: {unique_products}")

#ii,The owner says some stock was never ordered today.
# use set operation (difference) between all stock keys and daily_orders to find which product was not ordered at all

unoredered_products = set(stock.keys()) - set(daily_orders)
print(f"Unordered Products: {unoredered_products}")


#3Add a new entry to stock s004("Puma RS-X", 110) 
stock["s004"] = ("Puma RS-X", 110)
print(f"Updated Stock: {stock}")

#II,Create a new dictionary called order_count that counts how many times each productid appearsin daily_orders 
order_count = {}
for code in daily_orders:
    order_count[code] = order_count.get(code, 0) + 1
print(f"Order Count: {order_count}")

#iii,Using order_count and stock calculate totasales for the day
total_sales=sum(order_count[code]*stock[code][1] for code in order_count)
print(f"Total Sales for the Day: ${total_sales}")