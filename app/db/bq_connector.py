import logging
from google.cloud import bigquery
from decouple import config
import json 
client = bigquery.Client()

BQ_TBL_NAME=config('BQ_TBL_NAME_FULL')
# Perform a query.
COUNT_QUERY = (
    f"SELECT company_id FROM `{BQ_TBL_NAME}` GROUP BY company_id"
)

def fire_bq():
  query_job = client.query(COUNT_QUERY)  # API request
  rows = query_job.result()  # Waits for query to finish

  if rows.total_rows > 0:
    df = rows.to_dataframe()
    json_rows = json.loads(df.to_json())
    for row in json_rows:
        logging.info("ROW: %s. ROWs: %s. ",type(row),type(json_rows))
  return json_rows


def get_bq_tbl(bq_tbl_name):

    query_job = client.query(bq_tbl_name)
    if query_job.total_rows > 0:
        df = query_job.to_dataframe()
        return df.to_json(orient='records', force_ascii=False)

    return {"detail": {"status": "success", "message":"no data found"}}

