import socket as s
import time
import dns.resolver as ds
import requests
import pandas as pd

in_csv = pd.read_csv('input_fqdn.csv')
arr =[]
 
for i in in_csv['FQDN'].values:
    try:
        ip = s.gethostbyname(i.strip())
        if ip:
            result = ds.resolve(i.strip(), 'A')
            dns_time_ms = result.response.time * 1000
            response = requests.get('http://{}'.format(i.strip()), timeout=5)
            http_handshake_time_ms = response.elapsed.total_seconds() * 1000
            print("{} {} {} {}".format(i, ip, dns_time_ms, http_handshake_time_ms))
            arr.append([i.strip(), ip, round(dns_time_ms, 2), round(http_handshake_time_ms, 2)])
           
    except (s.gaierror, requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
        print("Error: Could not resolve hostname {}".format(i.strip()))

df = pd.DataFrame(arr,columns=['FQDN', 'IP', 'DNS_Time_ms', 'HTTP_Handshake_Time_ms'])
df.to_csv('output_fqdn.csv', index=False)