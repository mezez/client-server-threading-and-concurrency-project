package com.compnet.practical1;


import java.io.IOException;
import java.net.Socket;

/*
 * 
 */
public class Z2TCPClient {

    public static void main(String[] args) throws IOException {
        
        Socket s = new Socket("localhost", 9999);
        s.getOutputStream().write("HELLOJ\r\n".getBytes("utf-8"));
        //s.getOutputStream().flush();
        
        s.getOutputStream().write("HO HO HO\r\n".getBytes("utf-8"));

        s.getOutputStream().write("whatev\r\n".getBytes("utf-8"));
    }
}
