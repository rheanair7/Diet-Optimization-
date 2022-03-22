import pulp as plp
import pandas as pd
from openpyxl import load_workbook
global tot
# Read only the nutrition info not the bounds/constraints
def calculations(choice,body_type):

    df = pd.read_excel("C:/Users/vedik/Desktop/Vedzita/NMIMS MPSTME/Subjects/Sem 3/Group project/Code_dataset.xlsx",sheet_name=choice,nrows=33)
    df1 = pd.read_excel("C:/Users/vedik/Desktop/Vedzita/NMIMS MPSTME/Subjects/Sem 3/Group project/Code_dataset.xlsx", sheet_name=choice+"_req",nrows=33)


    # Create a list of the food items
    df = df.fillna(0)
    food_items = list(df['Name'])

    calories = dict(zip(food_items, df['Calories (kcal)']))
    fat = dict(zip(food_items, df['Total Fat (g)']))
    carbs = dict(zip(food_items, df['Carbohydrates (g)']))
    total_sugar = dict(zip(food_items, df['Total Sugar (g)']))
    protein = dict(zip(food_items, df['Protein (g)']))
    total_fat = dict(zip(food_items, df['Total Fat (g)']))
    saturated_fat = dict(zip(food_items, df['Saturated Fat (g)']))
    Monounsaturated_Fat = dict(zip(food_items, df['Monounsaturated Fat (g)']))
    Polyunsaturated_Fat = dict(zip(food_items, df['Polyunsaturated Fat (g)']))
    fiber = dict(zip(food_items, df['Total Fiber (g)']))
    Vitamin_B6 = dict(zip(food_items, df['Vitamin B6 (mg)']))
    Vitamin_A = dict(zip(food_items, df['Vitamin A (IU)']))
    Vitamin_C = dict(zip(food_items, df['Vitamin C (mg)']))
    # Vitamin_D = dict(zip(food_items, df['Vitamin D (IU)']))
    Vitamin_E = dict(zip(food_items, df['Vitamin E (IU)']))
    Vitamin_K = dict(zip(food_items, df['Vitamin K (ug)']))
    Thiamin = dict(zip(food_items, df['Thiamin (mg)']))
    Riboflavin = dict(zip(food_items, df['Riboflavin (mg)']))
    Niacin = dict(zip(food_items, df['Niacin (mg)']))
    Folate = dict(zip(food_items, df['Folate (ug)']))
    Pantothenic_Acid = dict(zip(food_items, df['Pantothenic Acid (mg)']))
    Choline = dict(zip(food_items, df['Choline (mg)']))
    Calcium = dict(zip(food_items, df['Calcium (g)']))
    Copper = dict(zip(food_items, df['Copper (mg)']))
    Iron = dict(zip(food_items, df['Iron (mg)']))
    Magnesium = dict(zip(food_items, df['Magnesium (mg)']))
    Manganese = dict(zip(food_items, df['Manganese (mg)']))
    Phosphorus = dict(zip(food_items, df['Phosphorus (g)']))
    Selenium = dict(zip(food_items, df['Selenium (ug)']))
    Zinc = dict(zip(food_items, df['Zinc (mg)']))
    # prob += plp.lpSum([costs[i] * food_vars[i] for i in food_items])
    # thin woman index= 29

    print(food_items)
    prob = plp.LpProblem("Simple_Diet_Problem", plp.LpMinimize)
    food_vars = plp.LpVariable.dicts("", food_items, lowBound=0, cat='Continuous')
    print(food_vars)
    prob += plp.lpSum([calories[i] * food_vars[i] for i in food_items])
    prob += plp.lpSum([carbs[f] * food_vars[f] for f in food_items]) >= df1.loc[0, body_type], "carbsMinimum"
    prob += plp.lpSum([total_sugar[f] * food_vars[f] for f in food_items]) >= df1.loc[
        1, body_type], "total_sugarMinimum"
    prob += plp.lpSum([protein[f] * food_vars[f] for f in food_items]) >= df1.loc[2, body_type], "proteinMinimum"
    prob += plp.lpSum([total_fat[f] * food_vars[f] for f in food_items]) >= df1.loc[3, body_type], "total_fatMinimum"
    prob += plp.lpSum([saturated_fat[f] * food_vars[f] for f in food_items]) >= df1.loc[
        4, body_type], "saturated_fatMinimum"
    prob += plp.lpSum([Monounsaturated_Fat[f] * food_vars[f] for f in food_items]) >= df1.loc[
        5, body_type], "Monounsaturated_FatMinimum"
    prob += plp.lpSum([Polyunsaturated_Fat[f] * food_vars[f] for f in food_items]) >= df1.loc[
        6, body_type], "Polyunsaturated_FatMinimum"
    prob += plp.lpSum([fiber[f] * food_vars[f] for f in food_items]) >= df1.loc[7, body_type], "fiberMinimum"
    prob += plp.lpSum([Vitamin_B6[f] * food_vars[f] for f in food_items]) >= df1.loc[8, body_type], "Vitamin_B6Minimum"
    prob += plp.lpSum([Vitamin_A[f] * food_vars[f] for f in food_items]) >= df1.loc[9, body_type], "Vitamin_AMinimum"
    prob += plp.lpSum([Vitamin_C[f] * food_vars[f] for f in food_items]) >= df1.loc[10, body_type], "Vitamin_CMinimum"
    # prob += plp.lpSum([Vitamin_D[f] * food_vars[f] for f in food_items]) >= df1.loc[11, body_type], "Vitamin_DMinimum"
    prob += plp.lpSum([Vitamin_E[f] * food_vars[f] for f in food_items]) >= df1.loc[12, body_type], "Vitamin_EMinimum"
    prob += plp.lpSum([Vitamin_K[f] * food_vars[f] for f in food_items]) >= df1.loc[13, body_type], "Vitamin_KMinimum"
    prob += plp.lpSum([Thiamin[f] * food_vars[f] for f in food_items]) >= df1.loc[14, body_type], "ThiaminMinimum"
    prob += plp.lpSum([Riboflavin[f] * food_vars[f] for f in food_items]) >= df1.loc[15, body_type], "RiboflavinMinimum"
    prob += plp.lpSum([Niacin[f] * food_vars[f] for f in food_items]) >= df1.loc[16, body_type], "NiacinMinimum"
    prob += plp.lpSum([Folate[f] * food_vars[f] for f in food_items]) >= df1.loc[17, body_type], "FolateMinimum"
    prob += plp.lpSum([Pantothenic_Acid[f] * food_vars[f] for f in food_items]) >= df1.loc[
        18, body_type], "Pantothenic_AcidMinimum"
    prob += plp.lpSum([Choline[f] * food_vars[f] for f in food_items]) >= df1.loc[19, body_type], "CholineMinimum"
    prob += plp.lpSum([Calcium[f] * food_vars[f] for f in food_items]) >= df1.loc[20, body_type], "CalciumMinimum"
    prob += plp.lpSum([Copper[f] * food_vars[f] for f in food_items]) >= df1.loc[21, body_type], "CopperMinimum"
    prob += plp.lpSum([Iron[f] * food_vars[f] for f in food_items]) >= df1.loc[22, body_type], "IronMinimum"
    prob += plp.lpSum([Magnesium[f] * food_vars[f] for f in food_items]) >= df1.loc[23, body_type], "MagnesiumMinimum"
    prob += plp.lpSum([Manganese[f] * food_vars[f] for f in food_items]) >= df1.loc[24, body_type], "ManganeseMinimum"
    prob += plp.lpSum([Phosphorus[f] * food_vars[f] for f in food_items]) >= df1.loc[25, body_type], "PhosphorusMinimum"
    prob += plp.lpSum([Selenium[f] * food_vars[f] for f in food_items]) >= df1.loc[26, body_type], "SeleniumMinimum"
    prob += plp.lpSum([Zinc[f] * food_vars[f] for f in food_items]) >= df1.loc[27, body_type], "ZincMinimum"
    prob.solve()
    ltvalue=[]
    ltname=[]

    print("Status:", plp.LpStatus[prob.status])
    for v in prob.variables():
        if v.varValue > 0:
            print(v.name, "=", round(v.varValue, 2))
            ltvalue.append(v.varValue)
            ltname.append(v.name)
            zipped= dict(zip(ltname,ltvalue))

    print(zipped)


    df2 = pd.DataFrame.from_dict(zipped, orient='index',columns=['Values'])


    print(df2)

    obj = plp.value(prob.objective)
    print("The total calories of this balanced diet is: {} cal".format(round(obj, 2)))
    food_integer = plp.LpVariable.dicts("Food", food_items, 0, cat='Integer')
    calories_row={'Values':obj}
    df2.append(calories_row,ignore_index=True)
    df2.insert(1,choice+"_calories",obj)
    print(df2)
    df2.to_excel('code_output.xlsx')
def main():

    height=float(input("Enter your Height (in cms):"))/100
    weight= float(input("Enter your  Weight (in kg):"))
    print(type(weight))
    sex=input("Enter your Sex (F/M):")
    bmi = weight / (height ** 2)
    meal_plan=input("Do want to see individual meal plan? Enter (Y/N)").lower()

    if meal_plan=='y':
        choice = input("Enter the meal (Breakfast/Lunch/Dinner)").lower()

        if sex == 'F' or 'f':
            if 0 < bmi <= 18.5:
                body_type = "thin"

            elif 18.5 < bmi <= 30:
                body_type = "normal"

            else:
                body_type = "obese"

        else:
            if 0 < bmi <= 18.5:
                body_type = "thinm"

            elif 18.5 < bmi <= 30:
                body_type = "normalm"

            else:
                body_type = "obesem"

        calculations(choice, body_type)
    else:
        if sex == 'F' or 'f':
            if 0 < bmi <= 18.5:
                body_type = "thin"

            elif 18.5 < bmi <= 30:
                body_type = "normal"
                print(body_type)
            else:
                body_type = "obese"

        else:
            if 0 < bmi <= 18.5:
                body_type = "thinm"

            elif 18.5 < bmi <= 30:
                body_type = "normalm"

            else:
                body_type = "obesem"

        choice="breakfast"
        calculations(choice, body_type)
        choice="lunch"
        calculations(choice, body_type)
        choice="dinner"
        calculations(choice, body_type)
print("hello")
main()