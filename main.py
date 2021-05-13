from database import Database



print("*"*20+"Hello Bookshelf Automation"+"*"*20)
print("")



while True:
    print("1/Add\n2/Del\n3/Update\n4/list\n5/Exit")
    control=input("Input=")
    if control=='1':
        Database().book_add()
    elif control=='2':
        Database().book_del()
    elif control=='3':
        Database().book_update()
    elif control=='4':
        print("id,book_name,book_writer,book_star,read_state")
        Database().book_list()
    elif control=='5':
        break
