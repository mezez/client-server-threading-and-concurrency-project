/*
 *
 */

package com.compnet.practical1;

import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

/**
*
* @author
*/
public class A3Server {

    /* 

    public static void main(String[] args) throws IOException {
        Display display = new Display();
        // start a new thread to accept new connections
        handleAcceptAll(display).start()
    }

    private static Thread handleAcceptAll(final Display display) {
        return new Thread(() -> {
            // create a socket that listens (on a port of your choice)
            ??? serverSocket = ???;
            ???
            // accept new clients connections,
            // and start a handleClient thread every time
            ???
        });
    }

    // processClient returns a Thread that can be started, i.e., use: processClient(.......).start();
    private static Thread handleClient(final Socket socket, final Display display) {
        return new Thread(() -> {
            // initialise a random integer position, e.g. between 0 and 100
            int i = ???

            // initialize a random direction (for later)
            int by = Math.random() > 0.5 ? 1 : -1;

            // add 1 to the display, at index i (and render it)
            ???

            // get ready to receive from the socket
            InputStream in = socket.getInputStream();

            // loop over the received data, ignoring (or just printing) this data for now (e.g., use NetUtils to read lines)
            // be sure to end the loop when the connection is closed (readLine returns null or throws an exception)
            ???

             // Later, we will use move_value_right(i, by) and increase the i variable by
            // ???

            // when the connection is closed, subtract at index (and rerender)
            ???

        });
    }

    //*/
}
