
#Creation of function which is used in front end/user interface.
def initialise():
    inventory=[]
    return inventory

#Function used for adding items to the inventory list determined by
#inputs taken from the user.
def add_car(inventory,make_model,price):
    inventory.append([make_model,price])

#A function used to display inventory items back to the user upon
#required input in the interface program.
def get_summary(inventory):
    summary=""
    i=0
    while(i<len(inventory)):
        summary+=inventory[i][0]+"\t"
        summary+=str(inventory[i][1])+"\n"
        i+=1
    return summary

#A function used to display information from a file created by the user.
def load_inventory(inventory,filename):
    file_obj = open(filename,"r")
    line = file_obj.readline()

    line = file_obj.readline()
    while(line!=""):
        fields = line.strip().split("\t")
        inventory.append(fields)
        line = file_obj.readline()
    
    file_obj.close()

#A function used to create and save data to file. 
def save_inventory(inventory,filename):
    file_obj = open(filename,"w")
    summary = get_summary(inventory)
    file_obj.write("Make and model\t\tPrice\n")
    file_obj.write(summary)
    file_obj.close()
