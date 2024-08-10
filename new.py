class BMI:

    def __init__(self,gender,Weight,height,age):

        self.age = age
        self.gender = gender
        self.Weight = Weight
        self.height = height

        while True:

            if self.gender == '남자':

                global Bmi = 66.47 + (13.75 * self.Weight) + (5 * self.height) - (6.76 * self.age)
                print(" BMI :",a)
                break
                

            elif self.gender == '여자':

                global Bmi = 65.51 + (9.56 * self.Weight) + (1.85 * self.height) - (4.68 * self.age)
                print(" BMI :",a)
                break

            else:
                print("성별을 잘못 입력하셨습니다. 다시 입력하세요.")
                continue

b = int(input("성별를 입력해주세요 : "))
c = int(input("몸무게를 입력해주세요 : "))
d = int(input("키를 입력해주세요 : "))
e = int(input("나이를 입력해주세요 : "))

bmi = BMI(b,c,d,e)
bmi1 = bmi.__init__()
print(bmi1)

class Exercise():

    def __init__ (self,Exercise_selection,Time,Level,Result):

            
        self.Exercise_selection = Exercise_selection
        self.Time = Time
        self.Level = Level

           
        def Exercise():

            while True:
                self.Result == 0
            
                if Exercise_selection == 1:

                    self.Result += Time*(600 + Level*50)
                    print(self.Result."만큼 칼로리 소모가 가능합니다.")
                    break

                elif Exercise_selection == 2:

                    self.Result += Time*(600 + Level*50)
                    print(self.Result."만큼 칼로리 소모가 가능합니다.")
                    break

                elif Exercise_selection == 3:

                    self.Result += Time*(300 + Level*25)
                    print(self.Result."만큼 칼로리 소모가 가능합니다.")
                    break

                elif Exercise_selection == 4:

                    self.Result += Time*(520 + Level*40)
                    print(self.Result."만큼 칼로리 소모가 가능합니다.")
                    break

                elif Exercise_selection == 5:

                    self.Result += Time*(600 + Level*50)
                    print(self.Result."만큼 칼로리 소모가 가능합니다.")
                    break

                else:
                    print("운동의 종류를 잘못 입력하셨습니다.")
                    continue

aa = int(input("운동할 방식을 선택하세요 /수영=1,달리기=2,걷기=3,농구=4,축구=5"))
bb = int(input("운동의 강도를 설정해 주세요 /1~5 : "))
cc = int(input("운동할 시간을 설정해주세요 = "))

exercise1 = Exercise(aa,bb,cc)
Exercise = exercise1.__init__
print(Exercise)

class EX(Exercise):

    def __init__ (self,Level):

        super().__init__(Result)

        self.Level = Level
        global Result2 = Ex_result
        
        if Level == 1:
            print(Ex_result)

        elif Level == 2:
            print(Ex_result)

        elif Level == 3:
            print(Ex_result)

        elif Level == 4:
            print(Ex_result)

        elif Level == 5:
            print(Ex_result)

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

            real_result = Bmi + Result2 - calorie_intake 

            while True:

                if real_result > 0

                    print(real_result,"만큼 소비해야 합니다.")

                elif real_result == 0

                    print("하루 적정 칼로리만큼 섭취했습니다.")

                else:

                    print(real_result,"만큼 섭취해야 합니다.") 

bbb = int(input("하루동안 먹은 칼로리를 입력하세요 : "))

Last = Daily_calories(bbb)
last1 = Last
print(last1)