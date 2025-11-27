def calculate_bmi(height,weight):
    print("Height = ", height)
    print("Weight = ", weight)
    bmi = weight/(height*height)
    print("BMI = ", bmi)
    if bmi < 18.5:
        print("You are Underweight")
    elif bmi <25:
        print("You are normal weight")
    else:
        print("You are overweight")

calculate_bmi(1.77,61)