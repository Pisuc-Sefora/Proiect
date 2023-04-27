package repository;

import domain.Bursa;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Repository {
    public Repository() {
    }

    List<Bursa> burse = new ArrayList<>();
    public void adauga(Bursa c){
        burse.add(c);
    }

    public List<Bursa> findAll() {
        return burse;
    }

    public Bursa getAngajat(Long id) {
        for (Bursa c : burse) {
            if (Objects.equals(c.getId(), id))
                return c;
        }
        return null;
    }
}
