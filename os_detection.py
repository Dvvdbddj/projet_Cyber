import nmap
import json

nm = nmap.PortScanner()
nm.scan("192.168.X.XX", arguments="-O")
print(json.dumps(nm._scan_result, indent=2))



