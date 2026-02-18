# 🔐 NTS Advanced Port Scanner

A multi-threaded TCP port scanner built using Python for educational cybersecurity purposes.

This tool scans a custom port range, detects open ports, performs basic service identification, and attempts banner grabbing.

---

## 🚀 Features

- ⚡ Multi-threaded fast scanning
- 🎯 Custom port range selection
- 🔎 Service detection (common ports)
- 🏷️ Banner grabbing
- 📝 Scan result logging to file
- ⏱️ Scan duration tracking
- 🎨 Colored terminal output

---

## 🧠 How It Works

The scanner performs a TCP Connect Scan by attempting a full TCP handshake using Python's `socket.connect_ex()` method.

For each open port:
- It identifies common services using `socket.getservbyport()`
- Attempts to grab banner information
- Logs results to `scan_results.txt`

---

## 🛠️ Technologies Used

- Python 3
- socket module
- threading module
- queue module
- datetime module

---

## 📌 Installation & Usage

1. Clone the repository:

git clone https://github.com/yourusername/narreshtamilselvan.git

css
Copy code

2. Navigate to the folder:

cd nts-port-scanner

markdown
Copy code

3. Run the script:

python port_scanner.py

yaml
Copy code

4. Enter:
- Target IP
- Start Port
- End Port
- Number of Threads

---

## 🖥️ Example Output

[OPEN] Port 22 | Service: ssh | Banner: OpenSSH_8.2p1
[OPEN] Port 80 | Service: http | Banner: Apache/2.4.41

yaml
Copy code

---

## 📚 What I Learned

- TCP handshake fundamentals
- Multi-threading concepts
- Thread-safe queue handling
- Banner grabbing techniques
- Network reconnaissance basics
- Ethical cybersecurity practices

---

## ⚠️ Disclaimer

This project is created strictly for educational and ethical cybersecurity practice.

Only scan systems you own or have explicit permission to test.

---

## 👨‍💻 Author

Narresh Tamilselvan  
First Year Cyber Security Student  
