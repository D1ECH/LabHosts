import os

def check_root_privileges() -> bool:
    """Verifica si el usuario tiene permisos de administrador (UID 0)."""
    if os.getuid() != 0:
        print("\n[!] Esta acción requiere privilegios de administrador.")
        print("[*] Por favor, ejecuta la herramienta usando 'sudo'.\n")
        return False
    return True

def is_valid_ip(ip: str) -> bool:
    """Opcional: Aquí podrías validar si el string es una IP válida antes de guardarla."""
    # Por ahora retorna True, la implementaremos más adelante
    return True