#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <unistd.h>

// Global variables
std::vector<std::string> possible_actions = {"Rock", "Paper", "Scissors"};
int Total_Games_Played = 1;
int Total_Wins = 0;
int Total_Loss = 0;

// Function declarations
void clear_screen();
void welcomemessage();
void presentchoices();
std::string get_userchoice();
std::string get_pcchoice();
void get_gameresult(const std::string& user_action, const std::string& pc_action);
void get_gamestats();
void exitmessage();
void PlayAgain();

int main() {
    srand(time(nullptr)); // Seed the random number generator
    welcomemessage();
    presentchoices();
    std::string user_action = get_userchoice();
    std::string pc_action = get_pcchoice();
    std::cout << "-----------------------------------\n";
    get_gameresult(user_action, pc_action);
    PlayAgain();
    return 0;
}

void clear_screen() {
    system("clear || cls"); // Clear the screen
}

void welcomemessage() {
    std::cout << "\nWelcome to Rock-Paper-Scissors Game!\n";
}

void presentchoices() {
    std::cout << "             Game No. " << Total_Games_Played << std::endl;
    std::cout << "-----------------------------------\nChoose only one from the following options:\n";
    for (const auto& choice : possible_actions) {
        std::cout << choice << std::endl;
    }
    std::cout << "-----------------------------------" << std::endl;
}

std::string get_userchoice() {
    std::string user_action;
    std::cout << "Your choice is: ";
    std::getline(std::cin, user_action);
    return user_action;
}

std::string get_pcchoice() {
    std::cout << "Waiting for PC";
    for (int dot = 0; dot < 9; dot++) {
        usleep(210000); // Sleep for 0.21 seconds
        std::cout << ".";
        std::cout.flush();
    }
    std::string pc_action = possible_actions[rand() % possible_actions.size()];
    std::cout << "\rPC chose " << pc_action << ".   " << std::endl; // Print PC's choice, overwrite "Waiting for PC..." with spaces
    return pc_action;
}

void get_gameresult(const std::string& user_action, const std::string& pc_action) {
    if (user_action == pc_action) {
        std::cout << "You both chose " << user_action << ". It's a tie!\n***********************************\n";
    } else if ((user_action == "Rock" && pc_action == "Scissors") ||
               (user_action == "Paper" && pc_action == "Rock") ||
               (user_action == "Scissors" && pc_action == "Paper")) {
        std::cout << "You win!\n***********************************\n";
        Total_Wins++;
    } else {
        std::cout << "You lose!\n***********************************\n";
        Total_Loss++;
    }
}

void get_gamestats() {
    std::cout << Total_Games_Played << " Game/s,\n";
    std::cout << Total_Wins << " total wins, and\n";
    std::cout << Total_Loss << " total losses\n";
}

void exitmessage() {
    std::cout << "Thank you for playing! You made a total of\n";
    get_gamestats();
}

void PlayAgain() {
    while (true) {
        std::string Continue_Playing;
        std::cout << "Would you like to continue playing? (Y/N): ";
        std::getline(std::cin, Continue_Playing);
        if (Continue_Playing[0] == 'Y' || Continue_Playing[0] == 'y') {
            clear_screen();
            Total_Games_Played++;
            main();
        } else if (Continue_Playing[0] == 'N' || Continue_Playing[0] == 'n') {
            clear_screen();
            exitmessage();
            break;
        }
    }
}
