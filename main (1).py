
def calculate_bmi(weight, height):
  bmi = weight / (height ** 2)
  return bmi

# Function to determine BMI category
def bmi_category(bmi):
  if bmi < 18.5:
      return "Underweight"
  elif 18.5 <= bmi < 24.9:
      return "Normal weight"
  elif 25 <= bmi < 29.9:
      return "Overweight"
  else:
      return "Obesity"

# Taking user input
try:
  weight = float(input("Enter your weight in kg: "))
  height = float(input("Enter your height in meters: "))
  bmi = calculate_bmi(weight, height)
  category = bmi_category(bmi)

  print(f"Your BMI is: {bmi:.2f}")
  print(f"Category: {category}")

except ValueError:
  print("Please enter valid numbers for weight and height.")
      


