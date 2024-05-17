#I declare that my work contains no examples of misconducted ,such as palgorism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID : w1761374

#Date : 2020/12/08

Progress_Count=0
Trailer_Count=0
Retriever_Count=0
Exclude_Count=0
total=0


#lists of list
value=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

def histogram():
    print()
    print("Histogram") 
    print("Progress",Progress_Count," :","*"*Progress_Count)
    print("Trailer",Trailer_Count,"  :","*"*Trailer_Count)
    print("Retriever",Retriever_Count,":","*"*Retriever_Count)
    print("Excluded",Exclude_Count," :","*"*Exclude_Count)
    print(total," outcomes in total.")




def Progress(): #DEFINE FUNCTION TO PRINT Progress
    print('Progress')
def Trailer(): #DEFINE FUNCTION TO PRINT Trailer
    print('Progress (module Trailer)')
def Retriever():  #DEFINE FUNCTION TO PRINT Retriever
    print('Do not progress-module Retriever')
def Exclude():    #DEFINE FUNCTION TO PRINT Exclude
    print('Exclude')
  
for x in value:
     p=x[0]
     q=x[1]
     r=x[2]

     if p==120:
         Progress()  #calling the progress function
         Progress_Count+=1
     elif p==100:
         Trailer()   #calling the Trailer function
         Trailer_Count+=1
     elif p>=0 and p<=80 and q>=0 and q<=120 and r>=0 and r<=60:
         Retriever()  #calling the Retriever function
         Retriever_Count+=1
     elif p>=0 and p<=40 and q>=0 and q<=40 and r>=80 and r<=120:
         Exclude()   #calling the Exclude function
         Exclude_Count+= 1
     total+= 1
    
histogram()
      
        
