/*
 *
 */

package com.compnet.practical1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Formatter;

/**
 *
 * @author
 */
public class Z1TCPServer {

    public static void main(String[] args) throws IOException {

        ServerSocket serverSocket = new ServerSocket(9999);

        // process clients one by one (not in parallel)
        while (true) {

            System.out.println("ACCEPTING CONNECTIONS");
            Socket socket = serverSocket.accept();
            System.out.println("GOT A CONNECTION");
            System.out.println("from ip: "+socket.getInetAddress());
            System.out.println("from port: "+socket.getPort());

            // Read two lines then ignore anything from this client
            InputStream inputStream = socket.getInputStream();
            String l = NetUtils.readLine(inputStream);
            System.out.println("RECEIVED FIRST: "+l);
            l = NetUtils.readLine(inputStream);
            System.out.println("RECEIVED SECOND: "+l);
            // ... ignore the rest

        }

    }

}
