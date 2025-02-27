class BMI:

    def __init__(self,gender,Weight,height,age):

        self.age = age
        self.gender = gender
        self.Weight = Weight
        self.height = height

    def BMR(self):

        if self.gender == '남자':

            Bmr = 66.47 + (13.75 * self.Weight) + (5 * self.height) - (6.76 * self.age)
            
        elif self.gender == '여자':

            Bmr = 65.51 + (9.56 * self.Weight) + (1.85 * self.height) - (4.68 * self.age)

        else:
            print("성별을 잘못 입력하셨습니다. 다시 입력하세요.")
        
        return Bmr

b = input("성별를 입력해주세요 : ")
c = int(input("몸무게를 입력해주세요 : "))
d = int(input("키를 입력해주세요 : "))
e = int(input("나이를 입력해주세요 : "))

bmi = BMI(b,c,d,e)
bmr = bmi.BMR()
print("기초대사량 : ",bmr)
print("")


class Exercise(BMI):

    def __init__(self, exercise_selection, time, level):
        self.exercise_selection = exercise_selection
        self.time = time
        self.level = level

    def calorie(self):
        while True:
            if self.exercise_selection == 1:
                exercise_calorie = self.time * (600 + self.level * 50)
                return exercise_calorie
            
            elif self.exercise_selection == 2:
                exercise_calorie = self.time * (600 + self.level * 50)
                return exercise_calorie
            
            elif self.exercise_selection == 3:
                exercise_calorie = self.time * (300 + self.level * 25)
                return exercise_calorie
            
            elif self.exercise_selection == 4:
                exercise_calorie = self.time * (520 + self.level * 40)
                return exercise_calorie
            
            elif self.exercise_selection == 5:
                exercise_calorie = self.time * (600 + self.level * 50)
                return exercise_calorie
            
            else:
                print("운동의 종류를 잘못 입력하셨습니다. 다시 입력하세요.\n")
                self.exercise_selection = int(input("운동할 방식을 다시 선택하세요 /수영=1,달리기=2,걷기=3,농구=4,축구=5\n"))

aa = int(input("운동할 방식을 선택하세요 /수영=1,달리기=2,걷기=3,농구=4,축구=5\n"))
bb = int(input("운동의 강도를 설정해 주세요 /1~5 : "))
cc = int(input("운동할 시간을 설정해주세요 : "))

exercise1 = Exercise(aa, cc, bb)
calorie1 = exercise1.calorie()
print(calorie1," 만큼 칼로리 소모가 가능합니다.\n")
class Daily_calories(Exercise):
         
    def __init__(self, bmr, calorie1, calorie_intake):
        
        self.bmr = bmr
        self.exercise_calories = calorie1
        self.calorie_intake = calorie_intake

    def real_calories(self):
        
        calorie_balance = self.bmr + self.exercise_calories - self.calorie_intake
    
        if calorie_balance < 0:
            return(calorie_balance * -1,"만큼 소비해야 합니다.")
            
        elif calorie_balance == 0:
            return("하루 적정 칼로리만큼 섭취했습니다.")
            
        else:
            return(calorie_balance,"만큼 섭취해야 합니다.")

calorie_intake = int(input("하루동안 먹은 칼로리를 입력하세요 : "))

daily_calories = Daily_calories(bmr,calorie1, calorie_intake)
calorie_balance = daily_calories.real_calories()
print(calorie_balance)