
import dns.resolver

def dmarc(website):
    record = dns.resolver.resolve('_dmarc.'+ website , 'TXT')
    for line in record:
        if "DMARC1" in str(line): print ("------DMARC active-----")
        print(line)

def dkim(website, selector):
    record = dns.resolver.resolve(selector + "._domainkey." + website, 'TXT')
    for line in record:
        if "DKIM1" in str(line): print ("------DKIM active-----")
        print(line)

def spf(website):
    record = dns.resolver.resolve(website , 'TXT')
    for line in record:
        if "spf1" in str(line): print ("-----SPF active-----")
        print(line)


if __name__ == "__main__":
    dmarc("metroline.co.uk")
    dkim("metroline.co.uk", 'Selector2')
    spf("metroline.co.uk")
