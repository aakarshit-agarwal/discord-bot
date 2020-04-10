import Configuration
import psycopg2

config = Configuration.Configuration()

class SQL:
    def __init__(self):
        dbConfig = config.getDatabaseConfig()
        self.__USERNAME = dbConfig["USER"]
        self.__PASSWORD = dbConfig["PASSWORD"]
        self.__HOST = dbConfig["HOST"]
        self.__PORT = dbConfig["PORT"]
        self.__DATABASE_NAME = dbConfig["NAME"]

    def createDatabaseConnection(self):
        print("Creating Database Connection")
        try:
            self.connection = psycopg2.connect(
                user = self.__USERNAME,
                password = self.__PASSWORD,
                host = self.__HOST,
                port = self.__PORT,
                database = self.__DATABASE_NAME
            )
            self.cursor = self.connection.cursor()
            print ( self.connection.get_dsn_parameters(),"\n")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

    def closeDatabaseConnection(self):
        print("Closing Database Connection")
        if(self.connection):
            self.cursor.close()
            self.connection.close()

    def getData(self, username, query):
        print("getData Query: ", query, "username:", username)
        self.createDatabaseConnection()
        self.cursor.execute("\
            SELECT DISTINCT(keyword) from search where username = '{}' and keyword like '%{}%';".format(
                username, query))
        record = self.cursor.fetchall()
        self.closeDatabaseConnection()
        response = [each[0] for each in record]
        print("Query Result:", response)
        return response

    def pushData(self, username, data):
        print("pushData Query:", data, "username:", username)
        self.createDatabaseConnection()
        self.cursor.execute("\
            INSERT INTO search (username, keyword) VALUES ('{}', '{}');".format(
                username, data))
        self.connection.commit()
        self.closeDatabaseConnection()