package service;

import repository.Repository;
import domain.Bursa;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;


public class Service {
    Repository repository;

    public Service(Repository repository) {
        this.repository = repository;
    }

    public void add(Long id, String nume, String prenume, String tip, double suma){
        Bursa c = new Bursa(id, nume, prenume, tip, suma);
        repository.adauga(c);
    }

    public void showAll(){
        for(int i = 0; i < repository.findAll().size(); i++)
            System.out.println(repository.findAll().get(i).toString());
    }
    public Bursa find(Long id){
        return repository.getAngajat(id);
    }

    public List<Bursa> getAll(){
        return repository.findAll();
    }

    public Bursa cautare(){
        String a = "Andronescu";
        List<Bursa> produse = getAll();
        return produse.stream()
                .filter(s -> s.getNume().equals(a))
                .filter(s -> s.getPrenume().equals("Ilinca"))
                .findFirst()
                .orElse(null);
    }

    public List<Bursa> filtarare1(){
        List<Bursa> burse = getAll();
        return burse.stream()
                .filter(s -> s.getTip().equals("social"))
                .collect(Collectors.toList());
    }

    public List<Bursa> filtarare2(){
        List<Bursa> burse = getAll();
        List<Bursa> filtered_list = burse.stream()
                .filter(s -> s.getTip().equals("social"))
                .collect(Collectors.toList());

        return filtered_list.stream()
                .filter(s -> s.getSuma() > 400)
                .collect(Collectors.toList());
    }

    public List<Bursa> sort1(){
        List<Bursa> burse = getAll();
        List<Bursa> sorted_list = burse.stream()
                .sorted(Comparator.comparing(Bursa::getNume).thenComparing(Bursa::getPrenume))
                .collect(Collectors.toList());
//        sorted_list.stream()
//                .map(s -> s.getId() + " " + s.getNume() + " " + s.getPrenume()).forEach(System.out::println);
        return sorted_list;
    }

    public List<Bursa> sort2(){
        List<Bursa> burse = getAll();
        List<Bursa> sorted_list = burse.stream()
                .sorted(Comparator.comparing(Bursa::getTip).reversed())
                .collect(Collectors.toList());
//        sorted_list.stream()
//                .map(s -> s.getNume() + " " + s.getCategorie() + " " + s.getDescriere()).forEach(System.out::println);
        return  sorted_list;
    }

    public List<Bursa> sort3(){
        List<Bursa> burse = getAll();
        List<Bursa> sorted_list = burse.stream()
                .sorted(Comparator.comparing(Bursa::getSuma))
                .collect(Collectors.toList());
//        sorted_list.stream()
//                .map(s -> s.getId() + " " + s.getPret()).forEach(System.out::println);
        return sorted_list;
    }
}
