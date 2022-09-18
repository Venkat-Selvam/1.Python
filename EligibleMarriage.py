class ElegibiltyForMarriage():
    def Eligible():
        User_Gender=input("Your Gender:")
        User_Age=int(input("Your Age:"))
        Gender1,Gender2="Male","Female"
        Age=21

        if(User_Gender==Gender1,Gender2)and(User_Age>=Age):
            print("ELIGIBLE")
            result="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            result="NOT ELIGIBLE"
        return result
