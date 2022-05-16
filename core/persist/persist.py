from peewee import MySQLDatabase
from core.utils.config import (
    create_conftest as json_conf
)


class Database:
    """Singleton Style to open or close a database connection.
    """

    _database = None
    _params = {
        'database': 'basename',
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '$RealMadrid10'
    }

    @classmethod
    def open_it(cls) -> MySQLDatabase:
        """It opens a new database connection.
        Or returns if there's it.

        Returns:
            MySQLDatabase: MySQL database style.
        """
        conf = json_conf()
        cls._params['database'] = conf['database'] \
            if not conf['testing'] else conf['dbtest']
        if not cls._database:
            cls._database = MySQLDatabase(**cls._params)
        return cls._database

    @classmethod
    def close_it(cls) -> None:
        """It close a database connection.
        """
        if isinstance(cls._database, MySQLDatabase):
            cls._database = None
            cls._params['database'] = 'basename'
