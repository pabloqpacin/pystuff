# [@Dataquest: Python Basics for Data Analysis](https://www.dataquest.io/path/python-basics-for-data-analysis/)


<details>
<summary>ToC</summary>

- [@Dataquest: Python Basics for Data Analysis](#dataquest-python-basics-for-data-analysis)
  - [I. Introduction to Python Programming](#i-introduction-to-python-programming)
    - [1. Python Programming](#1-python-programming)
    - [2. Programming Python Variables](#2-programming-python-variables)
    - [3. Python Data Types: Integers, Floats, Strings](#3-python-data-types-integers-floats-strings)
    - [4. Python Lists](#4-python-lists)
  - [II. Basic Operators and Data Structures in Python](#ii-basic-operators-and-data-structures-in-python)
    - [1. Python For Loops](#1-python-for-loops)

</details>

## I. Introduction to Python Programming


### 1. Python Programming

- 1.1 Learning Data Science

> - **Data Science**: field that uses algorithms, scientific methods, and systems to extract knowledge and insights from structured and unstructured data

- 1.2 Programming in Python

```py
print(23 + 7)
```

- 1.3 The `print()` Function

```py
print(0.00 + 6.99)
print(4.5 - 3.5)
```
- 1.4 Python Syntax

```py
# ERROR
print(1) print(2)
```

- 1.5 Computer Programs

```py
print(1.99 + 6.99)
```

- 1.6 Code Comments

```py
# print('foo')
```

- 1.7 Arithmetical Operations

> **PEMDAS**/**BODMAS**

```py
print(1.99 * 2)
print(6.99 / 3)
print(4 ** 2)

print(6.99 + 0.00 * 10)
print((6.99 + 0.00) * 10)
```
- Write a program with three lines of code that performs the following arithmetical operations and displays the results (use the `print()` function to display the results):
  - 16 × 10
  - 48 ÷ 5
  - 5³ (don't type 5^3 because ^ is not the symbol for exponentiation)

```py
print(16 * 10)
print(48 / 5)
print(5 ** 3)
```

- 1.8 Review

### 2. Programming Python Variables

- 2.1 Saving Values

```py
result = 6.99 * 2
print(result)
```

- 2.2 Variables -- computer memory...

```py
minecraft_cost = 6.99
fruit_ninja_cost = 1.99 * 1

print(minecraft_cost)
print(fruit_ninja_cost + 1.99)
print(minecraft_cost + fruit_ninja_cost)
```

- 2.3 Variable Names

```md
- We must use only letters, numbers, or underscores (**we can't use apostrophes, hyphens, spaces, etc.**).
- Variable names can't begin with a number.
> Variable names are case sensitive
```

```py
facebook_rating = 3.5
instagram_rating = 4.5
# facebook-rating = 3.5
# instagram rating = 4.5
```

- 2.4 Updating Variables

```py
app_costs = 1.99
app_costs = app_costs + 6.99
print(app_costs)
```

- 2.5 Syntax Shortcuts

```py
x += y
x -= y
x *= y
x /= y
x **= y
```

```py
rating_count_totals = 698516
rating_count_totals += 522012

fruit_ninja_totals = 1.99
fruit_ninja_totals *= 4

print(rating_count_totals)
print(fruit_ninja_totals)
```

- 2.6 Review

### 3. Python Data Types: Integers, Floats, Strings

- 3.1 Integers and Floats

```py
print(type(0))
print(type(0.0))
# print('foo' + 2)
```

- 3.2 Conversion Between Types

```py
print(float(0))         # 0.0
print(int(1.99))        # 1
print(round(1.49))      # 1
print(round(1.50))      # 2
```

```py
# ...
personal_apps = round(personal_apps)
gift_apps = int(gift_apps)
print(personal_apps)
print(gift_apps)
```

- 3.3 Strings

```py
print(type('AoC'))

app_name = 'Minecraft: Pocket Edition'
average_rating = 4.5
total_ratings = 522012
print(app_name)
```

- 3.4 Escaping Special Characters

```py
motto = "Facebook's old motto was 'move fast and break things'."
print(motto)

motto = 'Facebook\'s old motto was "move fast and break things".'
print(motto)
```

- 3.5 String Concatenation

```py
print('a' + 'b')
print('a' + ' ' + 'b')
print('This' + 'is' + 'a' + 'sentence.')
print('This' + ' ' + 'is' + ' ' + 'a' + ' ' + 'sentence.')

print('a' * 1)      # This will output: a
print('a' * 4)      # This will output: aaaa
print('a ' * 5)     # This will output: a a a a a
print('a' * 0)      # No output for this line
print('a' * -1)     # No output for this line

print('4' + 1)      # This will give an error
print('4' - 1.0)    # This will give an error
```
```py
facebook = "Facebook's rating is"
fb_rating_str = '3.5'
fb = facebook + ' ' + fb_rating_str

print(fb)
```

- 3.6 String Conversion

```py
print(int('4') + 1)         # 5
print(float('3.3') + 1)     # 4.3
print(int('wrong format'))  # ValueError

a = 2
b = 5
print(a+b)                  # 7
print(str(a)+str(b))        # 25
```
```py
facebook = "Facebook's rating is"
fb_rating = 3.5
fb_rating_str = str(fb_rating)

fb = facebook + ' ' + fb_rating_str
print(fb)
```

- 3.7 Multi-line Strings (`'''`)

```py
motto = '''Facebook's old motto was:
'move fast and break things'.
Nice.'''
print(motto)
```

- 3.8 Review


### 4. Python Lists

- 4.1  Storing Row Elements into Variables

```py
track_name_row_2 = 'Instagram'
price_row_2 = 0.0
rating_count_tot_row_2 = 2161558
```

- 4.2 Storing Rows as Lists -- `foo=[x, y]`

```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(row_1)
print(type(row_1))
```

- 4.3 List Lenght -- `len()`

```py
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
empty_row = []

row_2_length = len(row_2)
empty_row_length = len(empty_row)
```

- 4.4 List Indexing
- 4.5 Retrieving Values from Lists -- `foo[3]`

```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(row_1[0])
```
```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]

total = ratings_1 + ratings_2 + ratings_3
average = total / 3
```

- 4.6 Negative Indexing

```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

print(row_1[6])         # IndexError
print(row_1[-1])        # 3.5
print(row_1[4])         # 3.5
```
```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]

total_rating = rating_1 + rating_2 + rating_3
average_rating = total_rating / 3
```

- 4.7 Retrieving Multiple List Elements

```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
insta_rating_data = [row_2[0], row_2[3], row_2[-1]]
minecraft_rating_data = [row_5[0], row_5[3], row_5[-1]]

total_rating = fb_rating_data[-1] + insta_rating_data[-1] + minecraft_rating_data[-1]
average_rating = total_rating / 3
```

- 4.8 List **Slicing** -- `foo[0:3]`


```py
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
​
cc_pricing_data = [row_3[0], row_3[1], row_3[2]]
cc_pricing_data = row_3[0:3] # Syntax shortcut

print(cc_pricing_data)
```
> - Use `a_list[m:n]` to get the slice, where `m` is the index of the first item, and `n` is one more than the index of the last item.
>   - `a_list[:x]` when we want to select the first `x` elements.
>   - `a_list[-x:]` when we want to select the last `x` elements.

```py
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

first_3 = row_3[:3]
last_3 = row_3[-3:]

print(first_3)
print(last_3)
```
```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

last_3_fb = row_1[-3:]
minecraft_3_4 = row_5[2:4]

print(last_3_fb)
print(minecraft_3_4)
```

- 4.9 List of Lists

```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

data_set = [row_1, row_2, row_3, row_4, row_5]
print(data_set)
```

- 4.10 Retrieving from List of Lists

```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

data_set = [row_1, row_2, row_3, row_4, row_5]

# print(data_set[0])  # Shows the first item
# print(data_set[-1]) # Shows the last item
# print(data_set[:2]) # Shows the first two items

# fb_row = data_set[0]   # Gets the first item
# print(fb_row)         # Shows the first item
# fb_rating = fb_row[-1] # Gets the last part of the first item
# print(fb_rating)      # Shows 3.5

print(data_set[0][-1]) # Gets the last part of the first item
```
```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

total_rating = 0

for i in app_data_set:
    total_rating += i[-1]

avg_rating = total_rating / 5

# avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + app_data_set[4][-1]) / 5

print(avg_rating)   # 4.3
```

- 4.11 Review

## II. Basic Operators and Data Structures in Python

### 1. Python For Loops


- 1.1 Repetitive Process

```py
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]
​
app_data_set = [row_1, row_2, row_3, row_4, row_5]
avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] +
              app_data_set[2][-1] + app_data_set[3][-1] +
              app_data_set[4][-1]) / 5
​
print(avg_rating)
```

- 1.2 For Loops

```py
app_ratings = [3.5, 4.5, 4.5, 4.5, 4.5]

for element in app_ratings:
    print(element)
```

- 1.3 For Loops Continued

```py

app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_count = 0

for row in app_data_set:
    rating_count = row[3]
    print(rating_count)
```

- 1.4 For Loop Structure

```py

app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_sum = 0

for row in app_data_set:
    rating_count = row[3]
    rating_sum += rating_count
    print(rating_sum)
```

- 1.5 The Average App Rating

```py
app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_sum = 0

for row in app_data_set:
    rating = row[-1]
    rating_sum += rating

avg_rating = rating_sum / 5
```

- 1.6 Opening a File -- **!!**

> - [Module CSV: `reader` function](https://docs.python.org/3/library/csv.html)
> - **Module**: collection of *functions* and *variables*

```py
from csv import reader

opened_file = open('AppleStore.csv')    # OBJECT
read_file = reader(opened_file)         # OBJECT
apps_data = list(read_file)             # Create list of lists

# print(opened_file)
# print(read_file)

print(len(apps_data))                   # Although there are 7,197 rows (apps) in our dataset, len(apps_data) indicates there are 7,198 rows because it also considers the header row, which describes the column names (the first row).
print(apps_data[0])
print(apps_data[1:2])
```

- 1.7 Other Kinds of Errors
- 1.8 Dealing with Errors

```py
from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = 0
for row in apps_data[1:]:
    # print(type(row[7]))   # <class 'str'>
    rating = float(row[7])
    rating_sum += rating

avg_rating = rating_sum / len(apps_data[1:])    
```

- 1.9 Alternative Method to Calculate an Average -- `list.append()` + `sum()`

```py
from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum = []
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum.append(rating)

avg_rating = sum(rating_sum) / len(rating_sum)
print(avg_rating)
```

- 1.10 Review

> PAID FROM NOW ON

<!-- ### Python If, Else, Elif Statements
### Python If, Else, Elif Statements: MUltiple Conditions
### Python Dictionaries
### Python Dictionaries and Frequency Tables

## Python Functions and Jupyter Notebook

### Python Functions: Using Built-in Functions and Creating Functions
### Python Functions: Arguments, Parameters, and Debugging
### Python Functions:  Built-in Functions and Multiple Return Statements
### Python Functions:  Returning Multiple Variables and Function Scopes
### Project: Project: Learn and Install Jupyter Notebook
### Guided Project: Profitable App Profiles for the App Store and Google Play Markets

## Intermediate Python for Data Science

### Cleaning and Preparing Data in Python
### Python Data Analysis Basics
### Object-Oriented Python
### Working with Dates and Times in Python
### Guided Project: Exploring Hacker News Posts -->
