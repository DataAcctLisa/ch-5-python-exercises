# Making the program interactive

# Question 1
# determine the outcome without running the code

a = 10
b = 4

print(a, "-", b, "=", a-b)

# output
#  10 - 4 = 6


# Question 2

# rewrite print() statement to display the same output using the % operator

message = '%d - %d = %d'%(a,b,a-b)
print(message)

# Question 3

# rewrite print() statement to display the same output using the format() method

print('{} - {} = {}'.format(a,b,a-b))

# Question 4

# Determine the output of the following program 

print('''Date:\nJan 11, 2019

Time:\n1.28pm

Venue:\nConvention Center

Number of Pax:\n30''')

# output
# Date:
# Jan 11, 2019
# Time:
# 1.28pm
# Venue:
# Convention Center
# Number of Pax:
# 30

# Question 5

# print('This is a single quotation(') mark and this is a double quotation mark (") mark')
# this will result in an error. make corrections to code so it doesnt

print(r"\nThis is a single quotation (\') mark and this is a double quotation mark (\") mark")
# or answer
print('This is a single quotation (\') mark and this is a double quotation (") mark.')



# Question 6

day = {1:'Tuesday,', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday', 7:'Monday'}
venue = {1:'Tokyo to Osaka', 2:'Osaka', 3:'Kyoto', 4:'Kyoto to Nara', 5:'Nara to Osaka', 6:'Osaka to Tokyo', 7:'Tokyo'}


print('\nTravel Itinerary')
print('Day 1 (%s): %s'%(day[1], venue[1]))
print('Day 2 (%s): %s'%(day[2], venue[2]))
print('Day 3 (%s): %s'%(day[3], venue[3]))
print('Day 4 (%s): %s'%(day[4], venue[4]))
print('Day 5 (%s): %s'%(day[5], venue[5]))
print('Day 6 (%s): %s'%(day[6], venue[6]))
print('Day 7 (%s): %s'%(day[7], venue[7]))

# output
# Travel Itinerary
# Day 1 (Tuesday): Tokyo to Osaka
# Day 2 (Wednesday): Osaka
# Day 3 (Thursday): Kyoto
# Day 4 (Friday): Kyoto to Nara
# Day 5 (Saturday): Nara to Osaka
# Day 6 (Sunday): Osaka to Tokyo
# Day 7 (Monday): Tokyo

# need to use dictionaries for solution

# Question 7

# write program that uses input function to prompt the user to enter integer
# next prompt user to enter another integer

num1 = int(input("Please enter an integer:  "))
num2 = int(input("Please enter another integer:  "))

print('You entered', num1, 'and',num2)
# or book answer
print('You entered %s and %s' %(num1, num2))


# Question 8

in1 = int(input(" Please enter an integer:   "))
in2 = int(input(" Please enter another integer:  "))

average = (in1+in2)/2

print("The average is ", average)

# book answer
print("The average is %.2f" %(average))

# output should be:
# Please enter an integer:
# Please enter another integer:  
# The average is 

# Question 9
# 
# program asking for name
# asking for favorite number
# 

Username = input("Please enter your name:  ")
Favnumber = input("Hi %s what is your favorite number?:  " %(Username))
message = ("%s's number is %s ."%(Username, Favnumber))
print(message)

# or

print(("%s's number is %s ."%(Username, Favnumber)))

# Question 10

cities = {"Chicago":"USA", "Los Angeles":"USA", "New York":"USA", "Osaka":"Japan", "Tokyo":"Japan", "Shanghai":"China","Moscow":"Russia", "Paris":"France", "London":"England", "Seoul":"South Korea"}

message1 = "Cities: Chicago, Los Angeles, New York, Osaka, Tokyo, Shanghai, Moscow, Paris, London, Seoul"
print(message1)

# wrong answer
# answer = input("Please enter a city name from the list above:  ")
# message2 = ("%s is a city in %s."%(answer, input(Cities)))
# print(message2)

# correct book answer

print()

city = input("Please enter a city name from the list above:  ")
print("%s is a city in %s."%(city, cities[city]) )


# output should be:

# Cities: Chicago, Los Angeles, New York, Osaka, Tokyo, Shanghai, Moscow, Paris, London, Seoul

# Please enter a city name from the list above: Osaka

# Osaka is located in Japan

# 


# Question 11

# wrong answer

# numbers = input("Please enter 5 numbers separated by commas:  ")
# print("You entered ", numbers)

# total = sum(numbers.split('+'))
# print(total)

# book answer

userInput = input('Please enter 5 numbers, seperated by commas: ')

inputList = userInput.split(',')

print("\nYou entered %s,%s,%s,%s,%s." %(inputList[0], inputList[1], inputList[2], inputList[3], inputList[4]))

print('The sum is %d. ' %(int(inputList[0]) + int(inputList[1]) + int(inputList[2]) + int(inputList[3]) + int(inputList[4])))



# output should be
# You entered 23,1,12,4,5.
# (or whatever number you entered)
# The sum is 45
# (or the sum of whatever numbers you entered)





