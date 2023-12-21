from fastapi import FastAPI
import logging
import pymysql


def connection():
    conn = pymysql.connect(
        host='192.168.0.53',
        user='mct',
        password='adotAI!@34',
        database='AIC'
    )
    return conn
class Pymysql:
    def __init__(self, app=None, **kwargs):
        self._connection = None
        if app is not None:
            self.init_app(app=app, **kwargs)


    def init_app(self, app, **kwargs):
        self._connection = pymysql.Connection(
            host=kwargs.get("DB_URL"),
            user=kwargs.get("DB_USER"),
            password=kwargs.get("DB_PASSWORD"),
            database=kwargs.get("DB")
        )

        def startup():
            logging.info("DB connected")
            print("DB connected")

        def shutdown():
            self._connection.close()
            logging.info("DB Disconnected")
            print("DB Disconnected")

        app.add_event_handler("startup", startup)
        app.add_event_handler("shutdown", shutdown)

    # def get_db(self):
    #     if self._connection is None:
    #         raise Exception("must be called init_app")
    #     # try:
    #     cursor = self._connection.cursor()
    #     return self._connection, cursor
    #     # finally:
    #     #     self._connection.close()


db = Pymysql()




