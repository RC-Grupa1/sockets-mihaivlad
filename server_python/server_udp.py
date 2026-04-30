import socket

# Setări pentru server
HOST = '0.0.0.0'  # Ascultă pe toate interfețele, inclusiv Tailscale
PORT = 5001       # Portul diferit pentru UDP

def start_udp_server():
    # 1. Crearea socket-ului de tip UDP (SOCK_DGRAM în loc de SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        
        server_socket.bind((HOST, PORT))
        print(f"[*] Serverul UDP a pornit și așteaptă mesaje pe {HOST}:{PORT}...")

        # 2. Bucla de chat (Nu există .listen() sau .accept() în UDP)
        while True:
            # Serverul folosește recvfrom() care returnează datele ȘI adresa (IP + Port)
            data, addr = server_socket.recvfrom(1024)
            
            # Decodificare folosind UTF-8
            mesaj_primit = data.decode('utf-8').strip()

            # Oprire grațioasă dacă clientul trimite "exit"
            if mesaj_primit.lower() == 'exit':
                print(f"[-] Clientul {addr} a trimis 'exit'. Oprire server...")
                break

            # Afișează mesajul și de unde a venit
            print(f"Client {addr}: {mesaj_primit}")

            # Permite tastarea și trimiterea unui răspuns
            mesaj_de_trimis = (input("Server (tu): ") + "\n")
            
            # Codificare și trimitere înapoi folosind sendto() către adresa extrasă anterior
            server_socket.sendto(mesaj_de_trimis.encode('utf-8'), addr)

            print("[✓] Mesajul a fost trimis. Aștept răspuns...\n")
            # Oprire grațioasă dacă tu scrii "exit"
            if mesaj_de_trimis.lower() == 'exit':
                print("[-] Ai trimis 'exit'. Oprire server...")
                break

if __name__ == "__main__":
    start_udp_server()
