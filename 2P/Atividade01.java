import java.util.Random;
import java.util.Scanner;
import java.util.ArrayList;

public class Atividade01 {
    public static void main(String[] args) {
        Random gerador = new Random();


        Scanner input = new Scanner(System.in);
        int tamanho = input.nextInt();

    }

    public void gerarLista(int tamanho, Random gerador){

        ArrayList<Integer> lista = new ArrayList<>();

        for (int i = 0; i < 100; i++){
            System.out.println(gerador.nextInt());
            System.out.println("aqui tem o imput");
        }

        for (int i = 0; i <= tamanho; i++){
            lista.add(gerador.nextInt());
        }

        for (int i : lista){
            if( i % 3 == 0){
                System.out.println(i + "esse numero é multiplo de 3");
            }
            else if(i % 2 == 0){
                System.out.println(i + "esse numero é par");
            }
            else {
                System.out.println(i + "esse numero é impar");
            }
        }
    }
}