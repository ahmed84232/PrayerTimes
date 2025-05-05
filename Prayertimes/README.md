# 🕌 Prayer Times Fetcher

A Python script that retrieves daily Islamic prayer times (Fajr, Duha, Dhuhr, Asr, Maghrib, Isha) using your current IP address and geographic coordinates.

---

## 📦 Requirements

- Python 3.6+
- `requests` library

Install the required library using pip:

```bash
pip install requests
```

---

## ⚙️ Configuration

Create a file named `config.txt` in the root directory with the following format:

```
latitude=YOUR_LATITUDE
longitude=YOUR_LONGITUDE
```

Example:

```
latitude=30.0444
longitude=31.2357
```

---

## 🚀 Usage

Run the script using:

```bash
python prayer_times.py
```

The script will:
- Detect your IP address automatically.
- Use your coordinates and the IP to request prayer times from [IslamicFinder.us](https://www.islamicfinder.us).
- Print formatted prayer times to the terminal.
- Stay alive with a long sleep loop (use `Ctrl+C` to exit).

---

## 🧠 Example Output

```
AL-Fajr: 04:17AM
AL- DUHA: 05:47AM
Al-DUHR: 12:00PM
AL- ASR: 03:30PM
AL- MAGHRIB: 06:45PM
AL- ISHA: 08:05PM
```

---

## 🛑 Stopping the Script

To stop the script, press:

```
Ctrl + C
```

---

## 📜 License

This project is open source and free for everyone to use and modify.
