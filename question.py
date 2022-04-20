# a=int(input("enter the number: "))
# b=int(input("Enter the number: "))
# i=1
# total=0
# while i<=b:
#     total+=a
#     i+=1
# print(total)



# a=["n","d"]
# b=int(input("enter the number: "))
# i=1
# while i<=b:
#     j=0
#     while j<len(a):
#         print(a[j],end="")
#         print(i,end=" ")
#         j+=1
#     i+=1





# a=int(input("Enter the number: "))
# if a%2==0 or a%3==0 or a%5==0 or a%7==0 or a%9==0 :
#     print("it is not prime number: ")
# else:
#     print(" prime number: ") 

# a="True" 
# b=False
# print(a+b)

    
# a=int(input("Enter the date: "))
# b=int(input("Enter the month: "))
# c=int(input("Enter the year: "))
# d=int(input("Enter the current date:  "))
# e=int(input("Enter the current month: "))
# f=int(input("Enter the current year: "))

# if a==28 or b==2 or c<10000:
#     print(a+d,"-",b+1,"-",c+f)

#     if b==2:
#         if a+d==29:
#             print(a+d,"-",b+1,"-",c+f)
#     elif b!=2:
#         e=int(input("Enter the current month: ")) 
#         print(a+d,"-",b+e,"-",c+f)
# else:
#     print("error")       



# a={}
# i=0
# n=1
# b=[]
# while n<100:
#     if (n==2 or n==3 or n==5):
#         i+=1
#         b.append(n)
#         a.update({i:n})
#     elif n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 and n%11!=0:
#         i+=1
#         b.append(n)
#         a.update({i:n})
#     n+=1
# print(b)
# print(a)




# a=[1,3,4,5,6,7,8,9,4,32,15,65,98]
# b=[]
# i=0
# while i<len(a):
#     c=a[i]*10
#     b.append(c)
#     i+=1
# print(b)    
    

# 28/03/2009
# a=28
# b=0o3
# c=2009
# print(a,"/",b,"/",c)


# print("my name")
# def num():
#     a=10
#     b=20
#     return a+b
# #     # print(num)
# #     # print("Ddepu")
# # print("Deepanjali")
# print(num())
# print("anjali")





# a=[1,0,0,2,4,0,5,0]
# count=0
# leanght=len(a)
# for i in range(leanght):
#     if a[i]!=0:
#         a[count]=a[i]
#         count+=1
#         # print(count)
#         print(a[i])
# while count<leanght:
#     a[count]=0 
#     count+=1
# print(a)           



# def pushZerosToEnd(arr, n): 
#     count = 0 # Count of non-zero elements 

#     for i in range(n): 
#         if arr[i] != 0: 
        
#             arr[count] = arr[i] 
#             count+=1
#     while count < n: 
#         arr[count] = 0
#         count += 1

 

# def checkHarshad( n ) :
#     sum = 0
#     temp = n
#     while temp > 0 :
#         sum = sum + temp % 10
#         temp = temp // 10
#     # Return true if sum of
#     # digits is multiple of n
#     return n % sum == 0
 
# # Driver Code
# if(checkHarshad(12)) : print("Yes")
# else : print ("No")
 
# if (checkHarshad(15)) : print("Yes")
# else : print ("No")




# a = int(input('Enter number: '))
# copy = a
# digit_sum = 0
# while a:
#     digit_sum += a%10
#     a //= 10
# if copy%digit_sum == 0:
#     print('is Harshad Number',int(copy))
# else:
    # print('is Not Harshad Number',int(copy))

# i=0
# a=[]
# copy=i
# b=0
# while i<=100:
#     b+=i%10
#     i//=10
#     # i+=1
#     print(i)
# if copy%b ==0:
#     a.append(copy)
#     i+=1
# print(a)
# 
# 

# def digitsSum(Number):
#     Sum = rem = 0
#     while Number > 0:
#         rem = Number % 10
#         Sum = Sum + rem
#         Number = Number // 10
#     return Sum

# minHrd = int(input("Enter the Minimum Harshad Number = "))
# maxHrd = int(input("Enter the Maximum Harshad Number = "))

# print("\nThe List of Harshad Numbers from {0} and {1}".format(minHrd, maxHrd)) 
# for i in range(minHrd, maxHrd + 1):
#     Sum = digitsSum(i)
#     if i % Sum == 0:
#         print(i, end = '   ')    

   
# minHrd = int(input("Enter the Minimum Harshad Number = "))
# maxHrd = int(input("Enter the Maximum Harshad Number = "))
# number=1
# Sum = rem = 0
# while Number > 0:
#     rem = Number % 10
#     Sum = Sum + rem
#     Number = Number // 10
# for i in range(minHrd, maxHrd + 1):
#     Sum = i
#     if i % Sum == 0:
#         print(i, end = '   ')    

# [11:26 AM, 3/30/2022] Ankita Gmr: 
# a=[]
# for i in range(1,1001):
#     num=i
#     n=len(str(i))
#     sum1=0
#     i=str(i)
#     for digit in i:
#         sum1=sum1+int(digit)**n
#         if sum1==num:
#             a.append(num)
# print(a)
# [11:26 AM, 3/30/2022] Ankita Gmr: 



# n=int(input("enter the number: "))
# for i in range(n):
#     print('  ',(n-i-1)+"   ",*(i+1))
# for i in range(n-1):
#     print('  ',(i+1)+"   ",*(n-i-1))


# n=int(input("enter"))
# for i in range(n):
#     print('  '(n-i-1),+"   "*(i+1))
# for i in range(n-1):
#     print('  '(i+1),+"   "*(n-i-1))
# s=5
# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         if j<i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#         j=j+1
#     print()
#     s=s+1
#     i=i+1


# char_list=["a","n","j","a","l","i","d","i","v","y","a"]
# i=0
# l=[]
# while i<len(char_list):
#     j=0
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count+=1
#         j+=1
#     if char_list[i] in l:
#         i+=1
#         continue
#     l.append(char_list[i])
#     print(char_list[i],"-",count,"times ")



# a=0.1
# b=0.2
# print(a+b)




# to binary using recursion
# def DecimalToBinary(num):
     
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')
 
# # Driver Code
# if __name__ == '__main__':
     
#     # decimal value
#     dec_val = 46
     
#     # Calling function
#     DecimalToBinary(dec_val)

# num=int(input("enter the number: "))
# if num>=1:
#     num//2
#     print(num%2,end='')




# a=5.1e5
# print(a)


# public void reverseStri{}int left = 0;
#    {int end = s.length-1;
#    while (left < end) {
#       //swap
#       char temp = s[left];
#       s[left] = s[end];
#       s[end] = temp;
      
#       left ++;
#       end --;
#    }
# }


# s = ["h","e","l","l","o"]
# a=[]
# i=0/
# while i<len(s):

# print(s[-1:1])

# i+=1
# 



a=[12,40,34,90,76,80,12]
i=0
while i<len(a):
    if a[i]%10==0:
        