# Nombre del paquete: pyfiglet

# Propósito: Este paquete proporciona una forma fácil de crear texto ASCII art utilizando fuentes personalizadas.

# Lista de principales funciones:

# figlet_format(text, font=None, **kwargs): Crea texto ASCII art a partir del texto especificado y la fuente especificada (o la fuente predeterminada si no se especifica ninguna).
# get_figlet_font(font_name): Devuelve la ruta de acceso a la fuente especificada.
# Ejemplo en código de su utilización:

import pyfiglet

# Obtener la ruta de la fuente "slant"
font_path = pyfiglet.get_figlet_font("slant")

# Crear texto ASCII art utilizando la fuente "slant"
ascii_art = pyfiglet.figlet_format("Hello, world!", font=font_path)

# Imprimir el texto ASCII art
print(ascii_art)

