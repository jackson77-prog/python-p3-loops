#!/usr/bin/env python3

# Write a method `happy_new_year` that outputs numbers starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"
def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

# Write a method `fizzbuzz_printer` that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
def fizzbuzz_printer():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1





# Write a method `reverse_string` that takes one argument, a string, and reverses it. Don't use the built-in `.reverse` method. Instead, loop through the characters in the input string and reverse it.
def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

# Write a function `square_integers()` that takes one argument, a list of integers and returns the list of squared elements.
def square_integers(int_list):
    return [num ** 2 for num in int_list]

