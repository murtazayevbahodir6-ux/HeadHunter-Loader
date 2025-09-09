import pymysql
import logging

class Database:
  def __init__(self, host: str, user: str, password: str, db: str)  -> None:

    self.host = host
    self.user = user
    self.password = password
    self.db = db
    self.connection = None
    self.connect()
    self.create_main_vacancy()
    self.create_skills()
    self.create_vacancy_skill()

  def connect.self: > None:
    self.connection = pymysql.connect(
      host = self.host,
      user = self.user,
      password = self.password,
      db = self.db,
      port=3306,
      cursorclass=pymysql.cursors.DictCursor,
      )

    self.connection.autoocommit(True)
    self.cursor = self.connection.cursor()  


  def create_skills(self):
    try:
      sql = """
      CREATE TABLE IF NOT EXISTS `skills`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100)
);
"""
        
      self.cursor.execute(sql)
      self.connection.commit()

        except Exception as err:
            logging.error(err)


      def create_main_vacancy(self):
        try:
            sql = """
CREATE TABLE IF NOT EXISTS `main_vacancy`(
    `id` INT AUTO_INCREMENT,
    `vacancy_id` BIGINT,
    `min_salary` DECIMAL(10, 2),
    `max_salary` DECIMAL(10, 2)
);
"""

            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as err:
            logging.error(err)


    def create_vacancy_skill(self):
        try:
            sql = """
CREATE TABLE IF NOT EXISTS `vacancy_skill`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `skill_id` INT,
    `main_vacancy_id` INT,
    FOREIGN KEY (`skill_id`) REFERENCES `skills`(`id`),
    FOREIGN KEY (`main_vacancy_id`) REFERENCES `main_vacancy`(`id`)
);    
""""


            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as err:
            logging.error(err)

      def get_vacancy(self, vacancy_id):
        try:
            sql = "SELECT * FROM main_vacancy WHERE vacancy_id=%s"
            self.cursor.execute(sql, (vacancy_id, ))
            self.cursor.fetchone()
        except Exception as err:
            logging.error(err)

    def insert_vacancy(self, main_vacancy_id: int, min_salary: float = 0, max_salary: float = 0):
        try:
            sql = "INSERT INTO `main_vacancy`(`vacancy_id`, `min_salary`, `max_salary`) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (main_vacancy_id, min_salary, max_salary))
            self.connection.commit()
            self.cursor.lastrowid
        except Exception as err:
            logging.error(err)














      
  
