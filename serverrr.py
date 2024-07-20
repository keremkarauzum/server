import socket


host = '192.168.56.1'  
port = 5000

def start_server():
    
    sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sunucu.bind((host, port))
    
    
    sunucu.listen(1)  
    print("Baglanti araniyor")
    
    while True:
        
        client_socket, client_address = sunucu.accept()
        print(f"Bağlantı kabul edildi: {client_address}")
        
        # İstemciden veri alma
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Gelen veri: {data}")
        
        
        response = "Baglanti saglandi"
        client_socket.send(response.encode('utf-8'))
        
        

# Sunucuyu başlat
if __name__ == "__main__":
    start_server()
