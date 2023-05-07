#making the connection between sql and python

import mysql.connector
my=mysql.connector.connect(host='localhost',user='root',password='Bharathram@2')
cu=my.cursor()


#creating the database 
#this program will be executed once. Executing several times gives error.database having same name couldn't be created several times 
# Because of this reason commiting the code from line no 10 to line no 11

# a='create database Inventory_management'
# cu.execute(a)


#creating tables in the inventory_management database
#this program will be executed once. Executing several times gives error. same table couldn't be prepare several times .
#Because of this reason commiting the code from line no 10 to line no 11

mydb=mysql.connector.connect(host='localhost',user='root',password='Bharathram@2',database='Inventory_management1')
cur=mydb.cursor()
#manufacture table
a='CREATE TABLE manufacture(manufacture_id INT AUTO_INCREMENT PRIMARY KEY,product_name VARCHAR(40) NOT NULL,number_of_items_required INT NOT NULL,date_manufactured DATE,is_defective BOOLEAN)'
#goods table
b='CREATE TABLE goods (goods_id INT AUTO_INCREMENT PRIMARY KEY,product_name VARCHAR(50) NOT NULL,date_manufactured DATE,manufacturer VARCHAR(50) NOT NULL)'
#purchase table
c='CREATE TABLE purchase (purchase_id INT AUTO_INCREMENT PRIMARY KEY,store_name VARCHAR(50) NOT NULL,purchase_amount DECIMAL(10, 2),date_purchased DATE,product_name VARCHAR(50) NOT NULL,goods_id INT NOT NULL,FOREIGN KEY (goods_id) REFERENCES goods(goods_id))'
#sales table
d='CREATE TABLE sale (sale_id INT AUTO_INCREMENT PRIMARY KEY,store_name VARCHAR(50) NOT NULL,sale_amount DECIMAL(10, 2),profit_margin DECIMAL(5, 2),date_sold DATE,product_name VARCHAR(50) NOT NULL,goods_id INT NOT NULL,FOREIGN KEY (goods_id) REFERENCES goods(goods_id))'

cur.execute(a)
cur.execute(b)
cur.execute(c)
cur.execute(d)



#inserting data by writing the data in code
#into manufacture table
z1='insert into manufacture (manufacture_id, product_name,number_of_items_required, is_defective,date_manufactured) VALUES (%s,%s,%s,%s,%s)'
a1=(111, 'Red Toy Car', 200, 0,'2023-04-10')
a2=(222, 'Blue Toy Car', 80, 0, '2023-04-12')
a3=(333, 'Wooden Chair',  130, 0, '2023-04-14')
a4=(444, 'Wooden Table',40, 1, '2023-04-16')
cur.execute(z1,a1)
cur.execute(z1,a2)
cur.execute(z1,a3)
cur.execute(z1,a4)

# mydb.commit()
# print('data inserted successfully in manufacture table')

#in goods tables

z2='insert into goods (goods_id,product_name,date_manufactured,manufacturer) VALUES(%s,%s,%s,%s)'
b1=(111, 'red toy car', '2023-04-10','ss export')
b2=(222,'blue toy car', '2023-04-12','abc chan')
b3=(333, 'wooden chair', '2023-04-14','we prepare')
b4=(444,'Wooden Table', '2023-04-16','SS Export')
cur.execute(z2,b1)
cur.execute(z2,b2)
cur.execute(z2,b3)
cur.execute(z2,b4)
mydb.commit()
print('data inserted successfully in goods table')



# #in purchase table
z3='INSERT INTO purchase (purchase_id, goods_id, store_name,date_purchased, purchase_amount,product_name) VALUES(%s,%s,%s,%s,%s,%s)'
c1=(111, 111, 'MyKids', '2023-04-20', 25.00,'red toy car')
c2=(222, 222, 'ORay', '2023-04-22', 20.00,'blue toy car')
c3=(333,333, 'MyCare', '2023-04-24', 30.00,'wooden chair')
c4=(444, 444, 'ORay', '2023-04-26', 50.00,'Wooden Table')
c5=(555, 444, 'MyKids', '2023-04-28', 100.00,'wooden table')
cur.execute(z3,c1)
cur.execute(z3,c2)
cur.execute(z3,c3)
cur.execute(z3,c4)
cur.execute(z3,c5)
mydb.commit()
print('data inserted successfully in goods table')


# #in sales table


z4='INSERT INTO sale (sale_id, goods_id, store_name,date_sold, sale_amount, profit_margin,product_name) values(%s,%s,%s,%s,%s,%s,%s)'
d1=(111, 444, 'MyKids', '2023-05-01', 30.00, 0.20,'red toy car')
d2=(333, 333, 'MyCare', '2023-05-03', 45.00, 0.50,'wooden chair')
d3=(131, 444, 'MyKids', '2023-05-05', 150.00, 0.30,'wooden table')
d4=(999,888,'ORay','2023-04-01',230.00,0.32,'shirt')
cur.execute(z4,d1)
cur.execute(z4,d2)
cur.execute(z4,d3)
mydb.commit()
print('data inserted successfully in goods table')


# Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.

e='delete from (manucfacture inner join purchase inner join goods inner join sale inner join) where manufacture.is_detective=1'
cur.execute(e)
mydb.commit()



# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.

f='UPDATE manufacture SET number_of_items_required = number_of_items_required - purchase.number_of_items_required  FROM purchase INNER JOIN goods ON purchase.goods_id = goods.goods_id INNER JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE manufacture.product_name = red Toy car AND purchase.store_name = MyKids '
cur.execute(f)
mydb.commit()

# Display all the “wooden chair” items that were manufactured before the 1st May 2023. 

g='SELECT * FROM goods INNER JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE manufacture.product_name = wooden Chair AND goods.manufactured_date < 2023-05-01'
cur.execute(g)



# Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.

h='SELECT sale.sale_id, sale.sale_date, sale.sale_price - purchase.purchase_price AS profit_margin FROM( sale INNER JOIN purchase ON sale.purchase_id = purchase.purchase_id INNER JOIN goods ON purchase.goods_id = goods.goods_id INNER JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE manufacture.product_name = Wooden Table AND sale.store_name = MyCare AND manufacture.manufacturer_name = SS Export)'

cur.execute(h)




















#user friendly code fill the data dynamically into the database

#inserting the data into all the tables

#entering into the loop for selection of the loop and inserting data into them

# from 47 line to line no 228 is the code for dynamic insertion



def selection():
    print('enter which entry you want to write....')
    print('----------------------------------------')
    print('give number as input for selection of the table')
    print('------------------------------------------------')
    print('Manufacture table----> 1')
    print('goods table----------> 2')
    print('purchase table-------> 3')
    print('sale table-----------> 4')
    print('-------------------------')
    print('enter 0 for no selection')
    k=int(input('give your input: '))
    try:
        if(k==1):
            print('you selected Manufacture table\n')
            manufacture()
            return 
    except:
        print('Give Proper input:')
    try:
        if(k==2):
            print('you selected goods table: ')
            goods()
            return 
    except:
        print('Give Proper input:')
    try:
        if(k==3):
            print('you selected purchase table: ')
            purchase()
            return
    except:
        print('Give Proper input:')
    try:
        if(k==4):
            print('you selected sale table: ')
            sale()
            return          
    except:
        print('Give Proper input:')
    try:
        if(k==0 or k==" "):
            print('program executed successfully')
            return 
    except:
        print('Give Proper Input')
        
    else:    
        print('give your selection 1/2/3/4')
        selection()
        return
    


#writing the entries in manufacture table as a function


def manufacture():
    query = 'insert into manufacture (manufacture_id, product_name, number_of_items_required, date_manufactured, is_defective) VALUES (%s, %s, %s, %s, %s)'
    values = []
    i = 1

    while (i):
        print('To stop the entries enter space as input\n')

        ma_id = input(f'{i}. manufacture_id: ')

        if ma_id == ' ':
            print('inserting the data into the table is stopped')
            break

        values.append(int(ma_id))
        values.append(input('product_name: '))
        values.append(int(input('number_of_items_required: ')))
        date = input('date_manufactured (dd-mm-yyyy): ')
        values.append(date)
        values.append(bool(input('is_defective (True/False): ')))
        print(values)
        i += 1

    
    cur.executemany(query, [values])
    mydb.commit()
    print('manufacture details inserted successfully')



#writing the entries in goods table as a function
def goods():
    query ='insert into goods(goods_id,product_name,date_manufactured,manufacturer) values(%s,%s,%s,%s)'
    values = []
    i = 1

    while (i):
        print('To stop the entries enter space as input\n')

        go_id = input(f'{i}. goods_id: ')

        if go_id == ' ':
            print('inserting the data into the table is stopped')
            break

        values.append(int(go_id))
        values.append(input('product_name: '))
        date = input('date_manufactured (dd-mm-yyyy): ')
        values.append(date)
        values.append(input('manufacturer: '))
        

        i += 1

    cur.executemany(query, [values])
    mydb.commit()
    print('goods details inserted successfully')




#writing the entries in purchase table as a function
def purchase():
    query='insert into purchase(purchase_id,store_name,purchase_amount,date_purchased,product_name,goods_id,goods_id) values(%s,%s,%s,%s,%s,%s)'

    values = []
    i = 1

    while (i):
        print('To stop the entries enter space as input\n')

        ps_id = input(f'{i}. purchase_id: ')

        if ps_id == ' ':
            print('inserting the data into the table is stopped')
            break

        values.append(int(ps_id))
        values.append(input('store_name: '))
        values.append(int(input('purchase amount: ')))
        date = input('date_purchased (dd-mm-yyyy): ')
        values.append(date)
        values.append(input('product name: '))
        values.append(int(input('goods id: ')))

        i += 1

    cur.executemany(query, [values])
    mydb.commit()
    print('goods details inserted successfully')




#writing the entries in sale table as a function
def sale():
    query='insert into sale(sale_id,store_name,sale_amount,profit_margin,date_sold,product_name,goods_id,goods_id) values(%s,%s,%s,%s,%s,%s,%s)'


    values = []
    i = 1

    while (i):
        print('To stop the entries enter space as input\n')

        sale_id = input(f'{i}. sale_id: ')

        if sale_id == ' ':
            print('inserting the data into the table is stopped')
            break

        values.append(int(sale_id))
        values.append(input('store_name: '))
        values.append(int(input('sale amount: ')))
        values.append(int(input('profit margin: ')))
        date = input('date_sold (dd-mm-yyyy): ')
        values.append(date)
        values.append(input('product name: '))
        values.append(int(input('goods id: ')))

        i += 1

    cur.executemany(query, [values])
    mydb.commit()
    print('goods details inserted successfully')



coding_with_sql_and_python = selection()
