
package com.compnet.practical1;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 */
public class A2Thread {
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Display d = new Display();

        sleep(500, 0);
        int n = 20;
        for (int i = 0; i < n; i++) {
            // start a producer every 300ms
            sleep(300, 0);
            producer(d, i).start();
            // replace "start" by "run" above to not start a thread (and thus test as if you were not using threads...)
        }
    }

    private static Thread producer(final Display d, final int ind) {
        //* Java 8
        Runnable addElements = () -> {
            for (int i = 0; i < 9; i++) {
                d.add_value(ind, 1);
                sleep((int) (Math.random()*500), 0);
                d.render_clean();
            }
        };
        /*/// plain old java
        Runnable addElements = new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 9; i++) {
                    d.add_value(ind, 1);
                    sleep((int) (Math.random()*500), 0);
                    d.render_clean();
                }
            }
        };
        //*/
        
        Thread t = new Thread(addElements);
        return t;
    }
    
    private static void sleep(long ms, int nanos) {
        try {
            Thread.sleep(ms, nanos);
        } catch (InterruptedException ex) {
            Logger.getLogger(Display.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

}
