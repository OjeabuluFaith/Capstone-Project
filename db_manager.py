import mysql.connector
from mysql.connector import Error as MySQLError


class DatabaseManager():
    """
    This class manages access and CRUD operations to a MySQL database
    """

    def __init__(self, host, port, name, user, password):
        """The constructor

        Args:
            host (str): server host of the database
            port (int): server port of the database
            name (str): name of the database
            user (str): name of user
            password (str): password of user
        """
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
        self.__connection = None

        try:
            print(
                print(
                    f"\n-->>> Connecting to MySQL Database: {user}@{host}:{port} <<<---\n")
            )
            connection = mysql.connector.connect(
                host=host, port=port, user=user, passwd=password, db=name)

            self.__connection = connection
            print(f'\n-->>> MySQL Database connected successfully<<---\n')

        except MySQLError as err:
            print(f"\n-->>> MySQL Database connected failed: {err} <<---\n")

    def create_job_listings_table(self):
        """
            create job listings table
        """

        try:
            with self.__connection.cursor() as cursor:
                # create table
                sql = """CREATE TABLE IF NOT EXISTS `job_listings` (
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `title` VARCHAR(255) NOT NULL,
                    `link` TEXT,
                    `employer` VARCHAR(255),
                    `logo` TEXT,
                    `location` VARCHAR(255),
                    `type` VARCHAR(255),
                    `salary` VARCHAR(255),
                    `summary` TEXT,
                    `sector` VARCHAR(255),
                    `timestamp` VARCHAR(255),
                    PRIMARY KEY (`id`)
                ) DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1;
                """
                cursor.execute(sql)
            print(f"\n-->>> Table created successfully <<---\n")
        except MySQLError as err:
            print(f"\n-->>> Table creation failed: {err} <<---\n")

    def add_job_listings_to_table(self, job_listings):
        """bulk insert job listings to table

        Args:
            job_listings (list): list of job listings
        """
        try:
            values = ""
            for job_listing in job_listings:
                value = f"({job_listing.title}, {job_listing.link}, {job_listing.employer}, {job_listing.logo}, {job_listing.location}, {job_listing.type}, {job_listing.salary}, {job_listing.summary}, {job_listing.sector}, {job_listing.timestamp}), "
                values += value

            print(f"-->>> Inserting records... <<---\n")

            with self.__connection.cursor() as cursor:
                # bulk insert job listings
                sql = """INSERT INTO `job_listings` 
                (`id`,`title`, `link`, `employer`, `logo`, `location`, `type`, `salary`, `summary`, `sector`, `timestamp`) 
                VALUES {values};
                """.format(values=values)
                cursor.execute(sql)
            print(f"\n-->>> Records inserted successfully <<---\n")

        except MySQLError as err:
            print(f"\n-->>> Insert failed: {err} <<---\n")

    def drop_job_listings_table(self):
        """
            drop job listings table from the database
        """
        try:
            print(f"-->>> Dropping table... <<---\n")
            with self.__connection.cursor() as cursor:
                # drop table
                sql = """DROP TABLE IF EXISTS job_listings;
                """
                cursor.execute(sql)
            print(f"\n-->>> Table dropped successfully <<---\n")
        except MySQLError as err:
            print(f"\n-->>> Failed to drop table: {err} <<---\n")
