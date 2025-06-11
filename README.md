# 🛠️ port-scanner
A simple Python-based port scanner for cybersecurity learning. Scans the first 1024 ports of an IP address to identify open ports, does this by attempting to connect to a port and observing the response. Useful in deepening the understanding of how newtork services really work! A very useful tool for vulnerability scanning in cyber security! Note: it may be a bit slow. For faster results, you can reduce the connection timeout within the script.

# 📌 Features
- Scans ports 1–1024 of a given IP address
- Prints open ports
- Handles errors like unknown host and keyboard interruption

# ✅ Prerequisites
- Python 3.x
- pyfiglet module
  


# 📘 Lessons Learned
- Got practical with socket programming and how port scanning works at a low level
- Thought about out how to handle exceptions like timeouts and hostname errors properly (improving the UI).
- Realised that scanning sequentially is slow — planning to explore threading (parallel execution/pipelining)
- Applied my Python and GitHub skills to a working cyber security tool. 
- First step towards building out a full cybersecurity toolset (keep an eye out for more tools and a general tool that includes all the small tools joined together. 

# ⚠️ Disclaimer
This tool is intended only for educational and authorized testing purposes. Do not use it to scan networks without permission.
