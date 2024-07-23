import socket
from dronekit import connect
import mesajlar
import time
siha=connect('127.0.0.1:14550',wait_ready=True)

host = '127.0.0.1'  
port = 5000

def start_server():
    
    sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sunucu.bind((host, port))
    
    
    sunucu.listen(1)  
    print("Baglanti araniyor")
    
    while True:
         
        client_socket, client_address = sunucu.accept()
        print(f"Bağlantı kabul edildi: {client_address}")
        
    
        veri = client_socket.recv(1024).decode('utf-8')
        print(f"Gelen veri: {veri}\n")
        
        while 1:
            response = "Baglanti saglandi\n"
            client_socket.send(response.encode('utf-8'))
            enlem ,boylam ,irtifa=mesajlar.listen_gps(siha)
            dikilme,yonelme,yatis=mesajlar.listen_aci(siha)
            hiz=mesajlar.listen_hiz(siha)
            batarya=mesajlar.listen_batarya(siha)
            mesaj1=f"enlem:{enlem}\n"
            mesaj2=f"boylam:{boylam}\n"
            mesaj3=f"irtifa:{irtifa}\n"
            mesaj4=f"dikilme:{dikilme}\n"
            mesaj5=f"yonelme:{yonelme}\n"
            mesaj6=f"yatis:{yatis}\n"
            mesaj7=f"hiz:{hiz}\n"
            mesaj8=f"batarya:{batarya}\n"
            client_socket.send(mesaj1.encode('utf-8'))
            client_socket.send(mesaj2.encode('utf-8'))
            client_socket.send(mesaj3.encode('utf-8'))
            client_socket.send(mesaj4.encode('utf-8'))
            client_socket.send(mesaj5.encode('utf-8'))
            client_socket.send(mesaj6.encode('utf-8'))
            client_socket.send(mesaj7.encode('utf-8'))
            client_socket.send(mesaj8.encode('utf-8'))
            time.sleep(1)

if __name__ == "__main__":
    start_server()



