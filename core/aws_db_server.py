import mariadb

# connection params
conn_params = {
    'user': 'admin',
    'password': 'deloitteroot',
    'host': 'hawkbit-dev-db.cl6fb50ajwf8.us-east-1.rds.amazonaws.com',
    # 'database': 'app_users'
}

# establish connection
connection = mariadb.connect(**conn_params)

cursor = connection.cursor()

# cursor.execute(
#     '''
#     INSERT INTO users (
#         username,
#         password,
#         name
#     )
#     VALUES (
#         'laulita',
#         'pimienta',
#         'laura'
#     );
#     '''
# )

# connection.commit()

cursor.execute(
    'SELECT * FROM users;'
)

rows = cursor.fetchall()

for row in rows:
    print(
        f"""
            Username: {row[0]},
            Password: {row[1]},
            Name: {row[2]}
        """
    )

cursor.close()
connection.close()
