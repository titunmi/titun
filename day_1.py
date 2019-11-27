# x = 20
# y = 51
# x*y
# def stupid ():
#     x = 20
#     print (x)
    
# # stupid()
# # import this
# mynumber = 20.234
# rounded_num = round(mynumber,2)
# print(rounded_num)
# num = 22
# dem = 7
# pi = num/dem
# print (pi)
# rounded_num = round(pi,3)
# print(rounded_num)
# namme = "elton John"
# phone = 8031346305 * 6
# print(phone)
# name = 'Elton'
# surname = 'john'
# fullname = name + ' ' + surname
# print(fullname)
# day = '20'
# month = 'january'
# year = '1992'
# # print(day +'/'+ month +'/'+ year)
# pi = 22/7
# statement = 'pi is ' + str(round(pi, 2))
# # print(statement)
# akara = input ('please how many akara you want? ')
# akamu = input ('please how many akamu you want? ')
# akara_statement = 'you bought ' + akara + ' akara'
# akamu_statement = 'you bought ' + akamu + ' akamu'
# print(akara_statement)
# print(akamu_statement)#

# akara = input ('please how many akara you want? ')
# akamu = input ('please how many akamu you want? ')
# print ('you ordereded for ', akara,'akara ' + akamu,'akamu')
# akara_price = 20
# akamu_price = 50
# bill_akara =  akara_price * int(akara)
# bill_akamu =  akamu_price * int (akamu)
# total =  bill_akara + bill_akamu
# print(' your bill is ', total)
# name = input ('please enter your name:')
# age = input ('please enter age:')
# p_year = 2019
# year = p_year - int(age)
# comment =f' hello {name} you are {age}, you were born in {year}'
# print(comment)
# name = input ("Please enter your name: ")
# age = input ("please enter your age:")
# present_year = 2019
# year = present_year - int(age)
# comment =f" Hello {name} you are {age}, you were born in {year}"
# print(comment)
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("{0} is a leap year".format(year))
#         else :
#            print(" {0} is not a leap year".format(year))
#     else:
#        print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))
# name = input ("please enter your name longer than 7 words:")
# print(name[1], name[2], name[-1])
# print(name[0:5])

# word = input ('please put in a word ')
# legth = input ('what is the lenght of word ')
# split = int(int(legth)/2) - 1
# spltt = split + 2
# first_two = word[0:2]
# mid_two = word[split:spltt]
# last_two = word[-2: ]
# print(word[-1], word[split:])
# print(word[0:2]+word[split:spltt]+word[-2: ])
# statement = f"{first_two}{mid_two}{last_two}"
# # print(statement)
# word = "sweet mum"
# slice= word[-5::-1]
# # print(slice)
# mode = 6// 4
# print(mode)
# x=20
# # x +=5
# # print(x)
# a = input ('input value for a: ')
# b = input ("input value for b: ")
# inta = (int(a) ** 2)
# intb = (int(b)** 2)
# c =  (inta + intb) ** 0.5
# print(c)
# a = int(input('what\'s is value of a:'))
# b = int(input ("what's value of b:"))
# c = int(input ("what's the value of c:"))
# d = (b**2 - (4*a*c))**0.5
# x1 = (-b + d) / (2*a)
# x2 = (-b - d) / (2*a)
# statement = f'x is either {x1} or {x2}'
# print(statement)
# age = int(input ('Please enter your age : '))

# can_drink = age >= 20
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40
# statement = f"can drink alcohol: {can_drink}\ncan pay tax : {can_pay_tax}\nCan take pension : {can_take_pension}\n Can now Retire :{can_retire}"
# print(statement) 
# word = input('please put in your word:')
# step = word[::-1]
# print(step)
# statement = f'{word} is a palindrome'
# statementnot = f'{word} is not a palindrome'
# if step == word:
#     print(statement)
# else:
#      print(statementnot)
# vowels = {"a","e","i","o","u","A","E","I","O","U"}
# if word in vowels:
#     print('vowel present')
# else:
#     print('vowel not present')
# word = input("Please enter a word : ")
# reversed_word = word[::-1]
# print(f'{reversed_word} and {word} is a palindrome : {word == reversed_word}')
# response = "a" in word or "e" in word or "i" in word or "o" in word or "u" in word
# print (f" {word} contains vowels : {response}")
# word = input('please write a word: ')
# print( 'a' in word)


# a = int(input('input a'))
# b = int (input('input b'))
# c = int (input('input c'))
# d = int (input('input d'))
# numerator = (a*d) + (c*b)
# den = b*d

# x = numerator
# y =  den
# print(f'{x}/{y}')#

# fraction = input('please input your expression: ')
# a = int (fraction[0])
# b = int (fraction[2])
# c = int (fraction[4])
# d = int (fraction[6])
# numerator = (a*d) + (c*b)
# den = b*d
# x = numerator
# y =  den
# print(f'{x}/{y}')

# fraction = input ("please enter enter a fracton in the format 'a/b+c/d' : ")
# splitted_fraction = fraction.split('+')
# frac1 = splitted_fraction[0]
# frac2 = splitted_fraction[1]
# splitted_frac1 = frac1.split('/')
# splitted_frac2 = frac2.split('/')
# a = splitted_frac1[0]
# b = splitted_frac1[1]
# c = splitted_frac2[0]
# d = splitted_frac2[1]

# a = int (fraction[0])
# b = int (fraction[2])
# c = int (fraction[4])
# d = int (fraction[6])
# numerator = (a*d) + (c*b)
# den = b*d
# x = numerator
# y =  den
# print(f'{x}/{y}')


# frac1, frac2 = fraction.split('+')
# a,b,c,d = *frac1.split('/'), *frac2.split('/')
# print(a,b,c,d)

# dob = input ('please enter your date of birth in the format year-month-day: ')
# year = dob.split("-")
# print(year[0])
# print(1,2,3,sep = '\n',end = '-')
# print('newline')
# file = open ('my_data.csv','a')
# print ('name', 'age', 'state', 'due', file=file, sep = ',')
# print('ade', 20 , 'Osunstate', 20000, file =file, sep = ',')

# details = input( 'enter details in the format: name, age, state, due ')
# split_details = details.split(',')
# name, age, state, due = split_details[0], split_details[1], split_details[2],split_details[3]
# print(name,age,state,due)
# print(name, age,state,due, file=file, sep = ',')




# filename = 'gongoaso.csv'
# mode = 'r' #read mode open
# data = open (filename, mode)
# lyrics = data.read()
# print(lyrics)
# filename= 'akingo.csv'
# mode = 'w'#write mode activated
# file = open(filename, mode)
# text = 'akin makes some of the best odds in the land, he would make back the 4.8m he lost'
# file.write(text)
# myrange = range(20, 60,3)
# print(myrange)
# print(type(myrange))
# print(list(myrange))
# print(list(reversed(myrange)))
# x = [1,5,2,3,10,4,0,1,4]
# print (sorted(x))
# print(sorted(x, reverse= True))
# y= list ("abinbolami")
# print (sorted(y))
# mylist = ["saed", "bes", "a", 'checked' "priny"]
# print (sorted (mylist))
# print (sorted (mylist, key = len)) 
# print (sorted (mylist, key = len, reverse = True))
# mydict = dict (a = 20, b = 30)
# print (mydict)
# print (mydict['a'])
# name = 'abimbola'
# print (set(name))

# num = [ 1,2,3,4,5]
# mapped = map ( lambda x : x*2, num)
# print(list(mapped))
# names = ["ade", "john", "ada", "shola"] # 
# mapped = map (lambda x : 'Mr '+ x, names)
# print(list(mapped))

# word = 'SHARP'
# print(any(word))
# print(word.upper())

# word = input('please write a word: ')
# lowerword = word.lower()
# response = "a" in lowerword or "e" in lowerword or "i" in lowerword or "o" in lowerword or "u" in lowerword
# print (f" {word} contains vowels : {response}")
# print( response)
# word = input ('please write a word with pre- suffix: ')
# print (word)
# replaced_word = word.lower()
# replaced_word = word.replace('pre','post')
# print(replaced_word)

# names = ['gem', 'hem','blem','chem']
# mapped = map (lambda x : x.replace('e', 'a'), names )
# print(list(mapped))
# x = [1,3,1,2,2,4]
# mean = sum(x) / len(x)
# print('mean is',(mean))
# mapped = list(map (lambda x : (x - mean), x ))
# print('standard deviation is :', mapped)

# mapped_v = list (map (lambda mapped: mapped**2, mapped))

# d = ( (sum (mapped_v)) / (len(x)-1))
# print('variance is : ', d)

# v =[ 'hello', 'omo', 'baba', 'muko', 'muko']
# join_v = ' -'. join(v)
# print(join_v)


# filename = 'brown_skin_girl.txt'
# mode = 'r'


# data = open ('brown_skin_girl.txt', 'r')# how to open a folder
# lyrics = data.read()
# print (lyrics.find ('Lupita'))# finds a word in a txt
# print(lyrics.count ('skin'))#counts the number of times skin is mentioned
# print(lyrics.count ('Lupita'))
# print(lyrics.count ('africa'))

# names = [{'name':'bola'}, {'shola':'f'}, {'segun':'m'},{'john':'f'}]
# mapped = map [lambda x  : 'Mr '+ x, names]
# print(list(mapped))

# assignment2
# friend1 =int(input ('number of candy for friend 1: '))
# friend2 = int (input ('number of candy for friend 2: '))
# friend3 = int (input ('number of candy for friend 3: '))
# sum_of_candy = friend1 + friend2 + friend3
# each_candy = int(sum_of_candy/3)
# remainder = (sum_of_candy % 3)
# statement = f'number of candy to be shared is : {each_candy}\n number of canied to be crushed : {remainder}'
# print(statement)

# assignment3
# import random
# for x in range(2):
#     print(random.randint(1,6))
# if x is (6,6):
#     print('you win')
# else:
#     print('try again')
# import random
# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# print(dice1, dice2)
# if (dice1 == 6) & (dice2 == 6) :
#     print('yes you won')
# else:
#     print('try again')

# names =[('Ade', 'm'), ('shade','f'), ('john','m'), ('bolu', 'f')]
# raw_saluted_names = map (lambda x: 'Mr ' + x[0] if x[1] =='m' else 'Mrs ' + x[0], names) # Tenary operator
# saluted_names = list (raw_saluted_names)
# print(saluted_names)

# if 'foo' in ['foo', 'bar', 'baz']:
#     print ('outer condition is true')

#     if 10 > 20 :
#         print ('inner condition 1')
    
#     print ('between inner condition')

#     if 10< 20 :
#         print('inner condition 2')
    
#     print ('End of outer condition')

# print('After outer conditon')
# age = int (input ('please input your age: '))
# behaviour = input ('please input good or bad: ')
# if behaviour == 'good':
#     if age < 18 :
#         print('you get a toy')
#     else :
#         print('you get a car')
# else:
#     print('you are left')


# if 'a' in 'bar':
#     print('boo')
# elif 1/0:
#     print: ('this wont happen')
# elif var:
#     print ('this wont run either')
# # age = int (input ('please input your age: '))
# # behaviour = input ('please input good or bad: ')
# # if behaviour == 'good' and age < 18 :
# #     print('you get a toy')
# # if behaviour == 'good' and age > 18:
# #     print('you get a car')
# # if behaviour == 'bad':
# #     print('you are left alone')


# score = int (input ('score in exam: '))
# print('you', 'pass' if score > 50 else 'fail')

# x = 3
# x = ( 'foo' if (x ==1) else ('bar' if (x==2)else ('baz' if (x==3) else ('qux' if (x ==4) else 'quux'))))
# print(x)


question1 = input ('are you okay: ')
if question1 == 'false' :
    question2 = input ('do you have pains: ') 
    if question2 == 'true' :
        question3 = input ('did you sleep well: ')
        if question3 == 'true':
            question4 = input ('have you done hard work: ')
            if question4 == 'false':
                question5 = input('do you have fever: ')
                if question5 == 'true':
                    question6 = input ('are you vomitting: ')
                    if question6 == 'true':
                        print('please see a doctor')
                    else:
                        print ('take some anti malaria')
                else:
                    print('inconclusive see a doctor')
            else:
                print('have some pain killer')
        else: 
            print('try to sleep')
    else:
        print('unable to diagnose now')
else:
    print('please get a life')



