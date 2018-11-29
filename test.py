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
