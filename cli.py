import inquirer

def show_main_menu() -> str:
    """Muestra el menú de flechas y retorna la opción seleccionada."""
    questions = [
        inquirer.List(
            'menu_choice',
            message="¿Qué acción deseas realizar?",
            choices=[
                '[+] Añadir nuevo dominio/IP',
                '[*] Modificar dominio existente',
                '[-] Eliminar un dominio',
                '[=] Listar dominios registrados',
                '[x] Salir'
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    return answers['menu_choice']

def ask_host_inputs():
    """Pide al usuario la IP y el dominio para las operaciones de alta/modificación."""
    questions = [
        inquirer.Text('ip', message="Introduce la dirección IP (ej. 10.10.10.10)"),
        inquirer.Text('domain', message="Introduce el dominio (ej. machine.htb)")
    ]
    return inquirer.prompt(questions)