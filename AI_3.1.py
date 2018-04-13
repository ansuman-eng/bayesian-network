from random import choice
from pyknow import *


class Restaurant(Fact):
    """Info about the traffic light."""
    pass


class Recommend(KnowledgeEngine):
    @Rule(Restaurant(v="000"))
    def fun1(self):
        print("Yummpys")

    @Rule(Restaurant(v="001"))
    def fun2(self):
        print("Bits and Bytes")

    @Rule(Restaurant(v="002"))
    def fun3(self):
        print("Rajendra Dhaba")

    @Rule(Restaurant(v="010"))
    def fun4(self):
        print("Santosh")

    @Rule(Restaurant(v="011"))
    def fun5(self):
        print("Viceroy")

    @Rule(Restaurant(v="012"))
    def fun6(self):
        print("Elephant")

    @Rule(Restaurant(v="020"))
    def fun7(self):
        print("Momo kitchen")

    @Rule(Restaurant(v="021"))
    def fun8(self):
        print("Alankrita")

    @Rule(Restaurant(v="022"))
    def fun9(self):
        print("Celebrity")

    @Rule(Restaurant(v="100"))
    def fun10(self):
        print("BPHC Cafteria")

    @Rule(Restaurant(v="101"))
    def fun11(self):
        print("Banjara foods")

    @Rule(Restaurant(v="102"))
    def fun12(self):
        print("Leo's Food Court")

    @Rule(Restaurant(v="110"))
    def fun13(self):
        print("Chinatown")

    @Rule(Restaurant(v="111"))
    def fun14(self):
        print("Swagat Grand")

    @Rule(Restaurant(v="112"))
    def fun15(self):
        print("The Coffee Cup")

    @Rule(Restaurant(v="120"))
    def fun16(self):
        print("The Second Cup")

    @Rule(Restaurant(v="121"))
    def fun17(self):
        print("Mess 1 BPHC")

    @Rule(Restaurant(v="122"))
    def fun18(self):
        print("Aahar Express")




print("WELCOME TO RESTAURANT RECOMMENDATION SYSTEM")
print("Please answer the questions in the given format.")
veg=-1
sit=-1
cost=-1
while(not(veg=='0' or veg=='1')):
    veg=input("Would you prefer an all veg-restaurant? (1 for Yes, 0 for No)\n")
    if(veg!='0' and veg!='1'):
        print("Please enter a valid input")
    
    
while(not(sit=='0' or sit=='1' or sit=='2')):
    sit=input("Would you like to sit down and eat, or a buffet, or a take-away? (0,1,2 in that order)\n")
    if(sit!='0' and sit!='1' and sit!='2'):
        print("Please enter a valid input")
    

while(not(cost=='0' or cost=='1' or cost=='2')):
    cost=input("What cost range will you prefer? (0 for low, 1 for medium, 2 for high)\n")
    if(cost!='0' and cost!='1' and cost!='2'):
        print("Please enter a valid input")
    





pref=veg+sit+cost
engine = Recommend()
engine.reset()
engine.declare(Restaurant(v=pref))
engine.run()
