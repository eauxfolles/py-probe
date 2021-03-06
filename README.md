# py-probe
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

PoC/Alpha of a tool written in Python which allows to check if domains (loaded from list) are resolving, i.e. are active.

Tool loads external file including names of domains (potentially identified via https://github.com/OWASP/Amass and similar tools) and probes if they are available. Tested under Windows. 

***Usage:*** "pyprobe.py \<source> \<target>"

Where: 
* \<source> is file including domains to be checked. No heading protocol (http:// or https://). Located in same folder as the script. 
* \<target> is file to which validated list should be written. 

P.S. This tool is inspired by the work of Tom Hudson (https://github.com/tomnomnom) on httprobe (https://github.com/tomnomnom/httprobe).
