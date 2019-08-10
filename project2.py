booknames=["c","c++","java","spring","ds"]
authornames=["sangeetha","oliver","saravanan","mythreye"]
bd=dict()
ad=dict()
list2 = []
list3=[]
def most_frequent(List): 
    return max(set(List), key = List.count) 

def student():
    print("Welcome Student")
    print("Enter book/author Type \n 1.Book \n 2.Author")
    userdata=input("Enter Choice")
    if(userdata=="1"):
        userbook=input("Enter book")
        for x in  booknames:
            if x==userbook:
                list2.append(x)
    elif(userdata=="2"):
        userauthor=input("Enter Author")
        for i in  authornames:
            if i==userauthor:
                list3.append(i)
def choice():
    print("Do you want to continue yes/no")
    inp=input("Enter choice")
    if inp=="yes" or inp=="y":
        student()
        choice()
    else:admin1()
def admin1():
    print("Welcome Admin")
    print("1->no of user  \n 2.Max search book 3.Max search Author")
    print(list2)
    print("Maximum books searched",most_frequent(list2))
    print("Maximum Authors searched",most_frequent(list3))

def welcome():
    print("Enter User Type \n admin \n student")
    user=input("Enter user")
    if user=="admin":
        un=input("Enter Username")
        pwd=input("Enter password")
        if(un=="admin" and pwd=="niit"):
            admin1()
    elif user=="student":
        student()
        choice() 
    
welcome()   


'''print ([i for i in range(len(list1)) if list1[i]==1 ])
def sum1(tup1):
	a,b = tup1
	c = a+b
	return c

list1.sort(key=sum1)
print (list1)
           '''


