from proxy_randomizer import RegisteredProviders
import sys
import requests
from termcolor import colored

proxy = []
logo="  ___ ___ __    \n /__//__\\/ /\\/ Gen\n/   /  \\/_/ /\\ @KuliOnline0011 \n"

def gen():
    try:
        print(colored(logo,"magenta"))
        uwu = int(sys.argv[1])
        rp = RegisteredProviders()
        a = 0
        rp.parse_providers()
        for TtT in rp.proxies:
            a += 1
            if a <= uwu:
                prox = {"http": TtT.get_proxy()}
                respon = requests.get("https://google.com", proxies=prox)
                if respon.status_code == 200:
                    proxy.append(TtT)
                else:
                    print(TtT, "Tidak dapat digunakan")
            else:
                break
        
        hasil = []
        for huhu in proxy:
            hai = str(huhu).split( )
            hasil.append(hai[0])        
        return hasil
    
    except requests.ConnectionError:
        print("Koneksi sedang trouble")

if len(sys.argv) < 2:
    print(colored(logo,"magenta"))
    print("Bantuan:\n        proxyGen.py -h\n")
elif str(sys.argv[1]) == "-h":
    print(colored(logo,"magenta"))
    print("Panduan:\n -o    output file\nPenggunaan:\n      proxyGen.py [Jumlah Proxy]\n      proxyGen.py [Jumlah Proxy] -o [output file]\n")
elif len(sys.argv) > 2:
    if str(sys.argv[2]) == "-o":
        namafile=str(sys.argv[3])
        hai = gen()
        file = open(namafile,'w')
        for uwu in hai:
            file.write(str(uwu)+"\n")
        file.close()
        print(f"Output berhasil disimpan dengan nama {namafile}\n")
        
    else:
        pass
else:
    yuhu = gen()
    for hh in yuhu:
        print(hh)
    print(" ")