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




