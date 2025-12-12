
num=int(input("Enter the number"))
temp_num=num
temp_num_str=str(num)
num_len=len(temp_num_str)

Rem=0
Sum=0
armstrong_sum=0
num_reverse=0
digit_count=0

while(temp_num>0):
    rem=temp_num%10
    #extracting the last digit
    num_reverse=num_reverse*10+rem
    #making the reversed number
    digit_count+=1
    #increment count after the digit
    armstrong_sum+=rem**num_len
    #making the armstrong sum
    temp_num=temp_num//10
    #make the number to(n-1) digits
print("Orginal number    >>>>>",num)
print("Reversed number    >>>>>",num_reverse)
print("number of digits  >>>>>",digit_count)
print("Palindrome Status:>>>>> Yes") if num_reverse==num else print("Palindrome status:>>>>> No")
print("Armstrong Status :>>>>> Yes") if armstrong_sum==num else print("Armstrong status :>>>>> No")



