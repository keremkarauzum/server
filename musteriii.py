import socket
host = '192.168.56.1'  
port = 5000
    
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Sunucuya bağlandı: {host}:{port}")
    mesaj = "Baglanti saglandi"
    client_socket.send(mesaj.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Sunucudan gelen cevap: {response}")
    

if __name__ == "__main__":
    start_client()
