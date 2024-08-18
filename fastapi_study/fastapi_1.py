from fastapi import FastAPI

app = FastAPI()

players = ['데이터는 추후 수작업으로 입력'] 
#추후에 ["선수 이름 : 0","선수 이름 : 0"]이런 식으로 해놔서 선수 정보 입력하면 value에 1씩 더해 mvp선수 고르기
a = 0

@app. post("/vote")
def vote_player(player: str):
    global a

    if player in players.keys():
        a += 1
        player.value += 1
        return  f"{player}에게 투표했습니다. 전체 투표수: {a}"

    if player not in players.keys():
        return "없는 선수 정보입니다. 다시 입력해주세요."
    
@app. get("/progress")
def open_progress(player: str):
    if player in players.keys():
        return f"{player}의 표는 총 {player.value}표입니다."
        

@app. post("/players")
def add_player(player: str):
    
    if player not in players.keys():
        
        new_player = player
        players.keys() += new_player
        
    return players

@app. get("/results/")
def get_results():
    return players.keys()
