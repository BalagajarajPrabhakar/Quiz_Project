print("welcom to quiz")
print("please enter the following details")
print("---------menu----------")
print("1.user")
print("2.admin")
z=('1','2')
x=input("enter your opption")
while x not in z:
        print("invalied name")
        x=input("enter your opption")
if x == z[0]:
    name=input("enter your name:")
    Email=input("enter yout E-mail id:")
    while "@" not in Email:
        print("invalide Email id")
        Email=input("enter yout E-mail id:")
    while True:
        print("-------------Menu--------------")
        print("1.start quiz")
        print("")
        print("2.result")
        print("")
        print("3.quit")
        print("")
        c=('1','2','3','4','5','y','b','n')
        m=input("enter your opption:")
        while m not in c:
            print("invalide ")
            m=input("enter your opption:")
        i=1
        if m == c[0]:
            a=('a','b','b','a','a','a','a','b','a','a')
            d=('a','b')
            ss = []
            with open('qu.txt') as s:
                ss = s.readlines()
                tt = []
                with open('opp.txt') as t:
                    tt = t.readlines()
                    i=0
                    ans=0
                    for line in ss:
                        for line in tt:
                            while i < 10:
                                print(str(ss[i]))
                                print(str(tt[i]))
                                aa=input("answer")
                                while aa not in d:
                                    print("invalide answer")
                                    aa=input("answer")
                                if aa == a[i]:
                                    ans = ans + 5
                                
                                i += 1
            with open('res.txt',"a+")as r:
                r.truncate(0)
                r.write('result: \n')
                r.write(str(ans))
                r.write('\nname:\n')
                r.write(str(name))
                r.write('\nemail id:\n')
                r.write(str(Email))
                r.write('\n')
                print("")
                print("")
                print("result",ans)
                print(name)
                print(Email)
                                            
                                            

        if m == c[1]:
            with open('res.txt')as r:
                num = 6
                for n in range(num):
                    rr = r.readline()
                    print(rr)
        if m == c[2]:
            print("bye..........")
            break
if x == z[1]:
    aname=('bala','prabhu','jyo')
    name=input("enter your name:")
    while name not in aname:
        print("invalied name")
        name=input("enter your name:")
    Email="gcg@gmail.com"
           
    while True:
        print("")
        print("-------------Menu--------------")
        print("1.create quiz qustions")
        print("")
        print("2.create quiz opptions")
        print("")
        print("3.start quiz")
        print("")
        print("4.result")
        print("")
        print("5.quit")
        print("")
        c=('1','2','3','4','5','y','N','n','Y')
        m=input("enter your opption:")
        while m not in c:
            print("invalied")
            m=input("enter your opption:")            
        i=1
        if m == c[0]:
            print("welcom to quiz creation")
            yn=input("are you an admin?  y / n")
            while yn not in c:
                print("invalied")
                yn=input("are you an admin?  y / n")
            if (yn == c[5] or yn == c[8]):
                print("welcom to quiz creation")
                print("type your qustions")
                
                with open('qu.txt',"a+")as f:
                    while i != 0:
                        qq = f.write(input(str(i)))
                        f.write('\n')
                        print("would you like add anothe qustion")
                        kk=input("y/n")
                        while kk not in c:
                            print("invalied")
                            kk=input("y / n")
                        if (kk == c[6] or yn == c[7]):
                            break
                            
                        i += 1
            else:
                print("sorry yo cannot insert qustions")
        if m == c[1]:
            print("welcom to opption creation")
            yn=input("are you an admin?  y / n")
            while yn not in c:
                print("invalied")
                yn=input("are you an admin?  y / n")
            if (yn == c[5] or yn == c[8]):
                print("welcom to opption creation")
                print("type your qustions")
                print("type opptions")
                print("formet to type opptions")
                print("eg:a)Aravind Adiga                 b)Arundhati Roy")
                with open('opp.txt',"a+")as g:
                    while i != 0:
                        gg = g.write(input(str(i)))
                        g.write('\n')
                        print("would you like add anothe opptions")
                        kk=input("y/n")
                        while kk not in c:
                            print("invalied")
                            kk=input("y / n")
                        if (kk == c[6] or kk == c[7]):
                            break
                        i += 1
            else:
                print("sorry yo cannot insert opption")
        if m == c[2]:
            a=('a','b','b','a','a','a','a','b','a','a')
            d=('a','b')
            ss = []
            with open('qu.txt') as s:
                ss = s.readlines()
                tt = []
                with open('opp.txt') as t:
                    tt = t.readlines()
                    i=0
                    ans=0
                    for line in ss:
                        for line in tt:
                            while i < 10:
                                print(str(ss[i]))
                                print(str(tt[i]))
                                aa=input("answer")
                                while aa not in d:
                                    print("invalide answer")
                                    aa=input("answer")
                                if aa == a[i]:
                                    ans = ans + 5
                                i += 1
            with open('res.txt',"a+")as r:
                r.truncate(0)
                r.write('result: \n')
                r.write(str(ans))
                r.write('\nname:\n')
                r.write(str(name))
                r.write('\nemail id:\n')
                r.write(str(Email))
                r.write('\n')
                print("")
                print("")
                print("result",ans)
                print(name)
                print(Email)

        if m == c[3]:
            with open('res.txt')as r:
                num = 6
                for n in range(num):
                    rr = r.readline()
                    print(rr)
        if m == c[4]:
            print("bye..........")
            break
                    
     
               

     
     
                    
                  
                  
             
            
          
