Network Scanner with Vulnerability Extraction

Description:
--------------
This is a simple network scanner tool written in Python. It can be used to scan a host for open ports and extract vulnerabilities from a web server running on ports 80 (HTTP) or 443 (HTTPS).

Usage:
--------------
To use the network scanner, run the following command in your terminal:

python scanner.py <host> <start_port> [<end_port>]

- <host>: The host to scan (either an IP address or a domain name).
- <start_port>: The starting port number for the scan.
- [<end_port>]: Optional. The ending port number for the scan. If not provided, only the start port will be scanned.

Examples:
--------------
1. Scan a host on ports 80 to 100:
python scanner.py example.com 80 100

2. Scan a host on port 443 only:
python scanner.py example.com 443

3. Scan a host on port 8080:
python scanner.py example.com 8080

Dependencies:
--------------
- Python 3.x
- BeautifulSoup (bs4)
- Requests

Installation:
--------------
1. Make sure you have Python installed on your system. You can download it from https://www.python.org/downloads/.

2. Install the required dependencies using pip:
pip install beautifulsoup4 requests

3. Download the scanner.py file and run it using Python.

Author:
--------------
[Pascal]
