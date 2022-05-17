import java.util.Scanner;

public class HelloScanner {
    public static void main(String[] args) {
        //ui = input("message") python
        Scanner ui = new Scanner(System.in);
        System.out.println("What is your name? ");
        String name = ui.nextLine();
        System.out.println(name);
        Scanner u = new Scanner(System.in);
        System.out.println("How r u? ");
        String feel = u.nextLine();
        System.out.println(feel);
        Scanner a = new Scanner(System.in);
        System.out.println("What da weather like? ");
        String h = a.nextLine();
        System.out.println(h);        
        Scanner t = new Scanner(System.in);
        System.out.println("Y u here? ");
        String d = t.nextLine();
        System.out.println(d);        
        Scanner e = new Scanner(System.in);
        System.out.println("age? ");
        String som = e.nextLine();
        System.out.println(som);
    }
}
