print("welcom to quiz")
print("please enter the following details")
name=input("enter your name:")
Email=input("enter yout E-mail id:")
print("")
print("begin quiz")
print("")
q=(' Which among the following was the first Indian woman who went into space?','Who was the first Indian to go to space?',' Who among the following was the first man to climb Mount Everest without supplemental oxygen?',' Who built the Jama Masjid?','Who wrote the Indian National Anthem?','Who was the first Indian Scientist to win a Nobel Prize?','Who is the first Indian to win a Nobel Prize?','Who was the first Indian woman to win the Miss World Title?','Who was the first President of India?','Who was the first Indian to win the Booker Prize?')
print(q[0])
a=('Kalpana Chawla','Sunita Williams')
print(a)
aa=input("answer")
if aa==a[0]:
    ans1=5
else:
    ans1=0
print(q[1])
a=('Ravish Malhotra','Rakesh Sharma')
print(a)
aa=input("answer")
if aa==a[1]:
    ans2=5
else:
    ans2=0
print(q[2])
a=('Duncan Chessell','Phu Dorji')
print(a)
aa=input("answer")
if aa==a[1]:
    ans3=5
else:
    ans3=0
print(q[3])
a=('Shah Jahan',' Akbar')
print(a)
aa=input("answer")
if aa==a[0]:
    ans4=5
else:
    ans4=0
print(q[4])
a=('Rabindranath Tagore',' Bakim Chandra Chatterji')
print(a)
aa=input("answer")
if aa==a[0]:
    ans5=5
else:
    ans5=0
print(q[5])
a=('C.V Raman','Hargobind Khorana')
print(a)
aa=input("answer")
if aa==a[0]:
    ans6=5
else:
    ans6=0
print(q[6])
a=('Rabindranath Tagore','CV Raman')
print(a)
aa=input("answer")
if aa==a[0]:
    ans7=5
else:
    ans7=0
print(q[7])
a=('Diya Mirza','Reita Faria')
print(a)
aa=input("answer")
if aa==a[1]:
    ans8=5
else:
    ans8=0
print(q[8])
a=('Dr. Rajendra Prasad','Zakir Hussain')
print(a)
aa=input("answer")
if aa==a[0]:
    ans9=5
else:
    ans9=0
print(q[9])
a=('Aravind Adiga','Arundhati Roy')
print(a)
aa=input("answer")
if aa==a[0]:
    ans10=5
else:
    ans10=0

    
    
    
    
    
result=(ans1+ans2+ans3+ans4+ans5+ans6+ans7+ans8+ans9+ans10)
print(name)
print(Email)
print("your result:",result)
