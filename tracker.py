import requests
import os

def limpiar():
    os.system('clear')

def banner():
    # Esto genera el título grande estilo Linux
    os.system('figlet -c IP TRACKER BY SAID')
    print("="*60)

def rastrear(ip=""):
    # Usamos ip-api.com que es gratuita y rápida
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,isp,org,as,query"
    try:
        data = requests.get(url).json()
        if data['status'] == 'success':
            print(f"\n[+] Resultados para: {data['query']}")
            print(f"------------------------------------")
            print(f"País:      {data['country']}")
            print(f"Ciudad:    {data['city']}")
            print(f"Región:    {data['regionName']}")
            print(f"C. Postal: {data['zip']}")
            print(f"ISP:       {data['isp']}")
            print(f"Org:       {data['org']}")
            print(f"ASN:       {data['as']}")
            print(f"------------------------------------")
        else:
            print(f"\n[!] Error: {data.get('message', 'IP no válida')}")
    except Exception as e:
        print(f"\n[!] Error de conexión: {e}")

limpiar()
banner()
print("1. Rastrear mi propia IP")
print("2. Rastrear una IP específica")
opcion = input("\nSeleccione una opción: ")

if opcion == "1":
    print("\nEscaneando tu ubicación...")
    rastrear()
elif opcion == "2":
    ip_target = input("Pon la IP que deseas rastrear: ")
    print(f"Escaneando {ip_target}...")
    rastrear(ip_target)
else:
    print("Opción inválida.")

