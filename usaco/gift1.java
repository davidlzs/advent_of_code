/*
ID: davidlz2
LANG: JAVA
TASK: gift1
*/
import java.io.*;
import java.util.*;

class gift1 {
  public static void main (String [] args) throws IOException {
    // Use BufferedReader rather than RandomAccessFile; it is much faster
    BufferedReader f = new BufferedReader(new FileReader("gift1.in"));
                                                  // input file name goes above
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("gift1.out")));
    // Use StringTokenizer vs. readLine/split -- lots faster
    StringTokenizer st = new StringTokenizer(f.readLine());
    int np = Integer.parseInt(st.nextToken());
    Vector<String> names = new Vector<String>();
    for (int i = 0; i < np; i++) {
        names.add(f.readLine()); 
    }
    Map<String, Integer> nmap = new HashMap<String, Integer>();
    for (int i = 0; i < np; i++) {
        nmap.put(names.get(i), 0);
    }

    for (int i = 0; i < np; i++) {
        String giver = f.readLine();
        st = new StringTokenizer(f.readLine());
        int initialAmount = Integer.parseInt(st.nextToken());
        int nTos = Integer.parseInt(st.nextToken());
        nmap.put(giver, nmap.get(giver) - initialAmount);

        if (nTos != 0) {
            nmap.put(giver, nmap.get(giver) + initialAmount % nTos);
            for (int j = 0; j < nTos; j++) {
                String to = f.readLine();
                nmap.put(to, nmap.get(to) + initialAmount / nTos);
            }
        }

    }
    
    System.out.println(names);
    System.out.println(nmap);
    for (String n : names) {
        out.write(n + " " + nmap.get(n) + "\n");
    }
    out.close();
  }
}
