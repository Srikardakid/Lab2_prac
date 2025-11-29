def calculate_bmi(height,weight):
    print("Height = ", height)
    print("Weight = ", weight)
    bmi = weight/(height*height)
    print("BMI = ", bmi)
    if bmi < 18.5:
        print("You are Underweight")
        return -1
    elif bmi <25:
        print("You are normal weight")
        return 0
    else:
        print("You are overweight")
        return 1

calculate_bmi(1.77,61)