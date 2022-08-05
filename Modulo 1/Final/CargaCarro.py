import pandas as pd
import pymysql.cursors

# Import CSV
data = pd.read_csv(r'D:\BootCamp - Engenheiro de Dados IGTI\Modulo 1\Final\CargasCarro_DW.csv', delimiter=';')
csv_data = pd.DataFrame(data)

# Connect to SQL Server
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='bootm1',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

cols = "`,`".join([str(i) for i in csv_data.columns.tolist()])

# Insert DataFrame recrds one by one.
for i, row in csv_data.iterrows():
    sql = "INSERT INTO `carro` (`" + cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()
