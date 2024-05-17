#I declare that my work contains no examples of misconduct,such as palgorism or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID : w1761374

#Date :2020/12/08

print("Staff Version with Histogram")
print("")

action1=True
while action1==True:
    try:
        action2=True
        
        def Progress(): #DEFINE FUNCTION TO PRINT Progress
            print('Progress')
        def Trailer():  #DEFINE FUNCTION TO PRINT Trailer
            print('Progress-module Trailer')
        def Retriever():   #DEFINE FUNCTION TO PRINT Retriever
            print('Do not progress-module Retriever')
        def Exclude():    #DEFINE FUNCTION TO PRINT Exclude
            print('Exclude')
        n=[0,20,40,60,80,100,120]
        #count progresses ,Trailers ,Retrievers and Excludes

        Progress_Count=0 
        Trailer_Count=0 
        Retriever_Count=0
        Exclude_Count=0
        
        while action2==True:
            n=[0,20,40,60,80,100,120]
            # p,q,r represents student pass credits,Defer credits and Fail credits
            p=int(input('Enter your total PASS credits:')) #asking user to enter the pass credits
            while p not in n:
                print("Out of range")
                p=int(input('Enter your total PASS credits:'))
                
            q=int(input('Enter your total DEFER credits:'))  #asking user to enter the defer credits
            while q not in n:
                print("Out of range")
                q=int(input('Enter your total DEFER credits:'))
                
            r=int(input('Enter your total FAIL credits:')) #asking user to enter the fail credits
            while r not in n:
                print("Out of range")
                r=int(input('Enter your total FAIL credits:'))
                
                p+q+r==120
            if p+q+r!=120:
                print("Total incorrect")#if total is not eqal to 120
                
            elif p==120:
                Progress()  #calling the progress function
                Progress_Count+=1
            elif p==100:
                Trailer()   #calling the Trailer function
                Trailer_Count+=1
            elif p>=0 and p<=80 and q>=0 and q<=120 and r>=0 and r<=60:
                Retriever()   #calling the Retriever function
                Retriever_Count+=1
            elif p>=0 and p<=40 and q>=0 and q<=40 and r>=80 and r<=120:
                Exclude()   #calling the Exclude function
                Exclude_Count+= 1
            

            print("")
            print("Would you like to enter another set of data?")
            #you can enter y without q to continue programme
            q=input("Enter 'y' for yes or 'q' to quit and view results:")
            if q=='q':
                
               progressions=['Progress','Trailer','Retriever','Exclude']
               print('  '.join(progressions))
               for h in range(max(Progress_Count,Trailer_Count,Retriever_Count,Exclude_Count)):
                   print("{0:10}   {1:10}  {2:6}  {3}".format(
                       '*' if h < Progress_Count else ' ',
                       '*' if h < Trailer_Count else ' ',
                       '*' if h < Retriever_Count else ' ',
                       '*' if h < Exclude_Count else ' ',end=' '
                      
                    ))
            print("")             
                      
            
            action1=False
            
                        
    except ValueError:
        print('Integers Required')
        action1=True
    
        
                
   
       
            
            
         
        

            
