from typing import List, Union

import pymysql
from typing_extensions import Annotated
from fastapi import APIRouter, Query, HTTPException
from app.models import SubModel, MainModel, TypeModel, ProblemModel, NewProblem
from app.database.conn import db, connection
# from app.error.exceptions import NotFoundUsers, NotMatchEnum

router = APIRouter()


# @router.get('/common/users/')
# def db_check_ids(q: List[str] = Query()):
#     conn = connection()
#     with conn.cursor() as cursor:
#         # conn, cursor = db.get_db()
#         results = []
#         try:
#             for id in q:
#                 if id == '' or id is None:
#                     raise HTTPException(status_code=401, detail='Ids is empty')
#                 cursor.execute(f"SELECT id, tid, lesson_day FROM Users WHERE id='{id}'")
#                 result = cursor.fetchall()
#                 if len(result) == 0:
#                     results.append(id)
#             if results:
#                 raise NotFoundUsers(results)
#             data = ", ".join(f'"{id}"' for id in q)
#             cursor.execute(f"SELECT id, tid, lesson_day FROM Users WHERE id in ({data})")
#             result = cursor.fetchall()
#         except pymysql.Error as e:
#             raise HTTPException(status_code=500, detail=f'Database error: {e}')
#         finally:
#             cursor.close()
#             print("cursor.close")
#             conn.close()
#             print("conn.close")
#         return result
#
#
# @router.get('/common/')
# def get_user(user_id: str, skip: Union[str, None] = None, short: bool = False):
#     """
#     `ELB 상태 체크용 API`\n
#     입력내용
#     """
#     conn = connection()
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute("SELECT id FROM Users")
#             raw_data = cursor.fetchall()
#             data = ", ".join(f'{id}' for id in raw_data)
#             if user_id not in data:
#                 raise NotFoundUsers(user_id)
#             cursor.execute(f"SELECT * FROM Users WHERE id = '{user_id}'")
#             result = cursor.fetchone()
#             return result, skip, short
#     except pymysql.Error as e:
#         raise HTTPException(status_code=500, detail=f'Database error: {e}')
#
#
# @router.post('/common/')
# def create_item(item_id: str, q: Annotated[Union[str, None], Query(max_length=50)] = 'hellop'):
#     results = {"items": [{"ite_id": "Foo"}, {"item_id": "Bar"}]}
#     return q


@router.get('/main')
def get_main_category(main: int):
    """
    `대분류 API`\n
    """
    return


@router.post('/main/sub')
def get_sub_category(sub: SubModel):
    """
    `소분류 API`\n
    response: 문제번호 / 문제 출처 /
    """
    return sub.grade, sub.year, sub.month, sub.problem_number


@router.post('/type')
def get_type():
    """
    `문제 유형 API`\n
    response: 문제 유형 전체
    """
    return


@router.post('/main/sub/type/problem')
def get_problem(problem: ProblemModel):
    """
    `문제 유형 API`\n
    `request: problem_id(int, 문제 번호) / problem_source(str, 출처) / type(int, 유형)`\n
    `response: problem_id(int, 문제 번호) / problem_source(str, 출처)`
    """
    return problem.problem_id, problem.problem_source


@router.get('/main/sub/type/problem/{problem_id}')
def get_problem_content(problem_id: int):
    """
    `문제 내용 API`\n
    `request: problem_id(int, 문제 번호)`\n
    `response: problem_content(str, 문제 내용)`
    """
    return problem_id


@router.get('/main/sub/type/problem/{problem_id}/change')
def get_new_problem_content(problem_id: int):
    """
    `선생님이 수정한 문제 내용 API`\n
    `request: problem_id(int, 문제 번호)`\n
    `response: problem_content(str, 문제 내용)`
    """
    return problem_id


@router.post('/main/sub/type/problem/{problem_id}/change')
def post_new_problem_content(problem: NewProblem):
    """
    `선생님이 수정한 문제 내용 API`\n
    `request: new_problem_content(str, 수정된 문제 내용), new_problem_id(int, 수정된 문제 ID)`\n
    `response: "success"`
    """
    return problem.new_problem_id, problem.new_problem_content