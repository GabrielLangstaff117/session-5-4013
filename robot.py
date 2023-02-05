

name = "Robot" 
age = 1
Battery = 100
Powered = True

if Powered == True:
    print("hello i am",name , "// i am" ,age, "years old", " // my battery is ",Battery, " %", "// powered on?", Powered)
    print( " 0 for command list")

while Powered == True:

    if Battery <=10:
        print(" / / z ^ z \ \ ")
        print(" \ \  ---  / / ")
        print( " I AM LOW on bbzzbbattry" )
    
    if Battery <= 0:
        print(" / /       \ \ ")
        print(" \ \       / / ")
        print( " Good.. b..zzyyt" )
        Powered == False
        quit()

    Command_List = ["Print : 0","Talk : 1","Charge : 2","Walk : 3 "," Self destuct: 4" ]

    Num = (int(input("number")))
    
    if Num == 0 :
        print(Command_List)

    if Num == 1 :

        print(" / / 0 ^ 0 \ \ ")
        print(" \ \  -_-  / / ")

        print ("hello i am robot, how is your day??")
        print ( " if good press 1    if bad press 2")

        Battery = Battery - 10
        Num = (int(input("number")))

        if Num == 1 :

            print(" / / - ^ - \ \ ")
            print(" \ \  ^-^  / / ")

            print ( "ahh good to hear" )
            Battery = Battery - 10
            print(Command_List)

            
        if Num == 2 :

            print(" / / [] ^ [] \ \ ")
            print(" \ \   T-T   / / ")

            print ( "OHH no " )
            Battery = Battery - 10
            print(Command_List)

    if Num == 2 and Battery <= 101:
        print(" / / 0 ^ 0 \ \ ")
        print(" \ \  T-T  / / ")

        print ( " ZZZTzz Thanks youuss " )

        Battery = Battery + 20
        if Battery >= 10 and Battery < 20:
            print("//                  :")
        if Battery >= 20 and Battery < 30:
            print("////                :")
        if Battery >= 30 and Battery < 40:
            print("//////              :")
        if Battery >= 40 and Battery < 50:
            print("////////            :")
        if Battery >= 50 and Battery < 60:
            print("//////////          :")
        if Battery >= 60 and Battery < 70:
            print("/////////////       :")
        if Battery >= 70 and Battery < 80:
            print("//////////////      :")
        if Battery >= 80 and Battery < 90:
            print("////////////////    :")
        if Battery >= 90 and Battery < 100:
            print("////////////////  :")
        if Battery >= 100 and Battery < 110:
            print("////////////////////:")
            print(Command_List)

    if Num == 2 and Battery >=100:
        print(" / / 0 ^ 0 \ \ ")
        print(" \ \  T-T  / / ")

        print ( " ZZZT I am Full already " )
        if Battery >= 100 and Battery < 110:
            print("////////////////////:")
            print(Command_List)
    
    if Num == 3:
        print(" / / 0 ^ 0 \ \ ")
        print(" \ \  T-T  / / ")

        print ( " i walked to the park do i carry on ( 1 yes   0 no) " )
        Battery = Battery - 15

        Num = (int(input("number")))
        if Num == 1:
                print(" / / ? ^ ? \ \ ")
                print(" \ \  T-T  / / ")
                print( " i found nothing " )
        Battery = Battery - 15

        if Num == 0:
            print(Command_List)

    if Num == 4:
        print(" / / [] ^ [] \ \ ")
        print(" \ \   T-T   / / ")

        print ( "OHH no " )
        print (" a-a-a are you sure??  (y = 1 n 0 0")
        Num = (int(input("number")))
        if Num == 1:
            print ("........................")
            quit
        if Num == 0:
            print(" / / 0 ^ 0 \ \ ")
            print(" \ \  ___  / / ")
            print("THANK YOU!!!!")
            print(Command_List)
            




