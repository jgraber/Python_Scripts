# from https://stackoverflow.com/questions/41620369/how-to-get-ssl-certificate-details-using-python
import socket
import ssl
from datetime import datetime
from typing import NamedTuple
from rich.console import Console
from rich.table import Table

domains = [
"ImproveAndRepeat.com",
"python.org",
"python-err.org"
]


class CertificateInfo(NamedTuple):
    domain: str
    expiry_date: datetime
    expires_in: int
    issuer: str
    
    def expires_on(self):
        return self.expiry_date.strftime('%Y-%m-%d')
 

def load_certificate(hostname):
    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )    
    conn.settimeout(5.0)
    
    conn.connect((hostname, 443))
    certificate = conn.getpeercert()
    return certificate


def read_certificate(hostname, certificate):
    date_format = r'%b %d %H:%M:%S %Y %Z'
    not_after = certificate['notAfter']
    expire_date = datetime.strptime(not_after, date_format)
    remaining = expire_date - datetime.now()

    # https://stackoverflow.com/a/30863209/532064
    issuer = dict(x[0] for x in certificate['issuer'])
    issued_by = issuer['organizationName']

    return CertificateInfo(hostname, expire_date, remaining.days, issued_by)


# if __name__ == "__main__":
#     for value in domains:
#         try:
#             certificate = load_certificate(value)
#             cert_info = read_certificate(value, certificate)
#             print(f"{cert_info.domain}, "\
#                 f"{cert_info.expires_on()}, "\
#                 f"{cert_info.expires_in}, "\
#                 f"{cert_info.issuer}"
#             )
#         except Exception as e:
#             print(f"{value} {e.strerror}")
        
        
if __name__ == "__main__":
    console = Console()

    table = Table(show_header=True, header_style="bold")
    table.add_column("Domain", style="dim")
    table.add_column("Expiry Date")
    table.add_column("Expires in (days)", justify="right")
    table.add_column("Issuer")
    
    for value in domains:
        try:
            certificate = load_certificate(value)
            cert_info = read_certificate(value, certificate)

            table.add_row(cert_info.domain, 
                          str(cert_info.expires_on()), 
                          str(cert_info.expires_in), 
                          cert_info.issuer)
        except Exception as e:
            table.add_row(value,"","",e.strerror)
    
    console.print(table)