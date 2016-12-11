/*
ID: davidlz2
LANG: JAVA
TASK: ride
*/
import java.io.*;
import java.util.*;

class ride {
  private static final int C = 47;
    static int aBase = Integer.valueOf('A') - 1;
  public static void main (String [] args) throws IOException {
    // Use BufferedReader rather than RandomAccessFile; it is much faster
    BufferedReader f = new BufferedReader(new FileReader("ride.in"));
                                                  // input file name goes above
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ride.out")));
    // Use StringTokenizer vs. readLine/split -- lots faster
    StringTokenizer st = new StringTokenizer(f.readLine());
    String name = st.nextToken();
    st = new StringTokenizer(f.readLine());
    String group = st.nextToken();
						  // Get line, break into tokens
    System.out.println(name +  " | " + group);
    int nameReminder = reminder(name);
    int groupReminder = reminder(group);
    if (nameReminder == groupReminder) {
        out.write("GO\n");
    }
    else {
        out.write("STAY\n");
    }
    out.close();                                  // close the output file
  }

  public static int reminder(String str) {

    int result = Integer.valueOf('A') - aBase;
    for (int i = 0; i<str.length(); i++) {
        char c = str.charAt(i);
        result = result * (Integer.valueOf(c) - aBase);
        System.out.println(" " + c + " " + result);
    }
    return result % C;
  }
}
