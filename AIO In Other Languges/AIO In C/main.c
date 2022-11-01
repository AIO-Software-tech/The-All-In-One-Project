#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

//Info Change "Your Username" and "Your Password" to what you want
//Info You cant add spaces to your username

char cUsername[50] = "Your Username";
char cPassword[50] = "Your Password";

void pause()
{
    system("pause>nul");
    return;
}

void mainMenu()
{
    char MMS[5];
    printf(" \n");
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
    printf("Please Select One Of The Following Options 1,2,3,4: ");
    scanf("%s", MMS);
    if (strcmp(MMS, "1") == 0)
    {
        printf("1111\n");
    }
    else
    {
        printf("LLLL\n");rrr          
    }
}

void login(cUsername, cPassword)
{
    char Username[30], Password[30];
    printf("Username: ");
    scanf("%s", &Username);
    printf("Password: ");
    scanf("%s", &Password);
    if (strcmp(Username, "Ollie") == 0)
    {
        if (strcmp(Password, "123") == 0)
        {
            printf(" \n");
            printf("Hi Ollie\n");
            mainMenu();
        }
    }
    else if (strcmp(Username, "Imre") == 0)
    {
        if (strcmp(Password, "123") == 0)
        {
            printf(" \n");
            printf("Imre\n");
            mainMenu();
        }
    }
    else if (strcmp(Username, "Admin") == 0)
    {
        if (strcmp(Password, "123") == 0)
        {
            printf(" \n");
            printf("Hi Admin\n");
            mainMenu();
        }
    }
    else if (strcmp(Username, "Guest") == 0)
    {
        if (strcmp(Password, "123") == 0)
        {
            printf(" \n");
            printf("Hi Guest\n");
            mainMenu();
        }
    }
    else if (strcmp(Username, cUsername) == 0)
    {
        if (strcmp(Password, cPassword) == 0)
        {
            printf(" \n");
            printf("Hi %s\n", cUsername);
            mainMenu();
        }
    }
    else
    {
        MessageBox(0, "AIO Error 2 Incorrect Username Or Password", "AIO Error", MB_OK);
        printf("l rip ");
    }

}

int main()
{
    printf("All-In-One By Imre Kiss And Oliver Boucher\n");
    printf("\n");
    printf("Verstion 0.0.2 REV-1 Alpha-1 2022\n");
    printf("\n");
    login(cUsername, cPassword);
}