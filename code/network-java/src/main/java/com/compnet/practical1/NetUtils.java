/*
 * 
 */

package com.compnet.practical1;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 *
 * @author 
 */
public class NetUtils {

    public static final String LINE_SEPARATOR = "\r\n";
    
    public static String readLine(InputStream inputStream) throws IOException {

        ByteArrayOutputStream res = new ByteArrayOutputStream();
        
        boolean justSeenR = false;
        while (true) {
            int valueRead = inputStream.read();
            
            if (valueRead == -1) {
                return null;
            }
            
            byte b = (byte) valueRead;
            
            if (b == '\n' && justSeenR) {
                break;
            }
            if (justSeenR) {
                res.write('\r');
            }
            if (b == '\r') {
                justSeenR = true;
            } else {
                justSeenR = false;
                res.write(b);
            }
        }
        return res.toString("utf-8");
    }
    
}
