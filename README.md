# Explicația Aplicației Client-Server (TCP vs UDP)

## 1. Modul de funcționare TCP (Transmission Control Protocol)
**Cum se realizează conexiunea:**
TCP este un protocol orientat pe conexiune. Înainte ca orice mesaj să fie trimis, clientul și serverul stabilesc o conexiune stabilă prin procesul de **Three-Way Handshake** (SYN -> SYN-ACK -> ACK), vizibil și în Wireshark. În cod, serverul folosește funcțiile `bind()`, `listen()` pentru a aștepta, și `accept()` pentru a aproba conexiunea clientului.

**Cum sunt trimise mesajele:**
Odată conexiunea stabilită, datele sunt trimise ca un flux continuu (stream). Am folosit funcțiile `sendall()` și `recv()`. TCP garantează că mesajele ajung la destinație intacte și în ordinea corectă. Când comunicarea se termină, conexiunea este închisă grațios.

## 2. Modul de funcționare UDP (User Datagram Protocol)
**Cum sunt trimise mesajele:**
UDP este un protocol fără conexiune (connectionless). Nu există niciun handshake inițial. Serverul doar deschide un port (cu `bind()`) și așteaptă mesaje folosind `recvfrom()`. Clientul împachetează mesajul într-o datagramă și o "aruncă" spre adresa IP și portul serverului folosind `sendto()`. Serverul folosește adresa extrasă din pachetul primit pentru a ști unde să trimită răspunsul.

## 3. Diferențe principale observate
* **Conexiune:** TCP necesită stabilirea prealabilă a unei conexiuni (Handshake), în timp ce UDP trimite pachetele direct.
* **Fiabilitate:** TCP este fiabil (dacă un pachet se pierde, este retransmis). UDP funcționează pe principiul "fire-and-forget" (nu garantează livrarea).
* **Performanță/Overhead:** Capturile Wireshark demonstrează că TCP generează mai mult trafic de control (pachete SYN, ACK, FIN) și este mai lent, în timp ce UDP este extrem de rapid, trimițând strict pachetele de date.

---

## Capturi de ecran Wireshark


### Analiza UDP (Fără Handshake)
*(Se observă că datele sunt transmise direct, fără pachete de control prealabile)*


<img width="1919" height="1005" alt="udp" src="https://github.com/user-attachments/assets/2dc7712b-d978-4051-beca-ac696ff92f26" />

### Analiza TCP (Handshake și Date)

*(Se observă procesul de stabilire a conexiunii și confirmarea primirii datelor)*

<img width="1919" height="1004" alt="tcp" src="https://github.com/user-attachments/assets/2e5936a3-d43e-4136-b4f9-52e22a6addec" />
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UwOds2hL)
