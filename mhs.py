import tkinter as tk
import random

CACHE_SIZE = 3
RAM_SIZE = 5

secondary = [random.randint(10, 99) for _ in range(10)]
cache = []
ram = []

total_requests = 0
cache_hits = 0
cache_misses = 0


def process_data(data):
    global total_requests, cache_hits, cache_misses
    total_requests += 1

    log(f"\nRequesting Data: {data}")

    # CACHE CHECK
    if data in cache:
        cache_hits += 1
        log("✅ Cache Hit (Fast Access)", "green")

        # LRU Update → Move to end
        cache.remove(data)
        cache.append(data)

        update_display()
        return

    cache_misses += 1
    log("❌ Cache Miss", "red")

    # RAM CHECK
    if data in ram:
        log("➡ Found in RAM", "orange")

        # LRU Update in RAM
        ram.remove(data)
        ram.append(data)

    else:
        log("➡ Not in RAM", "purple")
        log("⬇ Fetching from Secondary Storage", "blue")

        # RAM LRU Replacement
        if len(ram) >= RAM_SIZE:
            removed_ram = ram.pop(0)
            log(f"RAM Full → Removed {removed_ram} (LRU)", "brown")

        ram.append(data)
        log(f"Loaded {data} into RAM", "blue")

    # CACHE LRU Replacement
    if len(cache) >= CACHE_SIZE:
        removed_cache = cache.pop(0)
        log(f"Cache Full → Removed {removed_cache} (LRU)", "brown")

    cache.append(data)
    log(f"Loaded {data} into Cache", "blue")

    update_display()


def access_random():
    data = random.choice(secondary)
    process_data(data)


def access_user():
    try:
        data = int(user_entry.get())
    except:
        log("Enter valid number!", "red")
        return

    if data not in secondary:
        log("Data not present in Secondary Storage!", "red")
        return

    process_data(data)


def update_display():
    hit_ratio = 0
    miss_ratio = 0
    hit_percent = 0
    miss_percent = 0

    if total_requests > 0:
        hit_ratio = cache_hits / total_requests
        miss_ratio = cache_misses / total_requests
        hit_percent = hit_ratio * 100
        miss_percent = miss_ratio * 100

    cache_label.config(text=f"Cache (LRU)\n{cache}")
    ram_label.config(text=f"RAM (LRU)\n{ram}")
    sec_label.config(text=f"Secondary Storage\n{secondary}")

    ratio_label.config(
        text=(
            f"Total Requests: {total_requests} | "
            f"Cache Hits: {cache_hits} | "
            f"Cache Misses: {cache_misses}\n"
            f"Hit Ratio: {hit_ratio:.2f} | "
            f"Miss Ratio: {miss_ratio:.2f} | "
            f"Hit %: {hit_percent:.1f}% | "
            f"Miss %: {miss_percent:.1f}%"
        )
    )


def log(message, color="black"):
    output.insert(tk.END, message + "\n", color)
    output.tag_config(color, foreground=color)
    output.see(tk.END)


def reset():
    global cache, ram, total_requests, cache_hits, cache_misses
    cache = []
    ram = []
    total_requests = 0
    cache_hits = 0
    cache_misses = 0
    output.delete("1.0", tk.END)
    update_display()


# GUI
root = tk.Tk()
root.title("Memory Hierarchy Simulator - LRU Version")
root.geometry("900x700")
root.config(bg="#f4f6f7")

title = tk.Label(
    root,
    text="Memory Hierarchy Simulator (LRU + Hit/Miss Statistics)",
    font=("Arial", 18, "bold"),
    bg="#f4f6f7"
)
title.pack(pady=10)

control_frame = tk.Frame(root, bg="#f4f6f7")
control_frame.pack(pady=10)

tk.Button(
    control_frame,
    text="Access Random Data",
    command=access_random,
    font=("Arial", 12),
    bg="#2ecc71",
    fg="white"
).pack(side="left", padx=10)

user_entry = tk.Entry(control_frame, width=10)
user_entry.pack(side="left", padx=5)

tk.Button(
    control_frame,
    text="Access User Data",
    command=access_user,
    font=("Arial", 12),
    bg="#3498db",
    fg="white"
).pack(side="left", padx=10)

tk.Button(
    control_frame,
    text="Reset",
    command=reset,
    font=("Arial", 12),
    bg="#e74c3c",
    fg="white"
).pack(side="left", padx=10)

cache_label = tk.Label(root, font=("Arial", 14), bg="#fcf3cf", width=60)
cache_label.pack(pady=10)

ram_label = tk.Label(root, font=("Arial", 14), bg="#fdebd0", width=60)
ram_label.pack(pady=10)

sec_label = tk.Label(root, font=("Arial", 14), bg="#ebdef0", width=60)
sec_label.pack(pady=10)

ratio_label = tk.Label(
    root,
    font=("Arial", 12, "bold"),
    bg="#d5f5e3",
    width=100
)
ratio_label.pack(pady=10)

output = tk.Text(root, height=12, width=110)
output.pack(pady=10)

update_display()
root.mainloop()
