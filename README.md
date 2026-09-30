# 🚀 LabHosts

> Gestor de `/etc/hosts` con menú interactivo para laboratorios de pentesting (HackTheBox, TryHackMe, etc.)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey?logo=linux)](https://github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![HTB](https://img.shields.io/badge/HTB-Ready-red)](https://www.hackthebox.com/)
[![THM](https://img.shields.io/badge/THM-Ready-orange)](https://tryhackme.com/)

---

## 📖 ¿Qué es LabHosts?

**LabHosts** es una herramienta de terminal escrita en Python que te permite **añadir, modificar, listar y eliminar** entradas en tu archivo `/etc/hosts` sin tocar nada más del sistema.

Ideal para:
- 🎯 Máquinas de **HackTheBox** y **TryHackMe**
- 🧪 Laboratorios de pentesting locales
- 🔧 Cualquier entorno donde gestiones múltiples mapeos IP ↔ dominio

## ✨ Características

- 🖱️ **Menú interactivo con flechas** (gracias a `inquirer`)
- 🛡️ **Bloque aislado de control**: todas tus entradas se guardan entre marcadores propios, sin tocar las líneas originales del sistema
- ➕ Añadir nuevos mapeos IP/dominio
- ✏️ Modificar la IP de un dominio existente
- 🗑️ Eliminar entradas de forma segura
- 📋 Listar entradas en tabla limpia y ordenada
- ⚡ Creación automática de bloques de control si no existen
- 🔐 Verificación de privilegios root (`sudo`)

## 📸 Vista previa

```
==================================================
      🚀 BIENVENIDO A HTB/THM LABHOSTS 🚀
==================================================

? ¿Qué acción deseas realizar?
❯ [+] Añadir nuevo dominio/IP
  [*] Modificar dominio existente
  [-] Eliminar un dominio
  [=] Listar dominios registrados
  [x] Salir
```

```
=============================================
DIRECCIÓN IP       | DOMINIO
=============================================
10.10.10.10        | machine.htb
10.10.11.5         | target.thm
=============================================
```

## 🧩 Arquitectura

```
labhosts/
├── main.py    # Punto de entrada y bucle del menú principal
├── cli.py     # Interfaz interactiva (menús y prompts con inquirer)
├── core.py    # Lógica de gestión de /etc/hosts
└── utils.py   # Utilidades (verificación de root, validación de IP)
```

## 🚀 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/labhosts.git
cd labhosts

# 2. Instalar dependencias
pip install inquirer
```

> 💡 En Python 3.12+, `inquirer` requiere la rama de desarrollo si hay problemas:
> ```bash
> pip install inquirer@git+https://github.com/magmax/python-inquirer
> ```

## 💻 Uso

**Importante:** para escribir en `/etc/hosts` necesitas privilegios de administrador.

```bash
sudo python3 main.py
```

| Opción | Descripción |
|--------|-------------|
| `[+] Añadir nuevo dominio/IP` | Registra un nuevo mapeo IP → dominio |
| `[*] Modificar dominio existente` | Actualiza la IP de un dominio registrado |
| `[-] Eliminar un dominio` | Elimina un dominio del bloque gestionado |
| `[=] Listar dominios registrados` | Muestra todas las entradas en formato tabla |
| `[x] Salir` | Cierra la herramienta |

## 🔧 ¿Cómo funciona el bloque aislado?

LabHosts marca todas sus entradas con comentarios especiales en `/etc/hosts`:

```bash
# --- BEGIN HOSTS MANAGER ---
10.10.10.10	machine.htb
10.10.11.5	target.thm
# --- END HOSTS MANAGER ---
```

✅ **Ventajas:**
- Nunca se toca el resto del archivo (`localhost`, `127.0.1.1`, etc.)
- Puedes desinstalar todo borrando solo el bloque
- Fácil identificación de qué entradas son tuyas

## 🗺️ Roadmap

- [ ] Validación de formato IP y dominio (`utils.is_valid_ip`)
- [ ] Soporte para múltiples dominios en la misma IP (`1.2.3.4 a.htb b.htb`)
- [ ] Búsqueda/filtro en el listado
- [ ] Exportar/importar configuración de hosts
- [ ] Soporte para Windows (`C:\Windows\System32\drivers\etc\hosts`)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un bug o tienes una idea:

1. 🍴 Haz un fork del proyecto
2. 🌿 Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. ✅ Haz commit de tus cambios (`git commit -m 'feat: añade X'`)
4. 📤 Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. 🔃 Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [`LICENSE`](LICENSE) para más información.

---

<p align="center">
  Hecho con ☕ y Python para la comunidad de CTF y pentesting 🐧🔐
</p>
