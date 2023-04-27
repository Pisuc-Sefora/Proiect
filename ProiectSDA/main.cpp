#include <iostream>
#include "RepositoryFile/Repository.h"
#include "Service/Service.h"
#include "UI/UI.h"

int main() {
    Repository repo=Repository();
    Service service=Service(repo);
    UI ui=UI(service);
    cout<<"Hello 1";
    ui.runApp();

    return 0;
}
