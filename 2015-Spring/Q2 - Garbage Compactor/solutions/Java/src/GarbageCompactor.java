import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

/**
 * Created by andrewsosa on 3/2/15.
 */
public class GarbageCompactor {

    public static void main(String args[]) {
        ArrayList<Pair> list = new ArrayList<Pair>();
        Scanner s = new Scanner(System.in);

        while (s.hasNext()) {
            String str = s.nextLine();
            str.replaceAll("\\W", "");

            for(int i = 0; i < str.length(); i = i + 2) {
                list.add(new Pair(str.charAt(i), str.charAt(i + 1)));
            }
        }
    }

    public class customCompare implements Comparator<Pair>{

        @Override
        public int compare(Pair o1, Pair o2) {
            return o1.y = o2.x;
        }
    }

    public static class Pair{
        public char x;
        public char y;

        public Pair(char x, char y) {
            this.x = x;
            this.y = y;
        }
    }
}
