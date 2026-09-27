database = {}


while True:
    command = input("MiniSQL > ")

    if command.lower() == "exit":
        break

    if command.lower() == "show database":
        print(database)
        continue

    parts = command.split()

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