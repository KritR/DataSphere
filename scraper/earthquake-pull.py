from google.cloud import bigquery
import db as db
import datetime
import sys

client = bigquery.Client()

def request_data():
  query_job = client.query("""
    WITH
    subset AS (SELECT * FROM `bigquery-public-data.noaa_significant_earthquakes.earthquakes` WHERE
    latitude IS NOT NULL AND longitude IS NOT NULL AND eq_primary IS NOT NULL AND month IS NOT NULL AND year IS NOT NULL),
    subset2 AS (SELECT * FROM subset ORDER BY year)
  
    SELECT country, eq_primary, month, year, day, latitude, longitude, location_name FROM subset2
    """)

  return query_job.result()



if __name__ == '__main__':
  username = sys.argv[1]
  password = sys.argv[2]
  earthquakes = request_data()
  # db.write_earthquake("USA", 7.65, 1, 2020, 26, 40.08, -86.9, "West Lafeyette", auth=(username, password))
  for row in earthquakes:
    day = None
    country = None
    location_name = None
    if not row["day"]:
      day = 1
    if not row["country"]:
      country = ""
    if not row["location_name"]:
      location_name = ""
    db.write_earthquake((row["country"] if not country else country), float(row["eq_primary"]), int(row["month"]), int(row["year"]), (int(row["day"]) if not day else day), float(row["latitude"]), float(row["longitude"]), (row["location_name"] if not location_name else location_name), auth=(username, password))
