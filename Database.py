import Configuration
import psycopg2
import logging

config = Configuration.Configuration()
logger = logging.getLogger()

class SQL:
    def __init__(self):
        dbConfig = config.getDatabaseConfig()
        self.__USERNAME = dbConfig["USER"]
        self.__PASSWORD = dbConfig["PASSWORD"]
        self.__HOST = dbConfig["HOST"]
        self.__PORT = dbConfig["PORT"]
        self.__DATABASE_NAME = dbConfig["NAME"]

    def createDatabaseConnection(self):
        logger.debug("Creating Database Connection")
        try:
            self.__connection = psycopg2.connect(
                user = self.__USERNAME,
                password = self.__PASSWORD,
                host = self.__HOST,
                port = self.__PORT,
                database = self.__DATABASE_NAME
            )
            self.__cursor = self.__connection.cursor()
            logger.info(self.__connection.get_dsn_parameters())
        except (Exception, psycopg2.Error) as e :
            logger.exception("Error while connecting to PostgreSQL")

    def closeDatabaseConnection(self):
        logger.debug("Closing Database Connection")
        if(self.__connection):
            self.__cursor.close()
            self.__connection.close()

    def getData(self, username, query):
        logger.debug("getData Query: %s username: %s", query, username)
        self.createDatabaseConnection()
        self.__cursor.execute("\
            SELECT DISTINCT(keyword) from search where username = '{}' and keyword like '%{}%';".format(
                username, query))
        record = self.__cursor.fetchall()
        self.closeDatabaseConnection()
        response = [each[0] for each in record]
        logger.debug("Query Result: %s", response)
        return response

    def pushData(self, username, data):
        logger.debug("pushData Query:%s username: %s", data, username)
        self.createDatabaseConnection()
        self.__cursor.execute("\
            INSERT INTO search (username, keyword) VALUES ('{}', '{}');".format(
                username, data))
        self.__connection.commit()
        logger.debug("Entry Saved to database")
        self.closeDatabaseConnection()