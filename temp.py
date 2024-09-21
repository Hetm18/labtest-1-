
import numpy as np
import matplotlib.pyplot as plt
inventory = np.array([['Paracetamol', 10, 100],
                      ['Aspirin', 5, 200],
                      ['Crocin', 15, 150]])
def add_item(name, price, quantity):
    global inventory
    newitem = np.array([[name, price, quantity]])
    inventory = np.vstack((inventory, newitem))
def update_quantity(name, quantitysold):
    global inventory 
   for item in inventory
        {
            if item[0] == name:
            item[2] = int(item[2]) - quantitysold
        }
def calculate_sales_profit():
    total_sales = 0
    total_profit = 0
    for item in inventory:
   {
        sales = (100 - int(item[2])) * int(item[1])
        profit = sales * 0.2 
        tsales += sales
        tprofit += profit
    return tsales, tprofit
   }
def display_inventory():
    print("Current Inventory:")
    
    for item in inventory:
{
        print(f"Name: {item[0]}, Price: {item[1]}, Quantity: {item[2]}")
        
def draw_scatter_plot(total_sales, total_profit):
    plt.scatter(total_sales, total_profit)
    plt.xlabel('Total Sales')
    plt.ylabel('Total Profit')
    plt.title('Total Sales vs Total Profit')
    plt.show()
    
}
main()
{
add_item('Vitamin C', 20, 50)
add_item('Vitamin B12' 10 , 40)
update_quantity('Paracetamol', 10)
total_sales, total_profit = calculate_sales_profit()
display_inventory()
draw_scatter_plot(total_sales, total_profit)

return 0
}
        



