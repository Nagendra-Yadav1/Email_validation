# email=input("Enter Your Email :->")
# flag=0
# flag1=0
# flag2=0
# if len(email)>=6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@")==1):
#             if (email[-4]==".") ^ (email[-3]=="."):
#                 for i in email:
#                     if i==i.isspace():
#                         flag=1
#                     elif i.isalpha():
#                         if i==i.upper():
#                             flag1=1
#                     elif i.isdigit():
#                         continue
#                     elif i=="_" or i=="." or i=="@":
#                         continue
#                     else:
#                         flag2=1
#                 if flag==1:
#                     print("Space is present Your Email") 
#                 elif flag1==1:
#                     print("Upper is present Your Email")
#                 elif flag2==1:
#                     print("Wrong Email")
#                 else:
#                     print("Email Login Successfully")
#             else:
#                 print("dot(.) is not present your email")
#         else:
#             print("Not present @ in your email") 
#     else:
#         print("Your first letter is not alphabet")
# else:
#     print("Wrong Email lenght is less") 



# import re
# email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# user_email=input("Enter Your Email  :->")
# if re.search(email_condition,user_email):
#     print("Right Email")
# else:
#     print("Wrong Email")



