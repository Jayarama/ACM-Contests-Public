import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Created by srohr_000 on 001,  Oct,  1.
 */
public class HolyHandNumbers {
    public static void main(String [] args){
        try {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            HolyHandNumbers HHN = new HolyHandNumbers();
            String h;

            //do {
            //System.out.print("Enter thy number: ");

            h = br.readLine();
            HHN.Counteth(h);
            //}
            //while(h != "0");

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    void Counteth(String n){

        //long t1 = System.nanoTime();
        long stoppeth = Long.valueOf(n);

        //Last digit must be a 3.
        if (stoppeth%10 >= 3)
            stoppeth /= 10;
        else {
            stoppeth /= 10; //e.g. 12342- we can't reply counting 12343 as a HHN.
            stoppeth--;
        }

        String s;
        long count = 0;
        for (Long i = Long.valueOf(0); i < stoppeth; i++){
            s = i.toString();
            //s += "3"; //May be assumed.

            if (!s.contains("5")) {
                if (isHHN(s))
                    count++;
            }
            else if (i%10 != 5)
                i = Long.valueOf(s.replace("5", "6"));
        }
        //System.out.print(output);

        //long t2 = System.nanoTime();
        //System.out.printf("Number of Holy Hand Numbers that do precede thy number: %d (%g s)\n\n", count, (t2 - t1)*Math.pow(10.0, -9));
        System.out.println(count);

        return;
    }

    Boolean isHHN(String n){
        if (n.contains("34"))
            return false;
        else if (n.contains("20") || n.contains("21") ||
            n.contains("22") || n.contains("24") ||
            n.contains("26") || n.contains("27") ||
            n.contains("28") || n.contains("29"))
            return false;

        else {
            //System.out.printf("%s, ", n);
            return true;
        }
    }
}
