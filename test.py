# def rect_area(a, b):
#     """
#     calculate area of a rectangel
#     """
#     return a*b

# area = rect_area(4,7)
# print("arean är ",area)

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

def work_on_my_own(hp, weeks, hours_scheduled):
    """ 
    calculate hours of own work a week
    """
    hours_total = hp /1.5*40
    hours_own = hours_total - hours_scheduled
    weekly_hours = hours_own / weeks
    return weekly_hours

def main():
    hours =work_on_my_own(6, 7, 50)
    print(hours)
    
    
if __name__ =="__main__":
    main()

