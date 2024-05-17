#I declare that my work contains no examples of misconduct,such as palgorism or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID : w1761374

#Date :2020/12/08

action1=True
while action1==True: 
    try:
        action2=True
        
        def Progress(): #DEFINE FUNCTION TO PRINT Progress
            print('progress')
            print("")
        def Trailer():  #DEFINE FUNCTION TO PRINT Trailer
            print('Progress (module Trailer)')
            print("")
        def Retriever(): #DEFINE FUNCTION TO PRINT Retriever
            print('Do not progress-module Retriever')
            print("")
        def Exclude():  #DEFINE FUNCTION TO PRINT Exclude
            print('Exclude')
            print("")

        while action2==True:
            n=[0,20,40,60,80,100,120]
            # p,q,r represents students Pass  credits ,Defer credits and Fail credits
            p=int(input('Please enter your credits at pass:')) #asking user to enter the pass credits
            while p not in n:
                print("Out of range.")
                print("")
                p=int(input('Please enter your credits at pass:'))
                
            q=int(input('Please enter your credits at defer:'))  #asking user to enter the defer credits
            while q not in n:
                print("Out of range.")
                q=int(input('Please enter your credits at defer:'))
                
                
            r=int(input('Please enter your credits at fail:')) #asking user to enter the fail credits

            while r not in n:
                print("Out of range.")
                r=int(input('Please enter your credits at faiil:'))
                
                p+q+r==120
            if p+q+r!=120:
                print("Total incorrect.") #if total is not eqal to 120
                print("")
                continue
            
            elif p==120:
                Progress() #calling the progress function
                
            elif p==100:
                Trailer() #calling the Trailer function
                
            elif p>=0 and p<=80 and q>=0 and q<=120 and r>=0 and r<=60:
                Retriever() #calling the Retriever function
                
            elif p>=0 and p<=40 and q>=0 and q<=40 and r>=80 and r<=120:
                Exclude() #calling the Exclude function
            
            
    except ValueError:
        print('Integers Required')
        print("")
        
    
    
        
                
   
       
            
            
         
        

            
