
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)") # helicopter helicopter~

def get_user_input():
    val = 1
    flag = 14
    num_string = input("")
    global numfltglobal
    num_list = num_string.split(", ")
    num_list_flt = [float(i) for i in num_list]
    numfltglobal = num_list_flt
    #print(num_list_flt)
    return num_list_flt


def calc_average(a):
    sum = 0
    for elem in a:
        sum += elem
    avg = round(float(sum/len(a)), 3)
    return avg

def calc_average_temperature(g):
    sum = 0
    for k in g:
        sum += k
    atemp = round(float(sum/len(g)), 3)
    return atemp


def find_min_max(h):
    minmaxlst = []
    minmaxlst.append(min(h))
    minmaxlst.append(max(h))
    return minmaxlst

def calc_median_temperature(s):
    s.sort()
    print("Sorted: ", s)
    mid = len(s) // 2
    res = (s[mid] + s[~mid]) / 2
    return res

#def calc_median_temperature:





display_main_menu()
print("The average of the numbers you've entered is:", calc_average(get_user_input()))
#display_main_menu()
print("Plot Twist! They're actually temperatures! The average temperature is:", calc_average_temperature(numfltglobal),"degrees Celsius.")
print("Min and Max temperatures are:", find_min_max(numfltglobal),"degrees Celsius respectively.")

print("The median temperature is:", calc_median_temperature(numfltglobal),"degrees Celsius.")
