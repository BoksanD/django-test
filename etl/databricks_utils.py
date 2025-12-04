import requests
import certifi
from django.conf import settings

class DatabricksConnection:
    def __init__(self, connection_name='default'):
        config = settings.DATABRICKS_CONNECTIONS.get(connection_name)
        if not config:
            raise ValueError(f"Connection '{connection_name}' not found in settings")
        
        self.host = config['HOST']
        self.token = config['TOKEN']
        self.warehouse_id = config['WAREHOUSE_ID']
    
    def execute_query(self, sql):
        url = f"{self.host}/api/2.0/sql/statements/"
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {
            "statement": sql,
            "warehouse_id": self.warehouse_id,
            "wait_timeout": "30s"
        }
        
        response = requests.post(url, headers=headers, json=data, verify=certifi.where())
        result = response.json()
        
        if result.get('status', {}).get('state') == 'SUCCEEDED':
            columns = [col['name'] for col in result.get('manifest', {}).get('schema', {}).get('columns', [])]
            data_array = result.get('result', {}).get('data_array', [])
            return [dict(zip(columns, row)) for row in data_array]
        
        raise Exception(f"Query failed: {result}")

# Default connection
databricks = DatabricksConnection('default')