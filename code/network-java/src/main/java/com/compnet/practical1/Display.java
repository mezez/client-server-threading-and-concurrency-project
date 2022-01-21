
package com.compnet.practical1;

import java.util.Arrays;
import java.util.function.IntFunction;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.Collectors;


public class Display {

    private final int[] values;

    public Display() {
        this(30);
    }

    public Display(int n) {
        this.values = new int[n];
    }
    
    public void add_value(int i) {
        add_value(i, 1);
    }
    
    public void add_value(int i, int v) {
        int nv = values[i%values.length] + v;
        sleep(1, 0); // simulate a computation that takes some time (to illustrate thing about threads later)
        values[i%values.length] = nv;
    }

    public void move_value_right(int i) {
        move_value_right(i, 1);
    }
    public void move_value_right(int i, int by) {
        move_value_right(i, by, 1);
    }
    public void move_value_right(int i, int by, int v) {
        add_value(i, -v);
        add_value(i+by, v);
    }
    
    public void render() {
        //* plain old mutable java
        String repr = "";
        int sum = 0;
        for (int v : values) {
            repr += String.format("%2d", v);
            sum += v;
        }
        /*/// java 8
        String repr = Arrays.stream(values).mapToObj(v -> String.format("%2d", v)).collect(Collectors.joining());
        int sum = Arrays.stream(values).sum();
        //*/
        System.out.println(repr + " -> " + sum);
    }

    public void render_clean() {
        //* plain old mutable java
        String repr = "";
        int sum = 0;
        for (int v : values) {
            //repr += v==0 ? "  " : v==1 ? " ." : String.format("%2d", v);
            repr += v>=0 && v<9 ? " " + " ▁▂▃▄▅▆▇█".charAt(v) : String.format("%2d", v);
            sum += v;
        }
        /*/// java 8
        IntFunction<String> toStr = v -> v==0 ? "  " : v==1 ? " ." : String.format("%2d", v);
        String repr = Arrays.stream(values).mapToObj(toStr).collect(Collectors.joining());
        int sum = Arrays.stream(values).sum();
        //*/
        System.out.println(repr + " -> " + sum);
    }

    private static void sleep(long ms, int nanos) {
        try {
            Thread.sleep(ms, nanos);
        } catch (InterruptedException ex) {
            Logger.getLogger(Display.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}


