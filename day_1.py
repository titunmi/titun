# # # # # x = 20
# # # # # y = 51
# # # # # x*y
# # # # # def stupid ():
# # # # #     x = 20
# # # # #     print (x)
    
# # # # # stupid()
# # # # # import this
# # # # mynumber = 20.234
# # # # rounded_num = round(mynumber,2)
# # # # print(rounded_num)
# # # # num = 22
# # # # dem = 7
# # # # pi = num/dem
# # # # print (pi)
# # # # rounded_num = round(pi,3)
# # # # print(rounded_num)
# # # # namme = "elton John"
# # # # phone = 8031346305 * 6
# # # # print(phone)
# # # # name = 'Elton'
# # # # surname = 'john'
# # # # fullname = name + ' ' + surname
# # # # print(fullname)
# # # # day = '20'
# # # # month = 'january'
# # # # year = '1992'
# # # # # print(day +'/'+ month +'/'+ year)
# # # # pi = 22/7
# # # # statement = 'pi is ' + str(round(pi, 2))
# # # # # print(statement)
# # # # akara = input ('please how many akara you want? ')
# # # # akamu = input ('please how many akamu you want? ')
# # # # akara_statement = 'you bought ' + akara + ' akara'
# # # # akamu_statement = 'you bought ' + akamu + ' akamu'
# # # # print(akara_statement)
# # # # print(akamu_statement)#

# # # akara = input ('please how many akara you want? ')
# # # akamu = input ('please how many akamu you want? ')
# # # print ('you ordereded for ', akara,'akara ' + akamu,'akamu')
# # # akara_price = 20
# # # akamu_price = 50
# # # bill_akara =  akara_price * int(akara)
# # # bill_akamu =  akamu_price * int (akamu)
# # # total =  bill_akara + bill_akamu
# # # print(' your bill is ', total)
# # name = input ('please enter your name:')
# # age = input ('please enter age:')
# # p_year = 2019
# # year = p_year - int(age)
# # comment =f' hello {name} you are {age}, you were born in {year}'
# # print(comment)
name = input ("Please enter your name: ")
age = input ("please enter your age:")
present_year = 2019
year = present_year - int(age)
comment =f" Hello {name} you are {age}, you were born in {year}"
print(comment)
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else :
           print(" {0} is not a leap year".format(year))
    else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
