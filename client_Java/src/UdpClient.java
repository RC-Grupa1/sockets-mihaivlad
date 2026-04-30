import java.net.*;
import java.util.Scanner;
import java.nio.charset.StandardCharsets;

public class UdpClient {
    public static void main(String[] args) {
        String serverAddress = "100.99.29.41";
        int serverPort = 5001;
        try (DatagramSocket socket = new DatagramSocket()) {
            InetAddress address = InetAddress.getByName(serverAddress);
            Scanner scanner = new Scanner(System.in);

            byte[] sendBuffer;
            byte[] receiveBuffer = new byte[1024];

            System.out.println("Pornit client UDP. Scrie un mesaj pentru a începe chat-ul.");

            while (true) {
                System.out.print("Tu (Client): ");
                String message = scanner.nextLine();
                sendBuffer = message.getBytes(StandardCharsets.UTF_8);

                DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, address, serverPort);
                socket.send(sendPacket);

                if (message.equalsIgnoreCase("exit")) {
                    System.out.println("Chat închis grațios.");
                    break;
                }

                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);

                String serverResponse = new String(receivePacket.getData(), 0, receivePacket.getLength(), StandardCharsets.UTF_8);
                System.out.println("Colegul (Server): " + serverResponse);

                if (serverResponse.equalsIgnoreCase("exit")) {
                    System.out.println("Serverul a închis chat-ul.");
                    break;
                }
            }
        } catch (Exception e) {
            System.err.println("Eroare la comunicarea UDP: " + e.getMessage());
        }
    }
}