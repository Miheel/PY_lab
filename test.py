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
