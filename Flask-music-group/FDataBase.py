import sqlite3
import json

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # додавання нового альбрму
    def AddAlbum(self, name, year, info, info2):
        try:
            self.__cur.execute("INSERT INTO albums VALUES(NULL, ?, ?, ?, ?)", (name, year, info, info2))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Помилка дадавання в БД"+str(e))
            return False
        return True

    #Отримати окремий альбом
    def getPost(self, postId):
        try:
            self.__cur.execute(f"SELECT * FROM albums WHERE id = {postId} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Помилка отримання даних з БД" + str(e))

        return (False, False)

    # Отримати всі альбоми
    def getAllPost(self):
        try:
            self.__cur.execute(f"SELECT * FROM albums")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Помилка отримання даних з БД" + str(e))

        return (False, False)

    #Оновити альбом
    def updatePost(self, postId, name, year, info, info2):
        try:
            print(name)
            print(postId)
            self.__cur.execute(f"UPDATE albums SET name = ?, year = ?, info = ?, info2 = ?  WHERE id LIKE {postId}", (name, year, info, info2))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Помилка отримання даних з БД" + str(e))

        return (False, False)

    def deletePost(self, postId):
        try:
            self.__cur.execute(f"DELETE FROM albums  WHERE id LIKE {postId}")
            self.__db.commit()
        except sqlite3.Error as e:
            print("Помилка видалення даних з БД" + str(e))

        return (False, False)