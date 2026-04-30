import socket

# Setări pentru server
HOST = '0.0.0.0'  # '127.0.0.1' pentru teste locale. Folosește '0.0.0.0' dacă clientul este pe alt PC.
PORT = 5000         # Portul de ascultare (asigură-te că partenerul tău folosește același port)

def start_tcp_server():
    # 1. Crearea socket-ului de tip TCP (SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Permite reutilizarea portului pentru a evita erorile la reporniri rapide
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[*] Serverul TCP a pornit și așteaptă conexiuni pe {HOST}:{PORT}...")

        # 2. Acceptă conexiunea de la client
        conn, addr = server_socket.accept()
        with conn:
            print(f"[+] Conectat cu succes la clientul: {addr}")

            # 3. Bucla de tip "Ping-Pong"
            while True:
                # Așteaptă mesajul de la client (Serverul citește primul)
                data = conn.recv(1024)
                
                # Dacă nu mai primim date, conexiunea s-a pierdut
                if not data:
                    print("[-] Clientul s-a deconectat brusc.")
                    break

                # Decodificare folosind UTF-8, conform cerințelor
                mesaj_primit = data.decode('utf-8').strip()

                # Oprire grațioasă dacă clientul trimite "exit"
                if mesaj_primit.lower() == 'exit':
                    print("[-] Clientul a trimis 'exit'. Închidere conexiune...")
                    break

                # Afișează mesajul primit
                print(f"Client: {mesaj_primit}")

                # Permite tastarea și trimiterea unui răspuns
                mesaj_de_trimis = input("Server (tu): ")
                
                # Codificare în UTF-8 și trimitere către client
                conn.sendall((mesaj_de_trimis + "\n").encode('utf-8'))
                
                print("[✓] Mesajul a fost trimis. Aștept răspuns...\n")
                
                # Oprire grațioasă dacă serverul scrie "exit"
                if mesaj_de_trimis.lower() == 'exit':
                    print("[-] Ai trimis 'exit'. Închidere server...")
                    break

if __name__ == "__main__":
    start_tcp_server()
