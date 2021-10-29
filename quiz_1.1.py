print("welcom to quiz")
print("please enter the following details")
name=input("enter your name:")
Email=input("enter yout E-mail id:")
while "@" not in Email:
     print("invalide Email id")
     Email=input("enter yout E-mail id:")    
print("")
print("begin quiz")
print("")
q=('Which among the following was the first Indian woman who went into space?','Who was the first Indian to go to space?',' Who among the following was the first man to climb Mount Everest without supplemental oxygen?',' Who built the Jama Masjid?','Who wrote the Indian National Anthem?','Who was the first Indian Scientist to win a Nobel Prize?','Who is the first Indian to win a Nobel Prize?','Who was the first Indian woman to win the Miss World Title?','Who was the first President of India?','Who was the first Indian to win the Booker Prize?')
o=('a)Kalpana Chawla b)Sunita Williams','a)Ravish Malhotra b)Rakesh Sharma','a)Duncan Chessell b)Phu Dorji','a)Shah Jahan b)Akbar','a)Rabindranath Tagore b)Bakim Chandra Chatterji','a)C.V Raman b)Hargobind Khorana','a)Rabindranath Tagore b)CV Raman','a)Diya Mirza b)Reita Faria','a)Dr. Rajendra Prasad b)Zakir Hussain','a)Aravind Adiga b)Arundhati Roy')
a=('a','b','b','a','a','a','a','b','a','a')
c=('a','b')
ans=0
i=0
while i < 10:
    print(str(q[i]))
    print(str(o[i]))
    aa=input("answer")
    while aa not in c:          
        print("invalide answer")
        aa=input("answer")
       
    if aa == a[i]:
        ans = ans + 5        
    
    i += 1
print("")
print("")
print("result:",ans)
print("Name :",name)
print("Email ID :",Email)
