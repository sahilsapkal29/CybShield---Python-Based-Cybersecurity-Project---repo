import socket
from datetime import datetime

def check_host(target):
   try:
       socket.gethostbyname(target)
       return True
   except:
       return False
[]

def scan_ports(target, ports):
   open_ports = []

   print(f"\nStarting scan on {target}")
   print(f"Time: {datetime.now()}\n")

   for port in ports:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.settimeout(0.5)

       result = s.connect_ex((target, port))

       if result == 0:
           try:
               service = socket.getservbyport(port)
           except:
               service = "Unknown"

           print(f"[OPEN] Port {port} → {service}")
           open_ports.append(port)

       s.close()

   print("\nScan Finished!")
   print("Open Ports:", open_ports)


# Main
target = input("Enter Target IP/Domain: ")

if check_host(target):
   ports = list(range(1, 1025))  # Common ports
   scan_ports(target, ports)
else:
   print("Host is not reachable!")          
   