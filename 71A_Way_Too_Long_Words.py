# Create a variable "n" that consists number of lines with one word in each line.
n = int(input())
#Now create a loop to take n lines of input
for i in range(n):
    #Now take user's input
    s = input()
    #Now, create a structure of the output
    out = s[0] + str(len(s) - 2) + s[-1]
    if len(s) > 10:
        print(out)
    else:
        print(s)



        #created by:- Sujay Hazra