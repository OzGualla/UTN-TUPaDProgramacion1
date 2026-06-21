#!/bin/bash
# Script de instalación — TPI Virtualización
# Gualla Mariano — UTN TUP Comisión 21
# Furfaro Ivan — UTN TUP Comisión 21

sudo apt update
sudo apt install -y openssh-server
sudo ufw allow OpenSSH
sudo apt install -y apache2
sudo ufw allow 'Apache'
sudo ufw enable
sudo systemctl enable apache2
echo "Instalación completa. IP del servidor:"
ip a | grep "inet " | grep -v 127.0.0.1