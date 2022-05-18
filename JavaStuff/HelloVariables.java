import java.util.Scanner;

public class HelloVariables {
    public static void main(String[] args){
        /*System.out.println(15/5);
        System.out.println(16/5);
        System.out.println(19/5.0);

        double number1 =0.0;
        number1+=5;
        number1-=3;
        System.out.println(number1);
        number1*=5;
        number1/=3;
        System.out.println(number1);
        number1++; //add 1
        number1--; //subtract 1
        //Math.pow(number1,2); 
        System.out.println(number1);
        */

        Scanner in = new Scanner(System.in);
        double gpa = 0.0;
        
        for(int i=0; i<5;i++){
            System.out.println("What is your grade");
            double ui = in.nextDouble();
            if(ui<=5 && ui>=0){
                gpa+=ui;
            } 
            //gpa+=in.nextDouble();
        }
        
        System.out.println(gpa/5);
    }
}
