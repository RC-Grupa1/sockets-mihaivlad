import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TcpClient {
    public static void main(String[] args) {
        String serverAddress = "100.99.29.41";
        int port = 5000;

        try (Socket socket = new Socket(serverAddress, port)) {
            System.out.println("Conectat la serverul TCP!");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
            PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "UTF-8"), true);
            Scanner scanner = new Scanner(System.in);

            String userInput;
            String serverResponse;

            System.out.print("Tu (Client): ");
            userInput = scanner.nextLine();
            out.println(userInput);

            while (!userInput.equalsIgnoreCase("exit")) {
                serverResponse = in.readLine();
                if (serverResponse == null || serverResponse.equalsIgnoreCase("exit")) {
                    System.out.println("Serverul a închis conexiunea.");
                    break;
                }
                System.out.println("Colegul (Server): " + serverResponse);

                System.out.print("Tu (Client): ");
                userInput = scanner.nextLine();
                out.println(userInput);
            }

            System.out.println("Chat închis.");
        } catch (IOException e) {
            System.err.println("Eroare la conectarea TCP: " + e.getMessage());
        }
    }
}