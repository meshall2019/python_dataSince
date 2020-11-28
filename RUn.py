from main_figure_Run_code import *



try:#Run the Program

        print("1.The exploratory data analysis")
        print("2.The figures of exploratory data analysis")
        user_option=int(input("Emter your option number: "))
        if user_option==1:
            EDA()

        elif user_option==2:
            figures_EDA()
            plt.show()
        else:
            print("please enter the correct number!!!")


except:
        print("There is a problem")


