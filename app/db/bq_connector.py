from google.cloud import bigquery
from decouple import config

client = bigquery.Client()

BQ_TBL_NAME=config('BQ_TBL_NAME_FULL')
# Perform a query.
QUERY = (
    'SELECT COUNT(DISTINCT user_id) user_identifier'
    f"FROM `{BQ_TBL_NAME}`"
)

def fire_bq():
  query_job = client.query(QUERY)  # API request
  rows = query_job.result()  # Waits for query to finish

  for row in rows:
      print(row.name)


def get_bq_tbl(bq_tbl_name):

    query_job = client.query(bq_tbl_name)
    rows = query_job.result(QUERY)
    if rows.total_rows > 0:
        df = rows.to_dataframe()
        return df.to_json(orient='records', force_ascii=False)

    return {"detail": {"status": "success", "message":"no data found"}}

