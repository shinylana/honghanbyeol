'''
실행 명령어
uvicorn 2_crud:app --reload
'''
from fastapi import FastAPI, HTTPException

app = FastAPI()

# 임시 저장소 (실습용)
items = {
    1: {"name": "사과", "price": 1000},
    2: {"name": "바나나", "price": 2000}
}

# GET: 전체 아이템 목록
@app.get("/items")
def get_items():
    return items

# GET: 특정 아이템 조회
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="아이템 없음")
    return items[item_id]

# POST: 새로운 아이템 추가
@app.post("/items/{item_id}")
def create_item(item_id: int, item: dict):
    if item_id in items:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이템")
    items[item_id] = item
    return {"msg": "추가 완료", "item": items[item_id]}

# PUT: 아이템 전체 수정
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="아이템 없음")
    items[item_id] = item
    return {"msg": "수정 완료", "item": items[item_id]}

# DELETE: 아이템 삭제
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="아이템 없음")
    del items[item_id]
    return {"msg": "삭제 완료"}
