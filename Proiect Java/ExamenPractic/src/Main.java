import repository.Repository;
import service.Service;
import ui.Ui;

public class Main {
    public static void main(String[] args) {
        Repository repository = new Repository();
        Service service = new Service(repository);
        service.add(1L,"Andronescu","Ilinca","merit",350);
        service.add(2L,"Pop","Ana","social",500);
        service.add(3L,"Popescu","Ion","social",300);
        service.add(4L,"Pop","Maria","facultate",800);
        service.add(5L,"Andronescu","Ale","social",400);
        service.add(6L,"Rus","Alex","merit",200);
        service.add(7L,"Zubascu","Ina","venit",450);
        Ui ui = new Ui(service);
        ui.run();
    }
}