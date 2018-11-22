#1,4
# m= 45
# s=20
# sec=m*60
# km=20
# print(m, s, ", is ", sec+s, "sec" )
# mi=km/1.609344
# print(km, "km är", mi, "miles" )

#1,5
# tal1=float(input("mata in ett tal"))
# tal2=float(input("mata in ett tal"))
# print("summan är ",tal1+tal2)

#1.6
# import time
# year=int(input("what year were you born?"))
# month=str(input("what month?"))
# day=int(input("what day?"))
# age=2018-year
# print("OK! you will turn ", age+1, " on ",month , day, "2019")

#1.6.2
# import time
# year=int(input("what year were you born?"))
# month=int(input("what month?"))
# day=int(input("what day?"))
# age=int((((((time.time()/60)/60)/24)/365)+1970))-year
# print("OK! you are", age, " years old ", month, "month and " , day, "days")

#1.7
# sec=int(input("how many seconds"))
# hours=sec//3600
# minutes=(sec-hours*3600)//60
# seconds=sec-hours*3600-minutes*60
# print(sec, " seconds are ",hours,"hours, ",minutes,"minutes and ",seconds,"seconds")

#1.8
# def plus(x_value, y_value):
#     dif=x_value+y_value
#     return dif
# x=int(input("value x"))
# y=int(input("value y"))
# result=plus(x,y)
# print(result)

#1.9
# def minus(x_value, y_value):
#     dif=x_value-y_value
#     return dif
# x=int(input("value x"))
# y=int(input("value y"))
# result=minus(x,y)
# print(result)

#1.10
# def mean(x_value, y_value):
#     return (x_value+y_value)/2

# x=int(input("value x"))
# y=int(input("value y"))

# result=mean(x,y)
# print(result)

#1.11
# celsius=float(input("temp cesius "))
# fahrenheit=((celsius*9)/5)+32
# print("det är ", fahrenheit, "grader fahrenheit")

#1.12
#weight=float(input("youre weight (kg)"))
#height_cm=int(input("youre height (cm)"))
#height_m=height_cm/100
#BMI=weight/pow(height_m, 2)
#print("your BMI is ", BMI)

#1.13
#def percent(value, total):
 #   procent=(value/total)*100
 #   return procent

#value1=float(input("value of "))
#total1=float(input("the total "))
#pcent=percent(value1, total1)
#print(pcent)

#1.14
#import math
#def pythagoras(a,b):
#    c=math.sqrt(pow(a, 2) + pow(b, 2))
#    return c

#opp=float(input("side 1 of the triangel"))
#adj=float(input("side 2 of the triangel"))
#hyp=pythagoras(opp, adj)
#print(hyp)

#1.15
#def unit(int_num):
#   ental=int_num%10
#   return ental

#def ten(int_num):
#    tal=int_num%100
#    ten=tal//10
#    return ten

#num=int(input("input a number "))
#print("ental ", unit(num), "ten ", ten(num))

#1.16
#def swap_units_and_tens(int_num):
#    ten_unit=int_num%100
#    num=int_num-ten_unit

#    unit=ten_unit//10
#    ten_ten=ten_unit%10
#    ten=ten_ten*10

#    whole_num=num+ten+unit
#    return whole_num

#num=int(input("type a number"))
#swap_num=swap_units_and_tens(num)
#print("input", num, "output", swap_num) 

#1.17
#bol=input("Do you like ice cream (Y/N)?")
#if bol in ["y", "Y"]:
#    print("Yay! me to")
#elif bol in ["n", "N"]:
#    print("BOO!")
#else:
#    print("ERROR")

#1.18
#num=int(input("Write a number "))
#div=int(input("write a number "))
#if num%4==0:
#    print(num, " is a multiple of 4")
#elif num%2==0:
#    print(num, " is Even!")
#else:
#    print(num, " is Odd!")
#quo=num%div
#if quo==0:
#    print("No leftovers")
#else:
#    print("Leftovers")

#1.19
#def max2(num1, num2):
#    if num1>num2:
#        result=num1
#    elif num2>num1:
#        result=num2
#    else:
#        result=num1
#    return result
#int_num1=int(input("Write a number"))
#int_num2=int(input("Write a number"))
#int_num=max(int_num1, int_num2)
#print(int_num, "Is biggest")

#i.20
#def max3(num1, num2 ,num3): 
#    if (num1>num2) and (num1>num3) or (num1==num2) and (num1>num3):
#        result=num1
#    elif (num2>num1) and (num2>num3) or (num2==num3) and (num2>num1):
#        result=num2
#    elif (num3>num1) and (num3>num2) or (num1==num3) and (num3>num2):
#        result=num3
#    else:
#        result=num1
#    return result

#int_num1=int(input("Write a number"))
#int_num2=int(input("Write a number"))
#int_num3=int(input("Write a number"))

#num=max3(int_num1, int_num2, int_num3)
#print(num, " Is Biggest")

#1.21
#def is_isoscelese(x, y, z):
#    if x<=0 or y<=0 or z<=0:
#        iso=False
#    else:
#        if x==y or x==z or y==z or x==y==z:
#           iso=True
#        else:
#            iso=False
#   return iso

#num1=int(input("Write a number"))
#num2=int(input("Write a number"))
#num3=int(input("Write a number"))
#triangel=is_isoscelese(num1, num2, num3)
#print(triangel)

#1.22
#import time

#def age(use_age):
#    cur_year=time.time()//(3.2*pow(10, 7))+1970
#    if use_age<1900 or use_age>cur_year:
#        year=False
#        print("Wrong year")
#    else:
#        year=True

#name1=input("Whats youre name ")
#year1=int(input("Year of birth "))
#age(year1)

#name2=input("Whats youre name ")
#year2=int(input("Year of birth "))
#age(year2)

#age1=time.time()//(3.2*pow(10, 7))+1970-year1
#age2=time.time()//(3.2*pow(10, 7))+1970-year2

#if age1>age2:
#    print(name1, age1, " Is older than ", name2, age2)
#elif age2>age1:
#    print(name2, age2, " Is older than ",name1, age2)
#else:
#    print(name1, age1, " and ", name2, age2, " are the same age")

#1.23
#import random
#rng=random.randrange(1,5)
#print("Find the number")

#while True:
#    num=int(input("write anumber"))
#    if num==rng:
#        print("congratulations you found it")
#        break
#    else:
#        print("Try again")

#1.25
#import random
#def dice():
#    rng=random.randrange(1,6)
#    return rng

#player1=input("Enter your name player 1 ")
#player2=input("Enter your name player 2 ")

#player_dice1=dice()
#player_dice2=dice()

#print(player1, ", your dice shows ", player_dice1, "\n", player2, ", your dice shows ", player_dice2)
#if player_dice1>player_dice2:
#    print(player1, "won!")
#elif player_dice1<player_dice2:
#    print(player2, "won!")
#else:
#    print("It's a draw")

#1.26
#def introduce(name="unknown", age="secret"):
#    print("My name is", name, ". My age a is", age)

#introduce("Micke", 19)
#introduce("Micke")
#introduce()

#1.30
#a
#for i in range(0, 26):
#    print(i)
#    i=i+1
#print("\n")
#b
#for j in reversed(range(26)):
#    print(j)
#print("\n")
#c
#for k in range(0, 31):
#    if k%2==0:
#        print(k)
#print("\n")
#d
#sum1=0
#for l in range(37, 150):
#    sum1+=l
#    l=l+1
#print(sum1)
#print("\n")
#e
#int_num_start=int(input("start of range "))
#int_num_end=int(input("end of range "))
#sum2=0
#for m in range(int_num_start, int_num_end+1):
#    sum2+=m
#    m=m+1
#print(sum2)

#1.31
#i=None
#while i!="x":
#    if i!="x":
#        i=input("Press x to exit ")
#    else:
#        break

#1.32
#2.2
#def count_e(word):
#    count = 0
#    e = "e"
#    for i in range(len(word)):
#        if e == word[i]:
#            count += 1
#    return count

#2.3
#def count_char(string, char):
#    count = 0
#    for i in range(len(string)):
#        if char == string[i]:
#            count += 1
#    return count

#2.4
#def substring(string, substr):
#    count = 0
#    for i in range(len(string)):
#        if substr[j] == string[i]:
#            j+=1

#2.5
# def get_char(string, pos):
#    let = "0"
#    if pos <= len(string):
#        for i in range(pos):
#            let = string[i]
#    else:
#        print("invalid position")
#    return let

#2.6


#2.7
# loop = True
# while loop:
#    word = input("Write a word")
#    ln = len(word)
#    letf = 1
#    for i in range(len(word)):
#        let1 = get_char(word, letf)
#        let2 = get_char(word, ln)
#        print(let1, "", let2)
#        ln -= 1
#        letf += 1
#        if let1.lower() == let2.lower():
#            pal = True
#        else:
#            pal = False
#    if pal == True:
#        print(word, "is a palindrome")
#    else:
#        print(word, "is not a palindrome")

#2.8
#fin = open("word.txt")
#for line in fin:
#    sent = line.strip()
#    print(sent)

#2.9
# def write_to_file(file_name, num):
#     fout = open (file_name, "w")
#     for i in range(1, num + 1):
#         for j in range(1, 10):
#             multi = i * j
#             line = str(i) + " * " + str(j) +" = "+ str(multi) + "\n" 
#             line2 = f"{i} * {j} = {multi}\n"
#             fout.write(line2)
#     fout.close()

# write_to_file("a.txt", 9)
# write_to_file("b.txt", 6)

#2.10

