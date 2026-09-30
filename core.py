PATH_HOSTS = "/etc/hosts"
START_MARKER = "# --- BEGIN HOSTS MANAGER ---"
END_MARKER = "# --- END HOSTS MANAGER ---"

def get_managed_hosts() -> list:
    """
    Lee /etc/hosts y devuelve únicamente las líneas de IP/Dominio
    que están dentro de nuestros marcadores de control.
    """
    managed_lines = []
    inside_block = False

    try:
        with open(PATH_HOSTS, 'r') as file:
            for line in file:
                clean_line = line.strip()
                
                # Si encontramos el inicio, todo lo que venga después es nuestro
                if clean_line == START_MARKER:
                    inside_block = True
                    continue
                
                # Si encontramos el fin, dejamos de leer
                if clean_line == END_MARKER:
                    inside_block = False
                    break
                
                # Si estamos dentro del bloque y la línea no está vacía ni es otro comentario
                if inside_block and clean_line and not clean_line.startswith('#'):
                    managed_lines.append(clean_line)
                    
    except FileNotFoundError:
        print(f"[!] Error: No se pudo encontrar el archivo en {PATH_HOSTS}")
    except PermissionError:
        print("[!] Error: Permisos insuficientes para leer el archivo.")
        
    return managed_lines


def list_hosts():
    """
    Obtiene los dominios gestionados y los muestra en la terminal
    con un formato de tabla limpio y ordenado.
    """
    hosts = get_managed_hosts()
    
    if not hosts:
        print("\n[*] No hay dominios registrados por la herramienta todavía.")
        return

    print("\n" + "="*45)
    print(f"{'DIRECCIÓN IP':<18} | {'DOMINIO':<25}")
    print("="*45)
    
    for host in hosts:
        # split() sin argumentos divide por cualquier cantidad de espacios
        parts = host.split() 
        
        if len(parts) >= 2:
            ip = parts[0]
            domain = parts[1]
            # Usamos alineación a la izquierda (<) para que quede perfecto
            print(f"{ip:<18} | {domain:<25}")
            
    print("="*45)


def add_host(ip: str, domain: str):
    """
    Añade un nuevo mapeo de IP y dominio dentro de los marcadores.
    Si los marcadores no existen, los crea al final del archivo.
    """
    new_entry = f"{ip}\t{domain}\n"
    
    try:
        # 1. Leer todo el contenido actual en memoria
        with open(PATH_HOSTS, 'r') as file:
            lines = file.readlines()
            
        # Limpiamos saltos de línea para buscar los marcadores con precisión
        clean_lines = [line.strip() for line in lines]
        
        # 2. Comprobar si los marcadores ya existen
        if END_MARKER in clean_lines:
            # Encontramos la posición del marcador de fin
            index = clean_lines.index(END_MARKER)
            
            # Insertamos la nueva entrada justo antes del marcador de fin
            # (Aseguramos que termine en salto de línea)
            lines.insert(index, f"{ip}\t{domain}\n")
            print(f"[+] Insertando dominio en el bloque existente...")
        else:
            # Si no existen, los preparamos para añadirlos al final
            print(f"[*] Configurando bloques de control por primera vez...")
            # Nos aseguramos de que la última línea existente tenga un salto de línea
            if lines and not lines[-1].endswith('\n'):
                lines[-1] += '\n'
                
            lines.append(f"{START_MARKER}\n")
            lines.append(new_entry)
            lines.append(f"{END_MARKER}\n")
            
        # 3. Reescribir el archivo con los cambios aplicados
        with open(PATH_HOSTS, 'w') as file:
            file.writelines(lines)
            
        print(f"[+] Éxito: Se ha vinculado {domain} a la IP {ip}.")
        
    except PermissionError:
        print("[!] Error: No tienes permisos de escritura en /etc/hosts. (¿Olvidaste el sudo?)")
    except Exception as e:
        print(f"[!] Ocurrió un error inesperado: {e}")


def delete_host(domain: str) -> bool:
    """
    Busca un dominio dentro del bloque gestionado y lo elimina.
    Devuelve True si lo borró, False si no lo encontró.
    """
    domain = domain.strip().lower()
    found = False
    
    try:
        with open(PATH_HOSTS, 'r') as file:
            lines = file.readlines()
            
        new_lines = []
        inside_block = False
        
        for line in lines:
            clean_line = line.strip()
            
            if clean_line == START_MARKER:
                inside_block = True
                new_lines.append(line)
                continue
            if clean_line == END_MARKER:
                inside_block = False
                new_lines.append(line)
                continue
                
            # Si estamos dentro de nuestro bloque, comprobamos si contiene el dominio
            if inside_block and clean_line and not clean_line.startswith('#'):
                parts = clean_line.split()
                if len(parts) >= 2 and parts[1].lower() == domain:
                    found = True
                    continue # Saltamos esta línea (la eliminamos de la lista final)
            
            # Conservamos el resto de las líneas
            new_lines.append(line)
            
        if found:
            with open(PATH_HOSTS, 'w') as file:
                file.writelines(new_lines)
            print(f"[+] Éxito: El dominio '{domain}' ha sido eliminado.")
        else:
            print(f"[!] No se encontró el dominio '{domain}' en la sección gestionada.")
            
        return found

    except PermissionError:
        print("[!] Error: Permisos insuficientes para modificar /etc/hosts.")
        return False
    
def update_host(ip: str, domain: str):
    """
    Modifica la IP de un dominio existente reutilizando la lógica
    de borrado y adición.
    """
    print(f"[*] Buscando '{domain}' para actualizar su IP a {ip}...")
    
    # Intentamos borrar el dominio primero
    was_deleted = delete_host(domain)
    
    if was_deleted:
        # Si se borró con éxito, lo añadimos con la nueva IP
        add_host(ip, domain)
        print(f"[+] Éxito: Registro actualizado correctamente.")
    else:
        print(f"[!] No se pudo actualizar porque el dominio no existía.")