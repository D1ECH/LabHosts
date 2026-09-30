import sys
from cli import show_main_menu, ask_host_inputs
from utils import check_root_privileges
import core as core

def main():
    print("\n" + "="*50)
    print("      🚀 BIENVENIDO A HTB/THM LABHOSTS 🚀      ")
    print("="*50)
    
    while True:
        try:
            # 1. Mostramos el menú interactivo con flechas
            choice = show_main_menu()
            
            # 2. Evaluamos la opción seleccionada
            if '[x] Salir' in choice:
                print("\n[+] ¡Hasta luego! Buenas prácticas en tu auditoría. 🚀\n")
                break
                
            elif '[+] Añadir' in choice:
                if check_root_privileges():
                    datos = ask_host_inputs()
                    # Pasamos los datos recolectados por inquirer al core
                    core.add_host(datos['ip'], datos['domain'])
                
            elif '[*] Modificar' in choice:
                if check_root_privileges():
                    # Reutilizamos el prompt que pide IP y Dominio
                    datos = ask_host_inputs()
                    core.update_host(datos['ip'], datos['domain'])
                    
            elif '[-] Eliminar' in choice:
                if check_root_privileges():
                    # Para eliminar solo necesitamos el dominio, pero podemos usar inquirer text
                    import inquirer
                    question = [inquirer.Text('domain', message="Introduce el dominio a eliminar")]
                    answer = inquirer.prompt(question)
                    core.delete_host(answer['domain'])
                    
            elif '[=] Listar' in choice:
                # Listar solo lee el bloque, no requiere estrictamente sudo
                core.list_hosts()

            # Pausa estética para que el usuario lea el resultado antes de limpiar o volver a pintar el menú
            input("\n[ Presiona Enter para volver al menú ]")
            
        except KeyboardInterrupt:
            # Capturamos un Ctrl+C para que no rompa feo la terminal
            print("\n\n[!] Saliendo de la aplicación de forma segura...")
            sys.exit(0)

if __name__ == "__main__":
    main()