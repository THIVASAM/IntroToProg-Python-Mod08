# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Thivanka Samaranayake,June 07 2020,Modified code to complete Product Class
# Thivanka Samaranayake,June 08 2020,Modified code to complete File Processor Class
# Thivanka Samaranayake,June 09 2020,Modified code to complete IO Class
# Thivanka Samaranayake,June 10 2020,Modified code to complete Main Body of the program
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = "products.txt"
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ThivankaS,June07,Added product class
    """
    pass
    # TODO: Add Code to the Product class (DONE)
    # -- Constructor __
    def __init__(self, product_name: str, product_price: float):
        # --Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # Product Name
    @property
    def product_name(self):
        return  str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception ("Names cannot be numbers")

        # Product Name
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric() == True:
            self.__product_name = value
        else:
            raise Exception("Product price cannot be letters")

    # -- Methods --
    def __str__(self):
        return self.product_name + "," + str(self.product_price)

    def to_String(self):
         return self.__str__()

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ThivankaS, June08,Modified code to complete assignment 8
    """
    # -- Save Data Method --
    def write_data_to_file(file_name, lstOfProductObjects):
        if str(file_name).isnumeric() == False:
            objFile = open(file_name, "w")
        else:
            raise Exception ("File name cannot be numbers")
        for row in lstOfProductObjects:
            objFile.write(str(row) + "\n")
        # objFile.close()
        return lstOfProductObjects

    # -- Read Data Method --
    def read_data_from_file(self, file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return: (list) of dictionary rows
        """
        with open(file_name, 'r') as file:
            return file.read()

    # pass
    # TODO: Add Code to process data from a file (DONE)
    # TODO: Add Code to process data to a file (DONE)

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring (DONE)
    """Inputs and outputs data:

    methods:
    print_menu() -- shows menu to user
    input_yes_no_choice(message) -- get user choice
    print_current_Product_in_list(list_of_rows) -- show the current data from the file to user
    input_new_product_and_price() -- get product data from user

    changelog:
    Thivanka Samaranayake, June08 2020, Created Class
    """
    pass
    # TODO: Add code to show menu to user (DONE)
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show existing products in list
        2) Add a new product
        3) Exit Program
        ''')
        print()  # Add an extra line for looks
    # TODO: Add code to get user's choice (DONE)
    @staticmethod
    def input_yes_no_choice():
        """ Gets a yes or no choice from the user

        :return: string
        """
        choice = str(input("What option from the menu would you like to perform? ")).strip()
        return choice

    # TODO: Add code to show the current data from the file to user (DONE)
    @staticmethod
    def print_current_Product_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current products are: *******")
        for row in list_of_rows:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user (DONE)
    @staticmethod
    def input_new_product_and_price():
        product_name = str(input("What is the product? ")).strip()  # Get Task
        if product_name.isnumeric():
            raise Exception("Please enter product name as text")
        product_price = float(input("What is the price? "))  # Get priority
        return product_name, product_price
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body (DONE)
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
while(True):
    IO.print_menu() # Shows menu to user
    strChoice = IO.input_yes_no_choice()

    if strChoice.strip() == '1':
        IO.print_current_Product_in_list(lstOfProductObjects) # Show the current data in the list
        continue

    elif strChoice.strip() == '2':
        strProduct, strPrice = IO.input_new_product_and_price()
        objP1 = Product(strProduct, strPrice)
        lstOfProductObjects = [objP1]
        FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
        continue

    elif strChoice == '3':
        print("Goodbye")
        break


