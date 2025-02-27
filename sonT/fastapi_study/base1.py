from fastapi import FastAPI

app = FastAPI()

@app.get("/calaulate")
def calculate(a:int,b:int,how:str):
    if how == '덧셈':
        return a+b
    elif how == '뺄셈':
        return a-b
    elif how == '곱셈':
        return a*b
    elif how == '나눗셈':
        return a/b
    else:
        return("그런 계산은 불가능해요 :(")
