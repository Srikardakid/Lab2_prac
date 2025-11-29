def main():
    print("ET0735 is a devops module ")
    display_main_menu()
    num_list = get_user_data()
    print("Average", calc_average(num_list))
    print("[Minimum,Maximum]",find_min_max(num_list))
    sort_temperature(num_list)
    print("Median:", calc_median_temp(num_list))
def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5,6,7)")
def calc_average(y):
    avg = sum(y)/len(y)
    return avg  
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
    return [min_val,max_val]
def sort_temperature(y):
    sort = sorted(y)
    print(sort)
def calc_median_temp(y):
    if len(y)%2 == 0:
       x =  (y[int(len(y)/2)]+y[int(len(y)/2-1)])/2
    else: 
       x = y[int(len(y)/2)]
    return x




if __name__ =="__main__":
    main()

    
