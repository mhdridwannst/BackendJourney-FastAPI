from fastapi import APIRouter

router = APIRouter()

data = [
    {"user_id": 1, "name": "Mhd. Ridwan"},
    {"user_id": 2, "name": "Wannn Sion"},
    {"user_id": 3, "name": "Anita Helviana"},
    {"user_id": 4, "name": "Mio Imada"},
    {"user_id": 5, "name": "Go Youn Jung"}
]


@router.get("/users/{user_id}")
def get_user(user_id: int, detail: bool = False):
    result = {"user_id": user_id, "name": f"{data[user_id - 1]['name']}"}
    if detail:
        result["note"] = "Ini data detail"
    return result
