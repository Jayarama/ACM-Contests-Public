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
        Integer stoppeth = Integer.valueOf(n);

        String s;
        long count = 0;

        //System.out.printf("# holy hand number")
        for (Integer i = 3; i <= stoppeth; i += 10){
            s = i.toString();
            //s += "3"; //May be assumed.

            if (!s.contains("5")) {
                if (isHHN(s)){
                    //System.out.println(Long.valueOf(s + "3"));
                    count++;
                  }
            }
            //else if (i%10 != 5)
                //i = Long.valueOf(s.replace("5", "6"));
        }
        //System.out.print(output);

        //long t2 = System.nanoTime();
        System.out.printf("%d\n", count);
        //System.out.println(count);

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
