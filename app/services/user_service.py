from app.schemas.user import UserCreate

users_db: dict[int, dict] = {}
next_id = 1


def create_user(data: UserCreate) -> dict:
    global next_id
    new_user = {"id": next_id, **data.model_dump()}
    users_db[next_id] = new_user
    next_id += 1
    return new_user
