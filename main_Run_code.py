from main_figure import * #from main_figure class


#Run the Program
try:

        print("1.The exploratory data analysis")
        print("2.The figures of exploratory data analysis")
        print("*******-Enter 0 to exit-*******")
        user_option=int(input("Emter your option number: "))
        if user_option==1:
            EDA()
        elif user_option==2:
            figures_EDA()
        else:
            print("please enter the correct number!!!")


except:
        print("There is a problem")


