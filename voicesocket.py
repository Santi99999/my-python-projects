from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import socket
ip = socket.gethostbyname(socket.gethostname())
print("Bienvenido a VoiceSocket!")
print("Tu codigo publico es: " + ip)
print()
code = input("Porfavor escribe el codigo para conectarte:")
print("Conectando a: " + code)
r = AudioReceiver(ip, 9999)
rthread = threading.Thread(target=r.start_server)
s = AudioSender(code, 5555)
sthread = threading.Thread(target=s.start_stream)
rthread.start()
sthread.start()
