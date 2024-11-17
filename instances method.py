class Mobile:
    def __init__(self,mobile,camera):
        self.mobile=mobile
        self.camera=camera
    def Make_call(self,number):
        return "calling...{}".format(number)
mobile_obj1=Mobile("oneplus ce","64 mp")
print(id(mobile_obj1))
print(type(mobile_obj1))

mobile_obj2=Mobile("samsung","64 mp")
print(id(mobile_obj2))
print(type(mobile_obj2))

