class HealthToolKit:
    def fit_check(self):
        while True:
            try:
                self.height = float(input("Enter your height: "))
                self.weight = float(input("Enter your weight: "))
                break
            except:
                print("Invalid Input. Try Again!")
        calculated_BMI = self.weight / self.height**2
        print("Your calculated BMI is: ", round(calculated_BMI))
        if calculated_BMI <= 18.5:
            print("UnderWeight")
        elif calculated_BMI >= 18.5 and calculated_BMI <= 24.9:
            print("HealthyWeight")
        elif calculated_BMI >= 25.0 and calculated_BMI <= 29.9:
            print("OverWeight")
        else:
            print("Obese")
    def age_wise(self):
        while True:
            try:
                self.year = int(input("Enter your Birth-Year: "))
                break
            except:
                print("Invalid Input. Try Again!")
        from datetime import date
        current_year = date.today().year
        current_age = current_year - self.year
        print(f"You are {current_age} years old. ")
    def weight_ideal(self):
        while True:
            try:
                self.height = float(input("Enter your height in cm: "))
                self.gender = input("Enter your gender. Press 'M' = male or Press 'F' = female: ").upper()
                if self.gender == "M":
                    self.ideal_weight = 50 + 0.9 * (self.height - 152)
                elif self.gender == "F":
                    self.ideal_weight = 45.5 + 0.9 * (self.height - 152)
                else:
                    print("Invalid gender Input.")
                    continue
                break
            except ValueError:
                print("Invalid Input. Try Again.")
        print(f"Your ideal body weight is approximately {round(self.ideal_weight)} kg")
    def pulse_guard(self):
        while True:
            try:
               self.systolic = float(input("Enter your systolic pressure (top number): "))
               self.diastolic = float(input("Enter your diastolic pressure (bottom number): "))
               break
            except ValueError:
                print("Invalid Input. Try Again!")
        if self.systolic > 180 or self.diastolic > 120:
            self.bp_category = "Hypertensive Crisis - Consult a doctor immediately"
        elif self.systolic >= 140 or self.diastolic >= 90:
            self.bp_category = "High Blood Pressure (Stage 2)"
        elif self.systolic >= 130 or self.diastolic >= 80:
            self.bp_category = "High Blood Pressure (Stage 1)"
        elif self.systolic >= 120 and self.diastolic < 80:
            self.bp_category = "Elevated"
        elif self.systolic < 120 and self.diastolic < 80:
            self.bp_category = "Normal"
        else:
            self.bp_category = "Uncategorized - please double check your values"
        print(f"Your blood pressure category is: {self.bp_category}")
    def birthday_countdown(self):
        from datetime import date
        while True:
            try:
                self.birth_month = int(input("Enter your birth month (1-12): "))
                self.birth_day = int(input("Enter your birth day (1-31): "))
                today = date.today()
                self.next_birthday = date(today.year, self.birth_month, self.birth_day)
                break
            except ValueError:
                print("Invalid Input. Try Again!")
        today = date.today()
        if self.next_birthday < today:
            self.next_birthday = date(today.year + 1, self.birth_month, self.birth_day)
            self.days_left = (self.next_birthday - today).days
        if self.days_left == 0:
            print("🎉 Happy Birthday! Today's the day!")
        else:
            print(f"There are {self.days_left} days left until your next birthday.")
    def selection_to_do(self):
        while True:
            print("Welcome To Our Health Mate! <3 ")
            print("Press 0 to exit.")
            print("Press 1 for Fit-Check.")
            print("Press 2 to Check-Age.")
            print("Press 3 to check Ideal-Weight.")
            print("Press 4 to check Pulse-Guard.")
            print("Press 5 to check no. of days until your Birthday <3")
            while True:
                try:
                    self.choice = int(input("Enter your choice: "))
                    break
                except :
                    print("Please Choose Option Between 0 and 5")
            if self.choice == 1 :
                self.fit_check()
            elif self.choice == 2 :
                self.age_wise()
            elif self.choice == 3 :
                self.weight_ideal()
            elif self.choice == 0:
                print("Are you sure to exit?\n" , "(Yes/No)")
                a = input("Your choice here: ").lower()
                if a == "no":
                    continue
                else:
                    print("Exited")
                    return
            elif self.choice == 4 :
                self.pulse_guard()
            elif self.choice == 5:
                self.birthday_countdown()
            else:
                print("Option not available yet.")
            while True:
                print("Press 'E' to exit and 'M' to return to options dashboard : ")
                b = input("Enter your choice: ").upper()
                if b == "E":
                    exit()
                elif b == "M":
                    continue
                else:
                    print("Invalid Input! Select only 'E' or 'M'.")







o = HealthToolKit()

o.selection_to_do()
