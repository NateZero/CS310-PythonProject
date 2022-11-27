def showmenu() : #Display Interface Menu (Funtction)
  print("="*50)
  print("%-13s %s %12s %8s %4s"% ("|","Main Menu","|","Code","|"))
  print("="*50)
  print("%-13s %s %13s %8s %4s"% ("|","Shopping","|","-S01-","|"))
  print("%-12s %s %11s %8s %4s"% ("|","Check Stock","|","-C01-","|"))
  print("%-12s %s %12s %8s %4s"% ("|","All orders","|","-A01-","|"))
  print("%-15s %s %15s %7s %5s"% ("|","Exit","|","-E-","|"))
  print("="*50)

  
def inputmenu() : # Enter word hook showmenu

    menu_check = True # check menu list
    while menu_check : # if true is work loop whiles

        menu = input(str("showmenu : ")).upper()

        if menu == "S" :
            shopping()
            menu_check = False
        elif menu == "C" : #Check Stock
            showmenu()
            menu_check = False
        elif menu == "A" :
            print("Work : inputmenu go to All orders")
            menu_check = False
        elif menu == "E" : #Exit
            print("Work : inputmenu go to Exit")
            menu_check = False



# # #First Function  runtime # # #
               
def shopping() :
    code = []
    with open(r"/content/datalist.txt") as file:
        resource = file.read().splitlines()
    
    print("-"*55)
    print("%-2s %s %-15s %-19s %-2s %s %2s"% ("|","Code","|","Food Menu","|","Price","|"))
    print("-"*55)

    for i in range(len(resource)) : # ดึงเอา txt resource splitlines() 
        
        resource_conlist = resource[i] # แปลง text เป็น List 
        resource_conlist = list(resource_conlist.split(",")) # แปลง text เป็น List
        code.append(resource_conlist[0])

        print("%-3s %-3s %-7s %-27s %-3s %-4s %2s"% ("|",resource_conlist[0],"|",resource_conlist[1],"|",resource_conlist[2],"|"))
        print("-"*55)
    
    order(code)
    
def order(code) : #ฟังชันก์สั่งออเดอร์ พร้อมบอกจำนวน
    input_oder = []
    input_amt = []
    exit = "N"
    while exit != "Y" :
        oder = (input("\nPlease enter your order : "))
        amt = int(input("Please enter the required quantity : "))
        if oder in code :
            code, namefood, price, stock  = stock_oder()
            input_oder.append(oder)
            input_amt.append(amt)
            for i in range(len(code)) :
                if (oder) == (code[i]) :
                    new_stock = int(stock[i]) - amt
                    stock.pop(i)
                    stock.insert(i,new_stock)
                    change_stock(code, namefood, price, stock)
            exit = input("Would you like to order more? [Y/N]: ").upper()
            exit = exit
        else :
            print("Invalid code!!, Please try again")
            exit = "N"
    checkbill(code, namefood, price, stock, input_oder,input_amt)
    
                
def stock_oder() :
    stock = []
    namefood = []
    price = []
    code = []
    
    with open("/content/datalist.txt",'r+') as file:
        resource = file.read().splitlines()
        
        for i in range(len(resource)) : # ดึงเอา txt resource splitlines() 
            resource_conlist = resource[i] # แปลง text เป็น List 
            resource_conlist = list(resource_conlist.split(",")) # แปลง text เป็น List
            code.append(resource_conlist[0])
            namefood.append(resource_conlist[1])
            price.append(resource_conlist[2])
            stock.append(resource_conlist[3])
    return code, namefood, price, stock                  

def change_stock(code, namefood, price, stock ) :
    with open("/content/datalist.txt",'w') as file:
        for i in range(len(code)) : # ดึงเอา txt resource splitlines() 
            file.write("%s%s%s%s%s%s%s\n"% (code[i],',',namefood[i],',',price[i],',',stock[i]))
    
def checkbill(code, namefood, price, stock, input_order,input_amt) :
    print("\n.................................................")
    print("                   BU Restaurant                 ")
    print("                     Receipt                     ")
    print(".................................................")
    print(" Menu                       QTY         Price    ")
    print(".................................................")
    cout = 0
    subtotal = 0
    for i in input_order :
        number = code.index(i)
        print(" %-27s %s %14.1f\n"%(namefood[number],input_amt[cout],float(price[number]) * float(input_amt[cout])))
        subtotal += float(price[number]) * float(input_amt[cout])
        cout += 1
    discount = (subtotal*0.1)
    print(".................................................")
    print("%-38s %7.2f "%("Subtotal", subtotal))
    print("%-38s %7.2f "%("Discount (10%)",-discount))
    print("%-38s %7.2f "%("Tax (7%)", subtotal * 0.07))
    print("%-38s %7.2f "%("Total", subtotal + (subtotal * 0.07)))
    print(".................................................")
    with open("/content/Receipt.txt","a") as outfile :
        outfile.write("\n")
        outfile.write(".................................................\n")
        outfile.write("                   BU Restaurant                 \n")
        outfile.write("                     Receipt                     \n")
        outfile.write(".................................................\n")
        outfile.write(" Menu                       QTY         Price    \n")
        outfile.write(".................................................\n")
        cout = 0
        subtotal = 0
        for i in input_order :
            number = code.index(i)
            outfile.write(" %-27s %s %14.1f\n"%(namefood[number],input_amt[cout],float(price[number]) * float(input_amt[cout])))
            subtotal += float(price[number]) * float(input_amt[cout])
            cout += 1
        discount = (subtotal*0.1)
        outfile.write(".................................................\n")
        outfile.write("%-38s %7.2f \n"%("Subtotal", subtotal))
        outfile.write("%-38s %7.2f \n"%("Discount (10%)",-discount))
        outfile.write("%-38s %7.2f \n"%("Tax (7%)", subtotal * 0.07))
        outfile.write("%-38s %7.2f \n"%("Total", subtotal + (subtotal * 0.07)))
        outfile.write(".................................................")
        
        
           
            
        

            
        


        
#def stock() :





############################################################
showmenu() # First Run times! 1
inputmenu() # First Run times!  2