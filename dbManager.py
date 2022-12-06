import sqlite3


class Database:
    def __init__(self) -> None:
        self.path_002 = "./database.db"
        self.connection_002 = sqlite3.connect(self.path_002)

        cur = self.connection_002.cursor()
        # cur.execute(""" drop table scores; """)
        # cur.execute(""" drop table users; """)

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL
            );
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                difficulty TEXT NOT NULL,
                score INTEGER NOT NULL,
                time_taken FLOAT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            """
        )

    def get_user_002(self, username):
        cur = self.connection_002.cursor()
        cur.execute(
            f"""
            SELECT * FROM users WHERE username = '{username}';
            """
        )

        return cur.fetchone()

    def insert_score_002(self, username, difficulty, score, time_taken):
        cur = self.connection_002.cursor()
        if self.get_user_002(username) is None:
            cur.execute(
                f"""
                INSERT INTO users (username) VALUES ('{username}');
                """
            )

            self.connection_002.commit()
            self.connection_002.close()
            self.connection_002 = sqlite3.connect(self.path_002)
            cur = self.connection_002.cursor()

        user_id = self.get_user_002(username)[0]

        cur.execute(
            f"""
                INSERT INTO scores 
                (user_id, difficulty, score, time_taken)
                VALUES 
                ('{user_id}', '{difficulty}', '{score}', '{time_taken}');
            """
        )

        self.connection_002.commit()

    def get_scores_002(self, difficulty=None):

        if difficulty is None:
            cur = self.connection_002.cursor()
            cur.execute(
                """
                SELECT u.username,s.difficulty, s.score, s.time_taken FROM scores s join users u on s.user_id = u.id ORDER BY s.score DESC, s.time_taken DESC;
                """
            )
            return cur.fetchall()

        cur = self.connection_002.cursor()
        cur.execute(
            f"""
            SELECT u.username, s.difficulty, s.score, s.time_taken FROM scores s join users u on s.user_id = u.id WHERE s.difficulty = '{difficulty}' ORDER BY s.score DESC, s.time_taken DESC;
            """
        )

        return cur.fetchall()


# db = Database()
# db.insert_score_002("test1", "HARD", 50, 11.89445)
# db.insert_score_002("test2", "EASY", 200, 20.32434)
# db.insert_score_002("test3", "MEDIUM", 300, 30.32434)
# db.insert_score_002("test4", "MEDIUM", 400, 40.883)
# db.insert_score_002("test5", "HARD", 500, 50.5035)
# db.insert_score_002("test6", "HARD", 600, 60.32434)

# print(db.get_scores_002("HARD"))

# print(db.get_user("u1"))
