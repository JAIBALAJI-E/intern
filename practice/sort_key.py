d = {"c":3, "a":1, "b":2}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(), key=lambda x: x[1])))

#nested dictionary
students = {
    101: {"name":"JB", "age":20},
    102: {"name":"Ravi", "age":21}
}

print(students[101]["name"])

#dict Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)

#zipping
keys = ["a","b"]
values = [1,2]
print(dict(zip(keys, values)))
