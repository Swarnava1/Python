class Dadddu:
    obj="hookah"
    def smoke(self):
        print("Gud gud gud")

class Mummy:
    def advice(self):
        print("Parhai karo")


class Papa:

    car="Nano"

    def drive(self):
        print("Wooooooohhhh Woooohhhhh")
    def advice(self):
        print("Mat parho")

class Pappu(Mummy,Papa):

    bicycle="Hero"

    def bi_drive(self):
        print("Khatar khatar")

    def advice(self):
            print("chill")


bunty=Pappu()

#bunty.bicycle
#bunty.car
#bunty.drive()

#bunty.smoke()#

bunty.advice()