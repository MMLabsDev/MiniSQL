database = {}

while True:
    command = input("MiniSQL > ")

    if command.lower() == "exit":
        break

    elif command.lower() == "show database":
        print(database)
        continue

    parts = command.split()

    
    if len(parts) == 2 and parts[0].upper() == "CREATE" and parts[1].upper() == "TABLE":
        table_name = input("Nombre de la tabla: ")

        if table_name in database:
            print(f"La tabla '{table_name}' ya existe")
            continue

        values = input("Inserte valores separados por espacios: ").split()

        v = []

        for val in values:
            v.append(val)

        database[table_name] = v

    print(f"Tabla '{table_name}' creada")
    print(database[table_name])


    if len(parts) == 3 and parts[0].upper() == "CREATE" and parts[1].upper() == "TABLE":
        table_name = parts[2]

        database[table_name] = []

        print(f"Tabla '{table_name}' creada.")


    elif len(parts) == 4 and parts[0].upper() == "INSERT" and parts[1].upper() == "INTO":
        table_name = parts[2]
        added = parts[3]

        if table_name not in database:
            print(f"La tabla '{table_name}' no existe.")
            continue

        database[table_name].append(added)
        print(f"'{added}' guardado correctamente")

    elif len(parts) > 3 and parts[0].upper() == "ADD" and parts[1].upper() == "COLUMNS":
        table_name = parts[2]
        column = parts[3]
        database[table_name][column] = []
        print(f"Columna {column} creada")

    elif len(parts) == 3 and parts[0].upper() == "SHOW" and parts[1].upper() == "TABLE":
        table_name = parts[2]

        print(database[table_name])

    elif len(parts) == 3 and parts[0].upper() == "DELETE" and parts[1].upper() == "TABLE":
        table_name = parts[2]
        del database[table_name]
        print("Tabla borrada")

    elif len(parts) == 2 and parts[0].upper() == "DELETE" and parts[1].upper() == "DATABASE":
        database = {}
        print("base de datos borrada")


    else:
        print("Error")
