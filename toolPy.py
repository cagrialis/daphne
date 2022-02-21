import os
from urllib import parse

def terminalCommands(url):
    nmapCommand = 'nmap -sS -sV -oN "test-results/nmap.txt" ' + parse.urlsplit(url).netloc
    niktoCommand = 'nikto -h '+ parse.urlsplit(url).netloc+ ' -output "test-results/nikto.txt" '
    nucleiCommand = 'nuclei -list success-subdomain.txt -o "test-results/nuclei.txt" '

    os.system(nmapCommand)
    os.system(nucleiCommand)
    os.system(niktoCommand)