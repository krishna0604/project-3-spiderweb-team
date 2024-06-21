# C:/Users/user/Downloads/spiderweb3-7a16d1d8cbf2.json

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2
from google.cloud import bigquery
from google.oauth2 import service_account

# Definisi fungsi extract_postgres_to_df dan load_df_to_bigquery seperti sebelumnya

def postgres_to_bigquery_task(table_name, table_id, host, database, user, password, key_path):
    try:
        df = extract_postgres_to_df(host, database, user, password, table_name)
        load_df_to_bigquery(df, table_id, key_path)
        print(f"Task for table {table_name} completed successfully.")
    except Exception as e:
        print(f"Error processing table {table_name}: {str(e)}")
        raise e
    
# Definisi default arguments untuk DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Buat DAG
with DAG(
    'postgres_to_bigquery_dag',
    default_args=default_args,
    schedule_interval='@daily',
) as dag:
    
    # Daftar tabel-tabel yang ingin diekstrak dan dimuat ke BigQuery
    tables_to_process = [
        {'table_name': 'categories', 'table_id': 'spiderweb3.spiderweb_p3.categories'},
        {'table_name': 'customers', 'table_id': 'spiderweb3.spiderweb_p3.customers'},
        {'table_name': 'employee_territories', 'table_id': 'spiderweb3.spiderweb_p3.employee_territories'},
        {'table_name': 'employees', 'table_id': 'spiderweb3.spiderweb_p3.employees'},
        {'table_name': 'order_details', 'table_id': 'spiderweb3.spiderweb_p3.order_details'},
        {'table_name': 'orders', 'table_id': 'spiderweb3.spiderweb_p3.orders'},
        {'table_name': 'products', 'table_id': 'spiderweb3.spiderweb_p3.products'},
        {'table_name': 'regions', 'table_id': 'spiderweb3.spiderweb_p3.regions'},
        {'table_name': 'shippers', 'table_id': 'spiderweb3.spiderweb_p3.shippers'},
        {'table_name': 'suppliers', 'table_id': 'spiderweb3.spiderweb_p3.suppliers'},
        {'table_name': 'territories', 'table_id': 'spiderweb3.spiderweb_p3.territories'},
        {'table_name': 'datamart_monthly_supplier_gross_revenue', 'table_id': 'spiderweb3.spiderweb_p3.datamart_monthly_supplier_gross_revenue'},
        {'table_name': 'datamart_monthly_category_sold', 'table_id': 'spiderweb3.spiderweb_p3.datamart_monthly_category_sold'},
        {'table_name': 'datamart_monthly_best_employee', 'table_id': 'spiderweb3.spiderweb_p3.datamart_monthly_best_employee'}
        # Tambahkan tabel-tabel lainnya sesuai kebutuhan
    ]
    
    # Definisi task untuk setiap tabel
    for table_info in tables_to_process:
        task_id = f'postgres_to_bigquery_task_{table_info["table_name"]}'
        PythonOperator(
            task_id=task_id,
            python_callable=postgres_to_bigquery_task,
            op_args=[table_info['table_name'], table_info['table_id'], 
                     '47.237.106.32', 'spiderweb_db', 'spiderweb_p3', 'spiderweb_p3',
                     'C:/Users/user/Downloads/spiderweb3-7a16d1d8cbf2.json'],  # Ganti dengan lokasi kunci Anda
        )