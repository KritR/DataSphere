from google.cloud import bigquery
import dateparser
import db as db
import datetime
import sys

client = bigquery.Client()

def request_data(yearmonth):
  query_job = client.query("""
    WITH
    subset AS (SELECT * FROM `gdelt-bq.gdeltv2.events` WHERE
    """
    f'MonthYear={yearmonth} AND'
    """
    (ActionGeo_Lat IS NOT NULL AND ActionGeo_Long IS NOT NULL)
    ORDER BY NumMentions
    LIMIT 1000
    )
    
    SELECT MonthYear, Year, ActionGeo_FullName, ActionGeo_Lat, ActionGeo_Long, SOURCEURL FROM `gdelt-bq.gdeltv2.events`
    WHERE GLOBALEVENTID IN
    (SELECT MIN(GLOBALEVENTID) FROM subset
    GROUP BY SOURCEURL LIMIT 1000)
    LIMIT 100
    """)

  return query_job.result()



if __name__ == '__main__':
  username = sys.argv[1]
  password = sys.argv[2]
  for year in range(2015, 2017):
    for month in range(1,13):
      yearmonth = str(year) + "{:0>2}".format(month)
      result = request_data(yearmonth)
      print(yearmonth)
      for row in result:
        #with open("data.csv", 'a') as f:
        #  f.write(f'{row["SOURCEURL"]}, {row["ActionGeo_Lat"]}, {row["ActionGeo_Long"]}\n')
        db.write_to_db("", datetime.datetime(year, month, 1), url=row["SOURCEURL"], lat=float(row["ActionGeo_Lat"]), lon=float(row["ActionGeo_Long"]), auth = (username, password))
