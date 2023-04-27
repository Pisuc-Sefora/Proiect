package domain;

public class BursaValidator implements Validator<Bursa> {
    @Override
    public void validate(Bursa entity) throws ValidatorException {
        if (entity.getNume() == null || entity.getPrenume() == null)
            throw new ValidatorException("Names cannot be null");
        if (entity.getSuma() == 0)
            throw new ValidatorException("Celebritatea cannot be null");
    }
}
