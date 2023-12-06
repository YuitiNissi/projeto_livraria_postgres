import psycopg2


class ConexaoFactory:

    def get_conexao(self):
        return psycopg2.connect(
            host='berry.db.elephantsql.com',
            database='rohnsxty',
            user='rohnsxty',
            password='ZYx591ExAtJiaNgFiRIn-9CZebJkmv9H')
