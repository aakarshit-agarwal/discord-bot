import psycopg2

class SQL:
    def __init__(self, config):
        self.__USERNAME = config["USER"]
        self.__PASSWORD = config["PASSWORD"]
        self.__HOST = config["HOST"]
        self.__PORT = "5432"
        self.__DATABASE_NAME = config["NAME"]

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
            print("PostgreSQL connection is closed")

    def getData(self, query):
        print("getData Query: ", query)
        self.createDatabaseConnection()
        self.cursor.execute("SELECT version();")
        record = self.cursor.fetchone()
        self.closeDatabaseConnection()
        print("You are connected to - ", record,"\n")

    def pushData(self, data):
        pass