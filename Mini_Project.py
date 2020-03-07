email=input("Email bata be")
password=input("Password kaun tera b**p dega")
if "@" in email:
    if email=="admin@mywbut.com" and password=="12345":
        print("Sahi hai")
    elif email=="admin@mywbut.com" and password!="12345":
        print("Koi baat nahi beta. Hota hai")
        password=input("Password phirse bata")
        if password=="12345":
            print("Ab sahi hai")
        else:
            print("Dobara mat dikhna")
    else:
        print("Chal be")
else:
    print("Gawaar")
