import socket
import screen


screen.say("HOST[h] or CONNECT[c] or MORE[enter]")
I = screen.ask(">>>")
I = I.lower()

if I == "c":
	screen.say("Please enter your BUDDY connection!")
	ip = screen.ask("IPV4>>>")
	port = screen.ask("PORT>>>")

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((str(ip), int(port)))
		s.sendall(b"[BUDDY CONNECTED]")
		data = s.recv(1024)
		print(data)
		while True:
			data = s.recv(1024)
			screen.say(str(data))
			I=screen.ask("SEND>>>")
			s.sendall(bytes(I, encoding='utf8'))

elif I == "h":
	screen.say("Your BUDDY conection:")
	screen.say("IPV4="+socket.gethostbyname(socket.gethostname()))
	port = screen.ask("PORT>>>")
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((socket.gethostbyname(socket.gethostname()), int(port)))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('Connected by',  addr)
			data = conn.recv(1024)
			print(data)
			conn.sendall(b"[BUDDY CONNECTED]")

			while True:
				I = screen.ask("SEND>>>")
				conn.sendall(bytes(I, encoding='utf8'))
				data = conn.recv(1024)
				screen.say(str(data))

else:
	screen.say("ERROR[not implemented the more area]")
	screen.quit()
