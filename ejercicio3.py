inventario = []

while True:
    print("\n================ MENÚ ================")
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Ordenar productos alfabéticamente")
    print("6. Mostrar número total de productos")
    print("7. Salir")
    
    opcion = input("Seleccione una opción (1-7): ")
    
    if opcion == "1":
        
        producto = input("Ingrese el nombre del producto a agregar: ")
        inventario.append(producto)
        print(f"¡'{producto}' ha sido agregado con éxito!")
        
    elif opcion == "2":
        lote_texto = input("Ingrese los productos separados por comas: ")
        lote = lote_texto.split(",")
        for p in lote:
            inventario.append(p.strip())
        print("¡Lote agregado con éxito!")
        
    elif opcion == "3":
        producto = input("Ingrese el nombre exacto del producto a eliminar: ")
        if producto in inventario:
            inventario.remove(producto)
            print(f"'{producto}' ha sido eliminado del inventario.")
        else:
            print("El producto no se encuentra en el inventario.")
            
    elif opcion == "4":
        if len(inventario) > 0:
            eliminado = inventario.pop() 
            print(f"Se ha eliminado el producto más reciente: '{eliminado}'")
        else:
            print("El inventario está vacío, no hay nada que eliminar.")
            
    elif opcion == "5":
        inventario.sort()
        print("Inventario ordenado alfabéticamente:")
        print(inventario)
        
    elif opcion == "6":
        total = len(inventario)
        print(f"El número total de productos en el inventario es: {total}")
        
    elif opcion == "7":
        print("Saliendo del programa de inventario. ¡Hasta luego!")
        break
        
    else:
        print("Opción inválida. Por favor, elija un número entre 1 y 7.")