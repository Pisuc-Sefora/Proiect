package ui;

import domain.Bursa;
import domain.BursaValidator;
import domain.Validator;
import service.Service;

import java.util.List;
import java.util.Scanner;

public class Ui {
    private Service service;
    static Validator<Bursa> tablouValidator = new BursaValidator();

    public Ui(Service service){
        this.service = service;
    }


    public void run(){
        showMenu();
    }

    void showMenu(){

        Boolean ok = true;

        while(ok) {


            System.out.println("1.Adauga angajat");
            System.out.println("2.Afisare:");
            System.out.println("3.Cauta bursa cu numele Andronescu si prenumele Ilinca.");
            System.out.println("4.Filtrare bursa sociala.");
            System.out.println("5.Filtrare bursa sociala si care au salariu > 400.");
            System.out.println("6.Sortare dupa nume si prenume,alfabetic,crescator.");
            System.out.println("7.Sortare dupa tip,descrescator.");
            System.out.println("8.Sortare dupa suma,crescator.");
            System.out.println("0.Iesire.");

            Scanner sc= new Scanner(System.in);
            int input = sc.nextInt();

            if (input == 1) uiAdd();
            else if (input == 2) uiShowAll();
            else if (input == 3) uiCautare();
            else if (input == 4) uifiltarare1();
            else if (input == 5) uifiltarare2();
            else if (input == 6) uisort1();
            else if (input == 7) uisort2();
            else if (input == 8) uisort3();
            else if (input == 0) ok = false;
            else System.out.println("Varianta invalida!");
        }
    }

    private void uiCautare() {
        System.out.println(service.cautare());
        System.out.println();
    }

    private void uifiltarare1() {
        System.out.println(service.filtarare1());
        System.out.println();
    }

    private void uifiltarare2() {
        System.out.println(service.filtarare2());
        System.out.println();
    }

    private void uisort1() {
        List<Bursa> sorted_list = service.sort1();
        sorted_list.stream()
                .map(s -> s.getId() + " " + s.getNume() + " " + s.getPrenume()).forEach(System.out::println);
        System.out.println();
    }

    private void uisort2() {
        List<Bursa> sorted_list = service.sort2();
        sorted_list.stream()
                .map(s -> s.getNume() + " " + s.getPrenume() + " " + s.getTip()).forEach(System.out::println);
        System.out.println();
    }

    private void uisort3() {
        List<Bursa> sorted_list = service.sort3();
        sorted_list.stream()
                .map(s -> s.getId() + " " + s.getSuma()).forEach(System.out::println);
        System.out.println();
    }

    public void uiAdd(){
        Scanner sc= new Scanner(System.in);
        System.out.println("Dati id-ul: ");
        Long id = sc.nextLong();
        System.out.println("Dati numele: ");
        String nume = sc.nextLine();
        System.out.println("Dati prenumele: ");
        String prenume = sc.nextLine();
        System.out.println("Dati tipul: ");
        String tip = sc.nextLine();
        System.out.println("Dati suma: ");
        Double suma = sc.nextDouble();

        tablouValidator.validate(new Bursa(id,nume,prenume, tip,suma));

        service.add(id,nume,prenume,tip,suma);
    }

    public void uiShowAll(){
        service.showAll();
    }
}
