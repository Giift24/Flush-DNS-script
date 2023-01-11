import subprocess
import platform

def flush_dns():
    # Flushes DNS based on OS
    if platform.system() == "Windows":
        command = ["ipconfig", "/flushdns"]#Windows
    elif platform.system() == "Darwin":  # macOS
        command = ["dscacheutil", "-flushcache"]
    else:  # Linux
        command = ["systemd-resolve", "--flush-caches"]

    # Run command
    try:
        subprocess.run(command, check=True)
        print("DNS cache flushed successfully")
    except subprocess.CalledProcessError:
        print("Failed to flush DNS cache")

# Flush the DNS cache
flush_dns()
