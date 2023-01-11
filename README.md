# Flush-DNS-script

The code defines a function called `flush_dns()` which is used to flush the DNS cache on a computer. It does this by using the `subprocess` module to run a command specific to the operating system of the computer it is running on.

The first step of the function is to determine the operating system of the computer using the `platform.system()` method. If the operating system is "Windows", the command `["ipconfig", "/flushdns"]` is used. If the operating system is "Darwin" (i.e. macOS), the command `["dscacheutil", "-flushcache"]` is used. And, if the operating system is not Windows or macOS, it assumes it's Linux and the command `["systemd-resolve", "--flush-caches"]` is used.

Once the appropriate command is determined, the `subprocess.run()` method is used to run the command. The `check=True` argument is used to raise an exception (`subprocess.CalledProcessError`) if the command exits with a non-zero return code.

In the try-except block, if the command runs without error, it print 'DNS cache flushed successfully' otherwise it will print 'Failed to flush DNS cache'

At last, the function is called, which will flush the DNS cache on the computer it is run on.
