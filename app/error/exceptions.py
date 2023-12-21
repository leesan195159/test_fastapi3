from typing import List
# from app.models import ModelName
from fastapi import HTTPException


class StatusCode:
    HTTP_500 = 500
    HTTP_400 = 400
    HTTP_401 = 401
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_405 = 405


class APIException(Exception):
    status_code: int
    detail: str

    def __init__(self, status_code: int, detail: str = None):
        self.status_code = status_code
        self.detail = detail


class NotFoundUsers(APIException):
    def __init__(self, user_id: List = None):
        super().__init__(
            status_code=StatusCode.HTTP_404,
            detail=f"해당 유저를 찾을 수 없습니다: {user_id}"
        )
        raise HTTPException(status_code=self.status_code, detail=self.detail)


# class NotMatchEnum(APIException):
#     def __init__(self, name: ModelName):
#         super().__init__(
#             status_code=StatusCode.HTTP_400,
#             detail=f"Enum 형식에 맞지 않습니다: {name.hiyoonji, name.yc0603}"
#         )
#         raise HTTPException(status_code=self.status_code, detail=self.detail)
