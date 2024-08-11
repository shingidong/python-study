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
print("가초대사량 : ",bmr)

class Exercise:

    def __init__ (self,Exercise_selection,Time,Level):
            
        self.Exercise_selection = Exercise_selection
        self.Time = Time
        self.Level = Level

        while True:
        
            if Exercise_selection == 1:

                exercise_calorie = Time*(600 + Level*50)
                return exercise_calorie

            elif Exercise_selection == 2:

                exercise_calorie = Time*(600 + Level*50)
                return exercise_calorie

            elif Exercise_selection == 3:

                exercise_calorie = Time*(300 + Level*25)
                return exercise_calorie

            elif Exercise_selection == 4:

                exercise_calorie = Time*(520 + Level*40)
                return exercise_calorie

            elif Exercise_selection == 5:

                exercise_calorie = Time*(600 + Level*50)
                return exercise_calorie

            else:
                return("운동의 종류를 잘못 입력하셨습니다.")

aa = int(input("운동할 방식을 선택하세요 /수영=1,달리기=2,걷기=3,농구=4,축구=5"))
bb = int(input("운동의 강도를 설정해 주세요 /1~5 : "))
cc = int(input("운동할 시간을 설정해주세요 : "))

exercise1 = Exercise.__init__(aa,bb,cc)
print(exercise1)

class EX(Exercise):

    def __init__ (self,Level):

        self.Level = Level
        
        if Level == 1:
            print(exercise1)

        elif Level == 2:
            print(exercise1)

        elif Level == 3:
            print(exercise1)

        elif Level == 4:
            print(exercise1)

        elif Level == 5:
            print(exercise1)

        else:
            print("운동량의 강도를 잘못 설정하셨습니다.")

aaa = int(input("운동의 강도를 선택해주세요(1~5) :"))

ex = EX(aaa)
Exercise1 = ex.__init__
print(Exercise1)

class Daily_calories(EX):

     def __init__ (self,calorie_intake):

            self.calorie_intake = calorie_intake 
            super().__init__(EX)

            real_result = bmi + exercise1 - calorie_intake 

            while True:

                if real_result > 0:

                    print(real_result,"만큼 소비해야 합니다.")

                elif real_result == 0:

                    print("하루 적정 칼로리만큼 섭취했습니다.")

                else:

                    print(real_result,"만큼 섭취해야 합니다.") 

bbb = int(input("하루동안 먹은 칼로리를 입력하세요 : "))

Last = Daily_calories(bbb)
last1 = Last
print(last1)