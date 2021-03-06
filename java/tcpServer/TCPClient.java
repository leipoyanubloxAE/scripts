import java.io.*;
import java.net.*;

class TCPClient {
 public static void main(String argv[]) throws Exception {
  String sentence;
  String modifiedSentence;
  if(argv.length!=0) {
    System.out.println("Connecting to server " + argv[0]);
  } else {
    System.out.println("Server IP is null.");
    return; 
  }
  BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
  Socket clientSocket = new Socket(argv[0], 6789);
  DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
  BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
  System.out.println("input data");
  sentence = inFromUser.readLine();
  outToServer.writeBytes(sentence + '\n');
  System.out.println("sent to server");
  modifiedSentence = inFromServer.readLine();
  System.out.println("FROM SERVER: " + modifiedSentence);
  System.out.println("Press enter to exit.");
  sentence = inFromUser.readLine();
  clientSocket.close();
 }
}
