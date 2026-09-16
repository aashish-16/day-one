name = input("enter your name :")
c_name = input("enter your colleg name :")
sem = (input("enter your semester number :"))


with open("data.txt","w") as f:
    f.write(name + "\n")
    f.write(c_name + "\n")
    f.write(sem + "\n")
with open("data.txt","r") as f:
    r = f.read()
    print(r)