# def rect_area(a, b):
#     """
#     calculate area of a rectangel
#     """
#     return a*b

# area = rect_area(4,7)
# print("arean är ",area)

##default argument
# def print_person(name="Unknown", age="Secret"):
#     print(name)
#     print(age)
#     return

# print_person("micke", 21)
# print_person("micke")
# print_person(age=21)
# print_person()

# def main():
#     print("main")


# if __name__ =="__main__":
#     main()

# def work_on_my_own(hp, weeks, hours_scheduled):
#     """ 
#     calculate hours of own work a week
#     """
#     hours_total = hp /1.5*40
#     hours_own = hours_total - hours_scheduled
#     weekly_hours = hours_own / weeks
#     return weekly_hours

# def main():
#     hours =work_on_my_own(6, 7, 50)
#     print(hours)

##count letters
# for letter in "Python":
#     print(letter)

# for i, letter in enumerate("Python"):
#     print("Bokstaven", letter, "finns på indexplats", i)

##matris
# rows = 4
# cols = 5
# for i in range(rows):
#     for j in range(cols):
#         print("* ", end = "")
#     print("")

# name = "micke"
# age = 21
# string = f"My name is {name} and my age is {age}"
# print(string)

# res = 100 / 3
# print(f"100 delat med tre är {res:.2}")
# print(f"100 delat med tre är {res:.2f}")
# print(f"100 delat med tre är {res:7.1f}")
# print(f"100 delat med tre är {res:<7.1f}")
# print(f"100 delat med tre är {res:>7.1f}")

#listor

#list_ = []
#list_in_list = [1, [1,2], 2, [3,4]]

#ten_list = list(range(1,11))
#lista på 10 element

#for loop bra med listor
# fruit_list = ["apple", "peach", "cherry"]
# for fruit in fruit_list:
#     print(fruit, "pie")
#len() ger längd på lista

#pets = ["cat", "dog"]
#more_pets = ["spider", "parrot", "fox"]
#all_pets = pets + more_pets #konkatination av listor
#print(all_pets[1:3]) #från index 1 till och med index 2
#.append lägger till element i listan
#"cat" in all_pets #controlera om element finns i listan
#all_pets.sort() #sorterar listan alfbetiskt
#.reverse vänder på listan 
#.pop(i) plockar ut element och returnerar elementet fån index i
#.insert(i,x) lägger till element x på index i
#.remove(x) tar bort första x ur lista

#copy list
#my_list = ["glasses", "phone"]
#youre_list = my_list #skapar alias på samma lista
#my_list.append("keys")
#my_list[:] skapar copia av lista
#youre_list = my_list[:]

#______tupel dictionary_______
#tupel
#cant change tupel
#tupel = ("item1", "item2", "item3")
#med eller itan parenteser
#tupel = (50,)
#must be commas 
#print("tupel[0]", tupel[0])
#same vay as with lists
#konkatination av tupler
#tupel4 = (500,)
#tupel4 = tupel4 + tupel2[2:7]
# nykel ord "del"
#del tupel
#can iterate through tupel

#dictionary
#dicto = {"name": "micke", "age": "21"}
#name is key age is value
#dict[name]
#ndex in dict is meaningless order does not exist
#add value dict[nykel] = value
#dicto["profession"] = "programmer"
#look for value key in dict
#"name" in dicto
#look for value value in dict.values()
#21 in dicto.values()
#dict.keys() give the keys 
#dict.value() give the values
#dict.pop(key) return value and remove
#del dict[key] remove key and value

#controll if elem exist in list recursive
# def cont_elem(elem, lst):
#     if lst == []:
#         return False
#     if lst[0] == elem:
#         return True
#     return cont_elem(elem, lst[1:])

# print(cont_elem(1, []))
# print(cont_elem(1, [2, 3, 1]))
# print(cont_elem(1, [2, 3, 4, 5, 6, 7]))

#copy list
# def lst_copy(lst):
#     if len(lst) == 0:
#         return []
#     result = lst_copy(lst[1:])
#     if type(lst[0]) != list:
#         return [lst[0]] + result
#     else:
#         return [lst_copy(lst[0])] + result

# print(lst_copy([1,[2,3],4,5]))

#högre ordningens funktion funktionell programering
# def with_all(func, seq):
#     if not seq:
#         return []
#     else:
#         return [func(seq[0])] + with_all(func, seq[1:])
# #def inc5(num):
# #    return num + 5
# def increment5(seq):
#     return with_all(lambda n: n + 5, seq)

# #def fist_elem(seq):
# #    return seq[0]

# def fist_element(seq):
#     return with_all(lambda s: s[0] , seq)


# lst1 = [1,2,3,4,5]
# new_lst1 = increment5(lst1)
# print(new_lst1)

# lst2 = [[1,2,3,4], ["a","s","d","r","h"], [[1.3,33.2,5.2], [2,45,3,21]]]
# new_lst2 = fist_element(lst2)
# print(new_lst2)
#lambda funktioner
#funtioner av ett uttryck
#lambda var: funkuttryck
#=
#def name(var):
#   uttryck

#currying - funktion som returnvärde

# def mod_counter(steps):
#     i = 0

#     def next_step():
#         nonlocal i 
#         i = (i + 1) % steps
#         return i
    
#     return next_step

#iteratorer

# lst1 = list(map(lambda n: n+5, [1,2,3,4,5]))
# lst2 = list(range(10, 0, -2))
# lst3 = [53,6,24,5,75,4,32,5,6,34]
# print(list(enumerate(lst3)))
# s_lst = sorted(lst3)
# print(lst1)
# print(lst2)
# print(s_lst)

#list comprehension
#[uttryck for i in seq]
#length of list elem
#[len(s) for s in ["alex", "martin", "fox"]]
#kvadrerar alla fr�n 0 till 10
#[x**2 for x in range(0,10)]
#nestlad for loop
#[(x,y) for x in range(3) for y in range(4)]


#file exep
try:
    file = open("text.txt", "r")

except:
    file = open("test.txt", "w+") #w+ read and write
    #if file dosnt exist create it
