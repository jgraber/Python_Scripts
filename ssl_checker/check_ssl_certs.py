# from https://stackoverflow.com/questions/41620369/how-to-get-ssl-certificate-details-using-python
import socket
import ssl
import datetime
from rich.console import Console
from rich.table import Table

domains_url = [
"jgraber.ch",
"ImproveAndRepeat.com",
"ImproveRepeat.com"
]

def ssl_expiry_datetime(hostname):
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 5 second timeout
    conn.settimeout(5.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # https://stackoverflow.com/a/30863209/532064
    issuer = dict(x[0] for x in ssl_info['issuer'])
    issued_by = issuer['organizationName']
    # print(ssl_info)
    # Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat), issued_by

if __name__ == "__main__":
    # see https://improveandrepeat.com/2022/07/python-friday-132-rich-tables-for-your-terminal-apps/
    
    console = Console()

    table = Table(show_header=True, header_style="bold")
    table.add_column("Domain", style="dim")
    table.add_column("Expiry Date")
    table.add_column("Expires in \[days]", justify="right")
    table.add_column("Issuer")
    
    for value in domains_url:
        now = datetime.datetime.now()
        try:
            expire, issuer = ssl_expiry_datetime(value)
            diff = expire - now
            table.add_row(value, str(expire.strftime('%Y-%m-%d')), str(diff.days), issuer)
            # print (f"Domain name: {value} \t\t Expiry Date: {} \t Expiry Day: {} \t Issuer: {}")
        except Exception as e:
            # print(dir(e))
            table.add_row(value,"","",e.strerror)
    
    console.print(table)
