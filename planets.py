def weight_on_planets():
   # write your code here
   weight= int(input("What do you weigh on earth? "))
   weightmars= weight * .38
   weightjupiter= weight * 2.34
   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(weightmars,weightjupiter))
  
   
if __name__ == '__main__':
   weight_on_planets()