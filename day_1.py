# # # # # # # # # # x = 20
# # # # # # # # # # y = 51
# # # # # # # # # # x*y
# # # # # # # # # # def stupid ():
# # # # # # # # # #     x = 20
# # # # # # # # # #     print (x)
    
# # # # # # # # # # stupid()
# # # # # # # # # # import this
# # # # # # # # # mynumber = 20.234
# # # # # # # # # rounded_num = round(mynumber,2)
# # # # # # # # # print(rounded_num)
# # # # # # # # # num = 22
# # # # # # # # # dem = 7
# # # # # # # # # pi = num/dem
# # # # # # # # # print (pi)
# # # # # # # # # rounded_num = round(pi,3)
# # # # # # # # # print(rounded_num)
# # # # # # # # # namme = "elton John"
# # # # # # # # # phone = 8031346305 * 6
# # # # # # # # # print(phone)
# # # # # # # # # name = 'Elton'
# # # # # # # # # surname = 'john'
# # # # # # # # # fullname = name + ' ' + surname
# # # # # # # # # print(fullname)
# # # # # # # # # day = '20'
# # # # # # # # # month = 'january'
# # # # # # # # # year = '1992'
# # # # # # # # # # print(day +'/'+ month +'/'+ year)
# # # # # # # # # pi = 22/7
# # # # # # # # # statement = 'pi is ' + str(round(pi, 2))
# # # # # # # # # # print(statement)
# # # # # # # # # akara = input ('please how many akara you want? ')
# # # # # # # # # akamu = input ('please how many akamu you want? ')
# # # # # # # # # akara_statement = 'you bought ' + akara + ' akara'
# # # # # # # # # akamu_statement = 'you bought ' + akamu + ' akamu'
# # # # # # # # # print(akara_statement)
# # # # # # # # # print(akamu_statement)#

# # # # # # # # akara = input ('please how many akara you want? ')
# # # # # # # # akamu = input ('please how many akamu you want? ')
# # # # # # # # print ('you ordereded for ', akara,'akara ' + akamu,'akamu')
# # # # # # # # akara_price = 20
# # # # # # # # akamu_price = 50
# # # # # # # # bill_akara =  akara_price * int(akara)
# # # # # # # # bill_akamu =  akamu_price * int (akamu)
# # # # # # # # total =  bill_akara + bill_akamu
# # # # # # # # print(' your bill is ', total)
# # # # # # # name = input ('please enter your name:')
# # # # # # # age = input ('please enter age:')
# # # # # # # p_year = 2019
# # # # # # # year = p_year - int(age)
# # # # # # # comment =f' hello {name} you are {age}, you were born in {year}'
# # # # # # # print(comment)
# # # # # name = input ("Please enter your name: ")
# # # # # age = input ("please enter your age:")
# # # # # present_year = 2019
# # # # # year = present_year - int(age)
# # # # # comment =f" Hello {name} you are {age}, you were born in {year}"
# # # # # print(comment)
# # # # # if (year % 4) == 0:
# # # # #     if (year % 100) == 0:
# # # # #         if (year % 400) == 0:
# # # # #             print("{0} is a leap year".format(year))
# # # # #         else :
# # # # #            print(" {0} is not a leap year".format(year))
# # # # #     else:
# # # # #        print("{0} is a leap year".format(year))
# # # # # else:
# # # # #    print("{0} is not a leap year".format(year))
# # # # name = input ("please enter your name longer than 7 words:")
# # # # print(name[1], name[2], name[-1])
# # # # print(name[0:5])

# # # word = input ('please put in a word ')
# # # legth = input ('what is the lenght of word ')
# # # split = int(int(legth)/2) - 1
# # # spltt = split + 2
# # # first_two = word[0:2]
# # # mid_two = word[split:spltt]
# # # last_two = word[-2: ]
# # # print(word[-1], word[split:])
# # # print(word[0:2]+word[split:spltt]+word[-2: ])
# # # statement = f"{first_two}{mid_two}{last_two}"
# # # # print(statement)
# # # word = "sweet mum"
# # # slice= word[-5::-1]
# # # # print(slice)
# # # mode = 6// 4
# # # print(mode)
# # x=20
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
word = input('please put in your word:')
step = word[::-1]
print(step)
statement = f'{word} is a palindrome'
statementnot = f'{word} is not a palindrome'
if step == word:
    print(statement)
else:
     print(statementnot)
vowels = {"a","e","i","o","u","A","E","I","O","U"}
if vowels in word:
    print('vowel present')
else:
    print('vowel not present')