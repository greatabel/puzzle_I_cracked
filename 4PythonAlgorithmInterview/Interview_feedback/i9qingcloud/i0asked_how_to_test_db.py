'''


#----------------------------#

1 怎么测试你们python和数据库相关的代码？
    

'''

import time
from termcolor import colored

import testing.mysqld
from sqlalchemy import create_engine

# prevent generating brand new db every time.  Speeds up tests.
MYSQLD_FACTORY = testing.mysqld.MysqldFactory(cache_initialized_db=True, port=7531)


def tearDownModule():
    """Tear down databases after test script has run.
    https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass
    """
    MYSQLD_FACTORY.clear_cache()


class TestWhatever(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mysql = MYSQLD_FACTORY()
        cls.db_conn = create_engine(cls.mysql.url()).connect()

    def setUp(self):
        self.mysql.start()
        self.db_conn.execute("""CREATE TABLE `foo` (blah)""")

    def tearDown(self):
        self.db_conn.execute("DROP TABLE foo")

    @classmethod
    def tearDownClass(cls):
        cls.mysql.stop()  # from source code we can see this kills the pid

    def test_something(self):
        # something useful
        ''


def main_process():
    t = '''
    1 怎么测试你们python和数据库相关的代码？
    https://stackoverflow.com/questions/28431452/mock-a-mysql-database-in-python

    '''
    print(t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





