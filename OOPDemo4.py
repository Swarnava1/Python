class Something:
    def __init__(self):
        self.a="use karle"
        self._b = "Mat use kar"
        self.__c= "use"

    def _x(self):
        print("wrwrrww")

    def __y(self):
        print("gwgwgwgw")

obj=Something()

print(obj.a)
print(obj._b)
print(obj._Something__c)
