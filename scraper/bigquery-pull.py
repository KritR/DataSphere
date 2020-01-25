from google.cloud import bigquery

client = bigquery.Client()

query_job = client.query("""
  WITH
  subset AS (SELECT * FROM `gdelt-bq.gdeltv2.events` WHERE
  MonthYear=201801 AND
  ((ActionGeo_Lat IS NOT NULL AND ActionGeo_Long IS NOT NULL)
  OR
  (Actor1GEO_Lat IS NOT NULL AND Actor1GEO_Long IS NOT NULL)
  OR
  (Actor2GEO_Lat IS NOT NULL AND Actor2GEO_Long IS NOT NULL))
  ORDER BY NumMentions
  LIMIT 1000
  )
  
  SELECT MonthYear, Year, ActionGeo_FullName, ActionGeo_Lat, ActionGeo_Long, SOURCEURL FROM `gdelt-bq.gdeltv2.events`
  WHERE GLOBALEVENTID IN
  (SELECT MIN(GLOBALEVENTID) FROM subset
  GROUP BY SOURCEURL LIMIT 1000)
  LIMIT 100
  """)

results = query_job.result()
print(results)
