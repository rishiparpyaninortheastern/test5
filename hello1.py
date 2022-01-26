print("---Welcome to La Casa Hotel---");
dd_price=9000
b_price=4000
d_price=6000

ch=int(input("please enter from the following options:\n1)booking\n2)room_service\n3)order"));


def booking():
    
    print("we have following options\n")
    print("1)Double deluxe room(includes jacuzzi,double bedroom,Seaview)\n")
    print("2)Deluxe room(includes double bedroom,jacuzzi\n")
    print("3)Basic room(includes single bedroom)\n")
    user_input=int(input("enter from the above options"))
    if user_input==1:
        print("you have selected Double deluxe room\n")
        print("The Price for the room is" )
        print(dd_price)
        booking_conf=input("would you like to go ahead with the booking?y/n")
        if booking_conf=='y':
            name=input("enter your name")
            age=input("enter yout age")
            addr=input("enter your address")
            f = open('hotel.txt', 'a')
            f.write(name)
            f.write(age)
            f.write(addr)
            f.write("double deluxe")



            print("congratulations .Your room has been booked")
        else:
             print("Hoping you choose us next time")
    elif user_input==2:
        print("you have selected  deluxe room\n")
        print("The Price for the room is"+d_price)
        booking_conf=input("would you like to go ahead with the booking?y/n")
        if booking_conf=='y':
            count=count+1
            print("congratulations .Your room has been booked")
        else:
             print("Hoping you choose us next time")     

    elif user_input==3:
        print("you have selected basic room\n")
        print("The Price for the room is"+b_price)
        booking_conf=input("would you like to go ahead with the booking?y/n")
        if booking_conf=='y':
            count=count+1
            print("congratulations .Your room has been booked")
        else:
             print("Hoping you choose us next time")  
            
           
            


if ch==1:
    booking()

if ch==2:
    room_service()







    
