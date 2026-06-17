# Network Scanner — nmap + Python

Scripts Python pour scanner un réseau local, réalisés en projet perso avant mon entrée à Epitech.
L'idée est de découvrir comment fonctionne le scan réseau en incluant nmap dans des scripts Python.  
Projet réalisé sur Raspberry Pi OS (basé sur Debian)  
(A utiliser uniquement sur un reseau perso)



## Prérequis


bash:
pip install python-nmap

nmap doit aussi être installé sur la machine :

bash:
Debian / Ubuntu:  
sudo apt install nmap




## Scripts

### scanner_routeur.py — Scanner le réseau

Liste toutes les machines connectées sur le réseau local avec leur IP, hostname et état.

import nmap

def wifi_ip(reseau):
    nm = nmap.PortScanner()
    nm.scan(reseau, arguments="-F -T4")
    hotes = nm.all_hosts()
    print(f"{len(hotes)} hôtes trouvés\n")
    for ip in hotes:
        hostname = nm[ip].hostname() or "inconnu"
        state = nm[ip].state()
        print(f"{ip:<16} {hostname:<20} {state}")

wifi_ip("192.168.X.X/24")
bash
python wifi_scanner.py

Exemple de sortie :

5 hôtes trouvés

192.168.1.1     routeur.local        up  
192.168.1.10    mon-pc               up  
192.168.1.22    inconnu              up  
...



### os_detection.py — Détection du système d'exploitation

Analyse un hôte précis et essaie de déterminer son OS. Nécessite les droits root.
pour passer les droits root utiliser sudo:  
sudo /usr/bin/python3 os_detection.py

import nmap
import json

nm = nmap.PortScanner()
nm.scan("192.168.X.XX", arguments="-O")
print(json.dumps(nm._scan_result, indent=2))

Le résultat est affiché en JSON avec toutes les infos retournées par nmap (OS détecté, ports, TTL...).



## Utilisation typique

- Lancer os_detection.py pour voir toutes les IPs actives sur le réseau
- La renseigner dans os_detection.py et lancer le scan approfondi



## Resources
(documentation python-nmap)  
-https://pypi.org/project/python-nmap/      
-https://xael.org/pages/python-nmap.html  


