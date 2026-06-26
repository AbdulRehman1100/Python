i = 100
while (i > 0):
    print(i)
    i -= 7
    # if(i < 50):
    #     break
    if(i < 20):
        continue
    print("This will print till number is greater than 20")
else:
    print("This will print when the loop is finished")