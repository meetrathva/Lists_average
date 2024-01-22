list = [10,20,30,40,50]
x = len(list)
s = 0
for i in range(0,x):
    s += list[i]
avg = s/x
fh = open("4_avg_listnos.txt","w")
fh.write("The average of given list is: ")
fh.write(str(avg))
fh.close()