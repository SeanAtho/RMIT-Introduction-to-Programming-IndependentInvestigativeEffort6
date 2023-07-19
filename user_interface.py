import sys
import backend

#Creation of function for string inputs
def get_str(prompt):
    sys.stdout.write(prompt)
    entered_str= sys.stdin.readline().strip()
    while(entered_str==""):
        sys.stdout.write("Error! Enter valid input: ")
        entered_str = sys.stdin.readline().strip()
    return entered_str
    
#The below function is responsible for displaying the interface to users. 
def main_interface():
    inventory = backend.initialise()
    #The string variable is created and used to store the main interface and
    #menu which indicates the available options to the user.
    #Prevents unnecessary use of stdouts and prints in code blocks. 
    menu=""
    menu+="Dealership Interface\n"
    menu+="====================\n"
    menu+="[L]oad inventory\n"
    menu+="[A]dd Car\n"
    menu+="[D]isplay Car\n"
    menu+="[S]ave inventory\n"
    menu+="E[x]it\n"
    menu+="Choice: "
    
    sys.stdout.write(menu)
    choice=sys.stdin.readline().strip().lower()
    while (choice!="x"):
        sys.stdout.write("\n")
        #If is created to allow for the user to display car inventory file
        if(choice=="l"):
             sys.stdout.write("Load an inventory...\n")
             filename=get_str("Enter filename: ")
             backend.load_inventory(inventory,filename)
        #Elif used for the user's input enables make, model and price of choice to
        #be stored in variable make_model.   
        elif (choice=="a"):
            sys.stdout.write("Adding Car Test...\n")
            make_model = get_str("Enter make and model: ")

            input_ok = False
            #While loop created for checking of price data type.
            while(input_ok == False):
                price_str = get_str("Enter price: ")
                #Try except constructed to for invalid inputs with the appropriate message
                #displayed to the user indicating incorrect input. 
                try:
                    price = float (price_str)
                    input_ok = True
                except:
                    sys.stdout.write("Invalid price! Re Enter: \n")


            backend.add_car(inventory,make_model,price)
        #Elif used to display all cars contained within the inventory,
        #organized with an interface specifying each section.  
        elif (choice=="d"):
            sys.stdout.write("Displaying all Cars...\n")
            summary = backend.get_summary(inventory)
            sys.stdout.write("Make and model\t\tPrice\n")
            sys.stdout.write(summary)
        #Elif to save inventory to file in the programs folder  
        elif (choice=="s"):
            sys.stdout.write("Saving all cars...\n")
            filename=get_str("Enter filename: ")
            backend.save_inventory(inventory,filename)
        #Else used to handle an invalid input from the user following the choice at the main menu.  
        else:
            sys.stdout.write("Invalid Menu Input!\n")

        sys.stdout.write(menu)
        choice=sys.stdin.readline().strip().lower()
    sys.stdout.write("Program finished...\n")

main_interface()
    
