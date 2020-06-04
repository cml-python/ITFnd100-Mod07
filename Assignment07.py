# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Structured Error Handling Work while
#              Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):

# cleung, 5.30.2020, Created script with Lab 06-03
# cleung, 6.1.2020, Tried to add pickling
# cleung, 6.1.2020, Added pickling as well as error handling
# ---------------------------------------------------------------------------- #
import pickle

# -- data -- #
strFileName= "AppData.dat"
value1= ""
value2= ""
e= ""

# -- Input/Output -- #
while(True):
    value1 = float(input("Enter Value 1: "))
    value2 = float(input("Enter Value 2: "))

    def DivideValues(value1, value2):
        return float(value1 / value2)

    def save_data_to_file(file_name, list_of_data):
        file = open(file_name, "ab")
        pickle.dump(list_of_data, file)
        file.close()

    def read_data_from_file(file_name):
        file = open(file_name, "rb")
        list_of_data = pickle.load(file)
        file.close()
        return file

# -- processing code -- #
    try:
        divide= float(value1/value2)
    except ValueError:
        print('Invalid character. Please enter a number.')
    except ZeroDivisionError:
        print('Divisor cannot equal zero. Please enter a valid divisor.')
    except Exception as e:
        print('Something went wrong.')
        print("Python Built-In error message:", (e))
    else:
        print("The Quotient of %.2f and %.2f is %.2f" % (value1, value2, DivideValues(value1, value2)))
        break

# -- presentation code -- #
list_of_data= [value1, value2, DivideValues(value1,value2)]
save_data_to_file(strFileName,list_of_data)
print(read_data_from_file(strFileName))