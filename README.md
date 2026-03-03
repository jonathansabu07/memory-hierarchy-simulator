 Memory Hierarchy Simulator (LRU + Hit/Miss Statistics)

A GUI-based Memory Hierarchy Simulator built using Python and Tkinter that demonstrates how Cache, RAM, and Secondary Storage interact using the LRU (Least Recently Used) replacement policy.

This project visually simulates data access operations and tracks cache performance metrics such as hit ratio, miss ratio, and percentages in real time.


Features

 LRU (Least Recently Used) Cache Replacement
 RAM LRU Replacement
 Random Data Access Simulation
 User-Specified Data Access
 Real-Time Cache Hit & Miss Tracking
 Hit Ratio and Miss Ratio Calculation
 Clean and Interactive GUI using Tkinter
 Step-by-step execution log with color coding


Memory Architecture Simulated

This simulator models:

1. Cache Memory (Fastest, Smallest)
2. RAM (Main Memory)
3. Secondary Storage (Largest, Slowest)

### Configuration:
- Cache Size = 3
- RAM Size = 5
- Secondary Storage = 10 Random Elements

---

##  How It Works

###  Data Request Flow

1. Check if data exists in Cache
   - If Yes → Cache Hit
   - If No → Cache Miss

2. If Miss:
   - Check RAM
   - If found → Move to Cache (LRU updated)
   - If not found → Fetch from Secondary Storage

3. If Cache or RAM is full:
   - Apply LRU replacement
   - Remove least recently used item

# Performance Metrics Calculated

- Total Requests
- Cache Hits
- Cache Misses
- Hit Ratio
- Miss Ratio
- Hit Percentage
- Miss Percentage

## 🖥️ GUI Overview

- Access Random Data Button
- Access User Data Input Field
- Reset Button
- Visual display of:
  - Cache contents
  - RAM contents
  - Secondary Storage
- Execution log with colored messages
- Real-time performance statistics

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI Framework)
- Random module


