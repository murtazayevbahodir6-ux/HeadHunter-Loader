import requests
from datetime import datetime, timedelta
from logging

from loader import db 
from pprint import pprint
from data.config import BASE_URL

class VacancyLoader:
  def __init__(self):
    self.start_date = (datetime.now() - timedelta(days = 2)).date()
    self.end_date = datetime.now().date()

  def fit(self):
    try:
        params = {
         "date_from": self.start_date.isoformat(),
         "date_to": self.end_date.isoformat(),
         "per_page": 100
        }
      response = requests.get(BASE_URL, params = params)

      if response.status_code == 200 and response.status_code != []:
        data = response.json()
        for i in data("items"):
          saver = VacancySaver(vacancy_id = i ["id"])
          save.fit()
          exit()
    except Exception as error:
        logging error(err)


class VacancySaver:
  def __init__2(self, vacancy_id):
    self.vacancy_id = vacancy_id


  def fit(self):
    try: 
      url = f"{BASE_URL}/{self.vacancy_id}"
      res = requests.get(url)

      if res.status_code == 200:
        data = res.json()
        logging.info(data)
        check = db.get_vacancy(vacancy_id = int(data["id"]))

        if check is None:
          vacancy_id = db.insert_vacancy(main_vacancy_id = int(data["id"]))
      else:
        logging.error("err")


    except Exception as err:
      logging error(err)

  

    
    
  
    
  
