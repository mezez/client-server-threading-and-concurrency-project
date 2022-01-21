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
public class A5ProducerKO {
    
    public static void main(String[] args) throws InterruptedException {
        
        Display d = new Display();

        sleep(500, 0);
        int n = 10;
        for (int i = 0; i < n; i++) {
            sleep(0, (int) (Math.random()*999999));
            producer(d).start();
        }
    }

    private static Thread producer(Display d) {
        return new Thread(() -> {
            for (int i = 0; i < 100; i++) {
                int ind = (int) (Math.random()*20);
                d.add_value(ind, 1);
                sleep((int) (Math.random()*2), 0);
                d.add_value(ind, -1);
            }
            d.render_clean();
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
