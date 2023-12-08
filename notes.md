# Notes

## `with` statement

- [`with` for exception handling...](https://www.geeksforgeeks.org/with-statement-in-python/)


```py
# file handling

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
	file.write('hello world')
finally:
	file.close()
```
```py
# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')
```

> see `cheat py-read_files`...
