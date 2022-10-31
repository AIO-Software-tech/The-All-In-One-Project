#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

char *user1 = 'Ollie';
char user2[10] = 'Imre';
char user3[10] = 'Admin';
char user4[10] = 'Guest';
char user5[10] = 'D';

void pause() {
    system("pause>nul");
    return;
}

int mainMenu(){
    printf(" ");
    printf("Selection Menu: Please Select One Of The Options\n");
    printf("O_______________________________________________O\n");
    printf("|                                               |\n");
    printf("|   1. = Personal                               |\n");
    printf("|                                               |\n");
    printf("|   2. = Calculations                           |\n");
    printf("|                                               |\n");
    printf("|   3. = Games                                  |\n");
    printf("|                                               |\n");
    printf("|   4. = Error Codes                            |\n");
    printf("|                                               |\n");
    printf("|   5. = Close                                  |\n");
    printf("|                                               |\n");
    printf("O_______________________________________________O\n");
}

int login() {
    char Username[30], Password[30];
    printf("Username: ");
    scanf("%s", &Username);

    printf("Password: ");
    scanf("%s", &Password);
    if (Username == "Ollie" && Password == "123"){
        printf("Hi Ollie\n");
        mainMenu();
    } else if(Username == "Admin"){
        printf("Hi Admin\n");
    } else if(Username == "Imre"){
        printf("Hi Imre\n");
    } else {
        MessageBox(0,"AIO Error 2 Incorrect Username Or Password", "AIO Error", MB_OK );
    }
    return 0;
}  

int main() {
    printf("All-In-One By Imre Kiss And Oliver Boucher\n");
    printf("\n");
    printf("Verstion 0.0.2 REV-1 Alpha-1 2022\n");
    printf("\n");
    login();
}