import java.util.Collections;
import java.util.Scanner;
import java.util.Vector;

public class Witchimiliarity {
    Vector<Person> notWitches;
    Vector<Person> population;
    int N;

    public static void main(String [] args){
        long t1 = System.currentTimeMillis();
        Witchimiliarity W = new Witchimiliarity();

        W.population = new Vector<Person>();
        W.notWitches = new Vector<Person>();
        W.ReadIn();
        long t2 = System.currentTimeMillis();

        //System.out.printf("Execution completed in: %g s\n", ((double)t2 - (double)t1)/1000.0);
    }

    void ReadIn(){
        Scanner s = new Scanner(System.in);
        String trash;

        try {
            N = s.nextInt();

            for (int i = 0; i < N; i++){
                Person p = new Person();
                p.name = s.next();
                p.height = s.nextInt();
                p.noseLen = s.nextInt();
                p.weight = s.nextInt();
                trash = s.next();

                population.add(p);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        int p1 = -1, p2 = -1;
        int desiredSize = (int) (0.9 * population.size());

        double maxW = -999999999;
        for (int i = 0; i < population.size(); i++)
            for (int j = i; j < population.size(); j++)
                if (i != j){
                    double w = Fn(population.elementAt(i), population.elementAt(j));
                    if (w > maxW){
                        maxW = w;
                        p1 = i;
                        p2 = j;
                    }
                }

        notWitches.add(population.elementAt(p1));
        notWitches.add(population.elementAt(p2));
        population.remove(notWitches.elementAt(0));
        population.remove(notWitches.elementAt(1));

        while (notWitches.size() != desiredSize){
            doItr();
        }



        Vector<String> Witches = new Vector<String>();
        for(Person p : population)
            Witches.add(p.name);

        /*for (int i = 0; i < population.size(); i++) {
            if (!notWitches.contains(population.elementAt(i))){
                Witches.add(population.elementAt(i).name);
            }
        }*/

        Collections.sort(Witches, String.CASE_INSENSITIVE_ORDER);

        //System.out.print("\nWitches:\n");
        //int itr = 1;
        for (String name : Witches) {
            //System.out.println(itr + ". " + name);
            System.out.println(name);
            //itr++;
        }
    }

    double Fn(Person p1, Person p2){
        return ((p1.height + p2.height) * Math.abs(p1.noseLen - p2.noseLen))
                / (p1.weight * p2.weight);
    }

    void doItr(){
        double wMax = -999999999;
        double w;
        int best = -1;

        for (int i = 0; i < notWitches.size(); i++)
            for (int j = 0; j < population.size(); j++){
                if (!notWitches.contains(population.elementAt(j)))
                {
                    w = Fn(notWitches.elementAt(i), population.elementAt(j));
                    //System.out.printf("%s - %s : %g", notWitches.elementAt(i).name, population.elementAt(j).name, w);
                    if (w > wMax){
                        //System.out.print("\tNew best!");
                        wMax = w;
                        best = j;
                    }
                    //System.out.println();
                }
            }

        //System.out.printf("Found a not-witch: %s (%g)\n", population.elementAt(best).name, wMax);
        Person p = population.elementAt(best);
        notWitches.add(p);
        population.remove(p);

    }

    class Person{
        String name;
        double height, weight;
        int noseLen;
    }
}
