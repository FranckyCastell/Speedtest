import colorama
from speedtest import Speedtest

# Initialize colorama
colorama.init(autoreset=True)

# Create a Speedtest object
s = Speedtest()

# Get the best server for the speedtest
best_server = s.get_best_server()

# Print a message indicating that the speedtest is starting
print("")
print(colorama.Fore.CYAN + "Starting speedtest..." + colorama.Fore.RESET)

# Run the speedtest
#download_speed = s.download()
#upload_speed = s.upload()
ping = s.results.ping

# Print the ping result
print("")
print(colorama.Fore.GREEN + "Ping: {} ms".format(ping))

# Print a message indicating that the download is starting
print("")
print(colorama.Fore.CYAN + "Downloading..." + colorama.Fore.RESET)
download_speed = s.download()

# Print the download speed result
print(colorama.Fore.GREEN + "Download speed: {} Mbps".format(download_speed/1000000))

# Print a message indicating that the upload is starting
print("")
print(colorama.Fore.CYAN + "Uploading..." + colorama.Fore.RESET)
upload_speed = s.upload()

# Print the upload speed result
print(colorama.Fore.GREEN + "Upload speed: {} Mbps".format(upload_speed/1000000))
