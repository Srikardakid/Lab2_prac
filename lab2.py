def main():
    print("ET0735 is a devops module ")
    display_main_menu()
    num_list = get_user_data()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5,6,7)")
def calc_average(y):
    avg = sum(y)/len(y)
    print(avg)  
def get_user_data():
    x = input()
    y = x.split(',')
    arr = []
    for z in y:
        arr.append(float(z))
    return arr
def find_min_max(y):
    min_val = min(y)
    max_val = max(y)
    print("Minimum:", min_val)
    print("Maximum:",max_val)
def sort_temperature(y):
    sort = sorted(y)
    print(sort)



if __name__ =="__main__":
    main()

    
