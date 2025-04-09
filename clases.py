# Sistema de Gestión de Bibliotecas con Herencia (POO en Python)

class Material:
    """Clase base para materiales de la biblioteca"""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info_basica(self):
        return f"'{self.titulo}' por {self.autor}"

class Libro(Material):
    """Hereda de Material y añade atributos específicos de libros"""
    def __init__(self, titulo, autor, isbn, editorial, año_publicacion):
        super().__init__(titulo, autor)  # Llama al constructor de Material
        self.isbn = isbn
        self.editorial = editorial
        self.año_publicacion = año_publicacion
        self.disponible = True

    def mostrar_info(self):
        return f"{self.mostrar_info_basica()} ({'Disponible' if self.disponible else 'Prestado'})"

class Persona:
    """Clase base para personas relacionadas con la biblioteca"""
    def __init__(self, id_persona, nombre, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

class Usuario(Persona):
    """Hereda de Persona y añade funcionalidad de préstamos"""
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)  # Llama al constructor de Persona
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            self.libros_prestados.append(libro)
            libro.disponible = False
            print(f"\n Libro '{libro.titulo}' prestado a {self.nombre}.")
        else:
            print("\n El libro no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.disponible = True
            print(f"\n📖 Libro '{libro.titulo}' devuelto por {self.nombre}.")
        else:
            print("\n Este usuario no tiene prestado ese libro.")

class Bibliotecario(Persona):
    """Hereda de Persona y añade permisos administrativos"""
    def __init__(self, id_bibliotecario, nombre, email):
        super().__init__(id_bibliotecario, nombre, email)
        self.permisos_administrativos = True

    def añadir_libro(self, biblioteca, libro):
        biblioteca.libros.append(libro)
        print(f"Libro '{libro.titulo}' añadido al sistema.")

    def eliminar_libro(self, biblioteca, libro):
        if libro in biblioteca.libros:
            biblioteca.libros.remove(libro)
            print(f"Libro '{libro.titulo}' eliminado del sistema.")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.bibliotecarios = []

    def registrar_usuario(self):
        print("\n Registro de Usuario:")
        id_usuario = input("ID de usuario: ")
        nombre = input("Nombre: ")
        email = input("Email: ")
        self.usuarios.append(Usuario(id_usuario, nombre, email))
        print(f"Usuario {nombre} registrado con éxito.")

    def añadir_libro(self):
        print("\n Añadir Libro:")
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        editorial = input("Editorial: ")
        año = input("Año de publicación: ")
        self.libros.append(Libro(titulo, autor, isbn, editorial, año))
        print(f"Libro '{titulo}' añadido.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None

    def menu_principal(self):
        while True:
            print("\n **Sistema de Biblioteca**")
            print("1. Registrar Usuario")
            print("2. Añadir Libro")
            print("3. Prestar Libro")
            print("4. Devolver Libro")
            print("5. Listar Libros")
            print("6. Registrar Bibliotecario")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.añadir_libro()
            elif opcion == "3":
                self.gestion_prestamo()
            elif opcion == "4":
                self.gestion_devolucion()
            elif opcion == "5":
                self.listar_libros()
            elif opcion == "6":
                self.registrar_bibliotecario()
            elif opcion == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def registrar_bibliotecario(self):
        print("\n Registro de Bibliotecario:")
        id_biblio = input("ID de bibliotecario: ")
        nombre = input("Nombre: ")
        email = input("Email: ")
        self.bibliotecarios.append(Bibliotecario(id_biblio, nombre, email))
        print(f"Bibliotecario {nombre} registrado con éxito.")

    def gestion_prestamo(self):
        print("\n Préstamo de Libro:")
        nombre_usuario = input("Nombre del usuario: ")
        usuario = self.buscar_usuario(nombre_usuario)
        if not usuario:
            print(" Usuario no registrado.")
            return

        titulo_libro = input("Título del libro a prestar: ")
        libro = self.buscar_libro(titulo_libro)
        if not libro:
            print(" Libro no encontrado.")
            return

        usuario.prestar_libro(libro)

    def gestion_devolucion(self):
        print("\n Devolución de Libro:")
        nombre_usuario = input("Nombre del usuario: ")
        usuario = self.buscar_usuario(nombre_usuario)
        if not usuario:
            print(" Usuario no registrado.")
            return

        titulo_libro = input("Título del libro a devolver: ")
        libro = self.buscar_libro(titulo_libro)
        if not libro:
            print(" Libro no encontrado.")
            return

        usuario.devolver_libro(libro)

    def listar_libros(self):
        print("\n **Libros Disponibles**")
        if not self.libros:
            print("No hay libros registrados.")
        for libro in self.libros:
            print(f"- {libro.mostrar_info()}")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    print("¡Bienvenido al Sistema de Gestión de Biblioteca!")
    biblioteca.menu_principal()