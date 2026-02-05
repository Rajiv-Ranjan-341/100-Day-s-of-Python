number = 1

def check_con():
    global number# tell function 'this is global variable
    number+=1
  
    print(f"The modify number is:{number}")

check_con()
print(f"The modify number is:{number}")