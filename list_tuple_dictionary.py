our_list = [27, 46, -5, "ram", True, 27]
print(our_list)
print(type(our_list))
# list are iterable data types
print(our_list[4])
print(our_list[4:])
print(our_list[:4])
list2 = [27, 46, -5, [4, 5, 'sita', False], "ram", True, 27]
print(list2[3])
print(list2[3][2])
print(list2[3][2:])
our_table = [[1,2,3], [4,5,6], ['ram', 8, 9]]
print(our_table[2])
print(our_table[2][0])
# our_table[row][column]

# adding list to a list
print(our_table)
our_list = our_list + [1]
our_list = our_list + [[1,2,3]]
our_list.append(['append', 'into', 'list'])
our_list = our_list + ["abcd"]
our_list = our_list + list("abcd")
our_table = our_table + our_list

# we can not add string or number or any other data type to the list
# insert in between
our_table.insert(2,['insert', 'into', 'list'])

#list are mutable and strings are immutable
our_table[0] = 4
print(our_table)

#=====================
# tuple are immutable
our_tuple = (1,2,3,'a','b','c')
print(type(our_tuple))
print(our_tuple[0:3])
# tuple = iterable dataypes
(a, b, c) = "mis"
print(a)
(d,e,f) = [4,5,6]
print(f)

# Dictonary
# doesn't have order
stu = {} # empty dictonary
students = {"Bibek": "ASE", "Mahesh": "SE"}
print(students)
print(students.keys())
print(students.values())
a = list(students.keys())
print(a)
print(a[1])
print(students['Bibek'])
students['Bibek'] = 23
print(students['Bibek'])
print(students.items())
del students['Bibek']
print(students)

#dictonary with list
lf ={
  "Bibek": ["ID0001", 23, "ASE"],
  "Mahesh": ["ID002", 20, "SE"]
}
print(lf)
print(lf['Bibek'])
print(lf['Bibek'][2])
print(lf['Bibek'][:2])

#dictonary with dictonary
lf ={
  "Bibek": {"ID": "ID0001", "Age": 23, "P": "ASE"},
  "Mahesh": {"ID": "ID002", "Age": 20, "P": "SE"}
}
print(lf)
print(lf["Mahesh"]["ID"], lf["Bibek"]['P'])