## juicy_dirs

for i in $(cat list); do python3 dirsearch.py -w juicy_dirs.txt -u $i; done

#### 80 443

for i in $(cat ips.txt); do python3 dirsearch.py -w juicy_dirs.txt -u http://$i; python3 dirsearch.py -w juicy_dirs.txt -u https://$i; done | tee dirsearch_juicy_ips80443.txt

for i in $(cat subdomains.txt); do python3 dirsearch.py -w juicy_dirs.txt -u http://$i; python3 dirsearch.py -w juicy_dirs.txt -u https://$i; done | tee dirsearch_juicy_subdomains_80443.txt

#### 80 443 8080 8443

for i in $(cat ips.txt); do python3 dirsearch.py -w juicy_dirs.txt -u http://$i; python3 dirsearch.py -w juicy_dirs.txt -u https://$i; python3 dirsearch.py -w juicy_dirs.txt -u http://$i:8080; python3 dirsearch.py -w juicy_dirs.txt -u https://$i:8443; done | tee dirsearch_juicy_ips8044380808443.txt

for i in $(cat subdomains.txt); do python3 dirsearch.py -w juicy_dirs.txt -u http://$i; python3 dirsearch.py -w juicy_dirs.txt -u https://$i; python3 dirsearch.py -w juicy_dirs.txt -u http://$i:8080; python3 dirsearch.py -w juicy_dirs.txt -u https://$i:8443; done | tee dirsearch_juicy_subdomains8044380808443.txt


-------------------------------------------

## juicy_ports

nmap -p 1090,1098,1099,4444,11099,47001,47002,10999,7000-7004,8000-8003,9000-9003,9503,7070,7071,45000,45001,8686,9012,50500,4848,11111,4444,4445,4786,5555,5556

Java RMI: 1090,1098,1099,4444,11099,47001,47002,10999

WebLogic: 7000-7004,8000-8003,9000-9003,9503,7070,7071

JDWP: 45000,45001

JMX: 8686,9012,50500

GlassFish: 4848

jBoss: 11111,4444,4445

Cisco Smart Install: 4786

HP Data Protector: 5555,5556
