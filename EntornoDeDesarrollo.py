import psycopg2

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = "123456789",
        # database = 'mi_base_de_datos',
        database = 'postgres',
        port = '5432'
    )
    print("conexion Exitosa")

    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM usuarios")

    # Recuperar los resultados de la consulta
    usuarios = cursor.fetchall()

    # Imprimir los resultados
    for usuario in usuarios:
        print(usuario)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

except Exception as ex:
    print(ex)