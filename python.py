print('Hello, Django girls!')
if 3 > 2:
    print("it is true!")
else:
    print("3 is not greater")

name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')



volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
   print("My ears are hurting! :(")


def hi():
    print("hi there!")
    print("how are you?")

hi()

def hi(name):
    if name == "ranju":
        print("hi ranju")
    elif name == "Sonja":
        print("hi sanju")
    else:
        print("hi anonymous")


hi(name)

hi("hari")

def hi(name):
    print ("hello" + name + "!")

girls = ["rita", "shrijan", "sonam", "sarita"]
for name in girls:
    hi(name)
    print("next cuti girl")


for i in range(1, 6):
    print(i)