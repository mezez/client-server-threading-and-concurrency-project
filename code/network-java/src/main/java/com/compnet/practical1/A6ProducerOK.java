/*
 * 
 */

package com.compnet.practical1;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author 
 */
public class A6ProducerOK {

    public static void main(String[] args) throws InterruptedException {
        
        BlockingQueue<String> q = new LinkedBlockingQueue<>();
        
        Display d = new Display();
        
        Thread c = consumer(q, d);
        c.setDaemon(true); // NB: the program terminates when all non-daemon thread are terminated
        c.start();

        sleep(500, 0);
        int n = 10;
        for (int i = 0; i < n; i++) {
            sleep(0, (int) (Math.random()*999999));
            producer(q, d).start();
        }

        sleep(5000, 0); // do not finish right away (so we can see if the daemon consumer prints)
    }

    private static Thread consumer(final BlockingQueue<String> q, final Display d) {
        return new Thread(() -> {
            try {
                while (true) {
                    String e = q.take();
                    if ("RENDER".equals(e)) {
                        d.render_clean();
                    } else {
                        String[] parts = e.split("/");
                        d.add_value(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
                    }
                }
            } catch (InterruptedException ex) {
                Logger.getLogger(A5ProducerKO.class.getName()).log(Level.SEVERE, null, ex);
            }            
        });
    }
    private static Thread producer(final BlockingQueue<String> q, final Display d) {
        return new Thread(() -> {
            try {
                for (int i = 0; i < 100; i++) {
                    int ind = (int) (Math.random()*20);
                    q.put(ind + "/" + 1);
                    sleep((int) (Math.random()*2), 0);
                    q.put(ind + "/" + -1);
                }
                q.put("RENDER");
            } catch (InterruptedException ex) {
                Logger.getLogger(Display.class.getName()).log(Level.SEVERE, null, ex);
            }
        });
    }

    private static void sleep(long ms, int nanos) {
        try {
            Thread.sleep(ms, nanos);
        } catch (InterruptedException ex) {
            Logger.getLogger(Display.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
