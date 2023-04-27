package domain;

import java.util.Objects;

public class Bursa {
    private Long id;
    private String nume;
    private String prenume;
    private String tip;
    private double suma;


    public Bursa(Long id, String nume, String prenume, String tip, double suma) {
        this.id = id;
        this.nume = nume;
        this.prenume = prenume;
        this.suma = suma;
        this.tip = tip;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public String getPrenume() {
        return prenume;
    }

    public void setPrenume(String prenume) {
        this.prenume = prenume;
    }

    public double getSuma() {
        return suma;
    }

    public void setSuma(double suma) {
        this.suma = suma;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Bursa bursa = (Bursa) o;
        return Double.compare(bursa.suma, suma) == 0 && Objects.equals(id, bursa.id) && Objects.equals(nume, bursa.nume) && Objects.equals(prenume, bursa.prenume) && Objects.equals(tip, bursa.tip);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, nume, prenume, suma, tip);
    }

    @Override
    public String toString() {
        return "Bursa{" +
                "id=" + id +
                ", nume='" + nume + '\'' +
                ", prenume='" + prenume + '\'' +
                ", suma=" + suma +
                ", tip='" + tip + '\'' +
                '}';
    }

    public String getTip() {
        return tip;
    }

    public void setTip(String tip) {
        this.tip = tip;
    }
}
