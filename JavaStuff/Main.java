import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        float sum=0;
        
        for (int i = 0; i <5; i++) {
            System.out.println(i);
            Scanner ui = new Scanner(System.in);
            System.out.println("How bad r u in schul? ");
            int name = ui.nextInt();
            sum = sum + name;
            System.out.println(sum);
        }
        float answer = sum/5;
        System.out.println(answer);
    }
}