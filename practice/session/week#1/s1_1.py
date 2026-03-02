#hello world
def hello():
    print("Hello, World!")
hello()

#mood
def today_mood():
    mood = "Good"
    print("Today's mood is: " + mood)

today_mood()

#add a function call so that "Lunch today is: 🍕" is printed to the console.
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu('🍕')

#The following function returns the sum of two integers: a and b.
def add(a, b):
    return a + b

print(add(1, 2))

#Write a function product() that returns the product of two integers, a and b.
def product(a,b):
    return a * b

print(product(8,2))

#Function that takes age as a parameter and returns "child" if less than 18, and "adult" otherwise.
def classify_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

print(classify_age(18))
print(classify_age(7))

#If hour is 2, the function should return "taco time 🌮".
#If hour is 12, the function should return "peanut butter jelly time 🥪”.
#Otherwise, the function should return "nap time 😴".

def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"

print(what_time_is_it(2))

#Blackjack

def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust")
    elif score < 17 and score > 21:
        print("Nice hand!")
    elif score < 17:
        print('Hit me')

blackjack(21)

#Write a function that returns the first item in the list. Return None if the list is empty.
def get_first(lst):
    if lst == []:
        return None
    else:
        return lst[0]

print(get_first([2,3,4]))

#Write a function that returns the last item in the list. Return None if the list is empty.
def get_last(lst):
    if lst == []:
        return None
    else:
        return lst[-1]

print(get_last([2,3,4]))

#Write a function to print numbers between 1 and a given stop value
def counter(stop):
    for i in range(stop):
        print(i + 1)

print(counter(7))

#Write a function sum_ten() that returns the sum of numbers from 1 to 10.
def sum_ten():
    return sum(range(0, 11))

print(sum_ten())

#returns the sum of numbers from 1 to a given stop value
def sum_positive_range(stop):
    return sum(range(stop + 1))

print(sum_positive_range(6))

#returns the sum of numbers from a given start value to a given stop value
def sum_range(start, stop):
    return sum(range(start, stop + 1))

print(sum_range(3, 9))

#Write a function that takes a list and prints all negative numbers in the list.
def print_negatives(lst):
    for item in lst:
        if item < 1:
            print(item)

print_negatives([-2,3,-4])











