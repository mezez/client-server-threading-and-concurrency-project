
package com.compnet.practical1;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 */
public class A1TestDisplay {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Display d = new Display();

        d.add_value(10, 2);
        d.render();

        sleep(2000, 0);

        int i = 6;
        d.add_value(i, 4);
        d.render();

        sleep(1000, 0);

        for (int j = 0; j < 100; j++) {
            d.move_value_right(i, 1, 4);
            i++;
            d.render();
            sleep(10, 0);
        }
        
        System.out.println();
        d.add_value(5, 1);
        d.render_clean();
        d.render();
        d.render_clean();
        d.render();
    }
    
    private static void sleep(long ms, int nanos) {
        try {
            Thread.sleep(ms, nanos);
        } catch (InterruptedException ex) {
            Logger.getLogger(Display.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

}
