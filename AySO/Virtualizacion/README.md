# Virtualización con VirtualBox — TPI

> **Materia:** Arquitectura y Sistemas Operativos  
> **Carrera:** Tecnicatura Universitaria en Programación a Distancia — UTN  
> **Alumno:** Gualla Mariano Guillermo | **Comisión:** 21  
> **Entrega:** 22/06/2026

---

## Descripción

Este repositorio contiene el informe del Trabajo Práctico Integrador sobre virtualización. El trabajo consiste en la implementación de un servidor web Apache sobre una máquina virtual con Ubuntu Server 26.04, utilizando VirtualBox como hipervisor tipo 2, y la verificación de su accesibilidad desde la red local.

---

## Contenido del repositorio

```text
Repositorio
├──  TPI_Virtualizacion.pdf   — Informe completo del trabajo práctico
├──  setup.sh                 — Comandos ejecutados en bash
└──  README.md                — Este archivo
```

---

## Tema: Virtualización

La virtualización es una tecnología que permite ejecutar múltiples sistemas operativos de forma simultánea sobre un mismo equipo físico, mediante la creación de máquinas virtuales administradas por un hipervisor.

En este trabajo se utilizó un **hipervisor tipo 2** (VirtualBox), que se instala como una aplicación dentro del sistema operativo anfitrión y permite crear y administrar máquinas virtuales desde un entorno de escritorio convencional.

---

## Caso práctico

**Objetivo:** implementar un servidor web Apache en una máquina virtual con Ubuntu Server y verificar su acceso desde la red local.

### Especificaciones de la VM

| Parámetro              | Valor               |
|------------------------|---------------------|
| Hipervisor             | Oracle VirtualBox   |
| Sistema operativo      | Ubuntu Server 26.04 |
| Memoria RAM            | 4 GB                |
| Almacenamiento         | 40 GB (VDI dinámico)|
| Controlador gráfico    | VBoxSVGA            |
| Red                    | Adaptador Bridge    |
| IP asignada            | 192.168.1.44        |

### Topología de red

```text
Internet
    │
  Router (192.168.1.1)
    │
    ├── PC Host — Windows 10 Home (192.168.1.100)
    │
    └── Ubuntu Server VM (192.168.1.44)
            └── Apache HTTP Server — puerto 80
```

### Comandos principales utilizados

```bash
# Actualizar repositorios
sudo apt update

# Instalar servidor SSH
sudo apt install openssh-server

# Habilitar firewall y permitir servicios
sudo ufw allow OpenSSH
sudo ufw allow 'Apache'
sudo ufw enable

# Instalar Apache
sudo apt install apache2

# Verificar estado del servicio
sudo systemctl status apache2 --no-pager

# Obtener IP de la VM
ip a
```

### Verificación desde Windows (host)

```cmd
ping 192.168.1.44
```

```text
Resultado:
  Paquetes enviados    = 4
  Paquetes recibidos   = 4
  Paquetes perdidos    = 0  (0% de pérdida)
```

Acceso web verificado ingresando `http://192.168.1.44` desde el navegador del host, visualizando la página predeterminada de Apache (*"It works!"*).

---

## Dificultades encontradas

**Error de controlador gráfico (vmwgfx)**  
Al iniciar Ubuntu 26.04 en VirtualBox, el sistema mostró errores relacionados con el driver vmwgfx, que no es compatible con VirtualBox. Se resolvió cambiando el controlador gráfico de `VMSVGA` a `VBoxSVGA` en la configuración de Pantalla de la VM.

**Perfil OpenSSH no encontrado**  
Al intentar ejecutar `sudo ufw allow OpenSSH`, el firewall no reconocía el perfil porque el servidor SSH no estaba instalado previamente. Se resolvió instalando `openssh-server` antes de configurar UFW.

---

## Video explicativo

https://www.youtube.com/watch?v=B1mufVx6HtQ&t=1s

---

## Bibliografía

```text
Apache Software Foundation. (s.f.). Apache HTTP Server Documentation.
  Recuperado el 19/06/2026 de https://httpd.apache.org/docs/

Canonical Ltd. (s.f.). Ubuntu Server Documentation.
  Recuperado el 19/06/2026 de https://ubuntu.com/server/docs

Oracle Corporation. (s.f.). Oracle VM VirtualBox User Manual.
  Recuperado el 19/06/2026 de https://www.virtualbox.org/manual/

Enferrel, A. (s.f.). Material de la asignatura Arquitectura y Sistemas Operativos.
  UTN — Tecnicatura Universitaria en Programación a Distancia.
```

---

## Datos académicos

```text
Coordinador        : Oscar Londero
Profesores adjuntos: Prof. David Rocco · Prof. Martin Aristiaran
                     Prof. Andrés Odiart · Prof. Mauricio Pasti
Tutor              : Jonathan Zárate
```
