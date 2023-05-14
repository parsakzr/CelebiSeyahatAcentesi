import psycopg
import sys

print("Python version: ", sys.version)
print("psycopg version: ", psycopg.__version__)

class Database:
    def __init__(self, db_name, db_username, db_passwd, db_host):
        self.db_name = db_name
        self.db_username = db_username
        self.db_passwd = db_passwd
        self.db_host = db_host
    
    def ticket_query(self, ticket_company, ticket_from, ticket_to):
        try:
            db_connection = psycopg.connect(dbname=self.db_name, user=self.db_username, host=self.db_host, password=self.db_passwd)
            cur = db_connection.cursor()

            query = str('SELECT tPrice FROM transportation WHERE tCompany=%s and tFrom=%s and tTo=%s')
            query_values = (ticket_company, ticket_from, ticket_to)

            cur.execute(query, query_values)
            db_connection.commit()
            query_result = cur.fetchone()

            print(f"The price is: {query_result[0]}")

            cur.close()
        except:
            print("Cannot execute query!")
        finally:
            if db_connection is not None:
                db_connection.close()
                print("Connection closed!")
    
def main():
    agenta_db = Database("agenta_db", "postgres", "15246868", "localhost")
    agenta_db.ticket_query(str('YTUR'), str('İstanbul'), str('New York'))

if __name__ == "__main__":
   main()