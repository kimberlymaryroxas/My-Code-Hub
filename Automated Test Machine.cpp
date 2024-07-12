#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <unistd.h>
#include <algorithm>

std::vector<std::string> username = {"Kimmy", "Kim", "Kimberly"};
std::vector<std::string> passcode = {"Kimmy123", "Kim123", "Kimberly123"};
std::vector<std::string> bank_options = {"Check Balance", "Withdraw", "Deposit", "Log to another Account", "Quit"};
std::vector<int> Balance = {1000, 7000, 15000}; // Initial balance, adjust as needed

void clear_screen() {
    if (system("clear") || system("cls")) {} // Clear the screen
}

void welcomemessage();

void login();

void access_check(const std::string& user_input, const std::string& pass_input);

void presentchoices(const std::string& user_input);

void get_userchoice(const std::string& user_input);

void checkbalance(const std::string& user_input);

void withdraw(const std::string& user_input);

void deposit(const std::string& user_input);

void quit();

int main() {
    welcomemessage();
    login();
    return 0;
}

void welcomemessage() {
    std::cout << "\n-----------------------------------\nWelcome to BEL Banking!\n-----------------------------------" << std::endl;
}

void login() {
    std::string user_input, pass_input;
    std::cout << "Enter your username: ";
    std::getline(std::cin, user_input);
    std::cout << "Enter your password: ";
    std::getline(std::cin, pass_input);
    access_check(user_input, pass_input);
}

void access_check(const std::string& user_input, const std::string& pass_input) {
    auto it = std::find(username.begin(), username.end(), user_input);
    if (it != username.end() && pass_input == passcode[std::distance(username.begin(), it)]) {
        std::cout << "Access Granted for " << user_input << "!" << std::endl;
        std::cout << "Entering account";
        for (int dot = 0; dot < 3; dot++) {
            usleep(1000000); // Sleep for 1 second
            std::cout << ".";
            std::cout.flush();
        }
        std::cout << std::endl;
        presentchoices(user_input);
    } else {
        std::cout << "Access Denied!" << std::endl;
        login();
    }
}

void presentchoices(const std::string& user_input) {
    std::cout << "\nChoose only one from the following options:" << std::endl;
    for (size_t i = 0; i < bank_options.size(); i++) {
        std::cout << "[" << i + 1 << "] " << bank_options[i] << std::endl;
    }
    std::cout << "-----------------------------------" << std::endl;
    get_userchoice(user_input);
}

void get_userchoice(const std::string& user_input) {
    try {
        int user_action;
        std::cout << "Choose an action: ";
        std::cin >> user_action;
        std::cin.ignore(); // Clear input buffer
        if (user_action >= 1 && user_action <= bank_options.size()) {
            switch (user_action) {
                case 1:
                    checkbalance(user_input);
                    break;
                case 2:
                    withdraw(user_input);
                    break;
                case 3:
                    deposit(user_input);
                    break;
                case 4:
                    login();
                    break;
                case 5:
                    quit();
                    break;
            }
        } else {
            std::cout << "Invalid choice." << std::endl;
            get_userchoice(user_input);
        }
    } catch (...) {
        std::cout << "Please enter a number." << std::endl;
        get_userchoice(user_input);
    }
}

void checkbalance(const std::string& user_input) {
    auto it = std::find(username.begin(), username.end(), user_input);
    if (it != username.end()) {
        int user_index = std::distance(username.begin(), it);
        std::cout << "Your current balance is: $" << Balance[user_index] << std::endl;
        presentchoices(user_input);
    }
}

void withdraw(const std::string& user_input) {
    auto it = std::find(username.begin(), username.end(), user_input);
    if (it != username.end()) {
        int user_index = std::distance(username.begin(), it);
        int withdraw_amt;
        std::cout << "Enter amount to be withdrawn: ";
        std::cin >> withdraw_amt;
        if (Balance[user_index] >= withdraw_amt) {
            Balance[user_index] -= withdraw_amt;
            std::cout << "Withdrawing " << withdraw_amt;
            for (int dot = 0; dot < 3; dot++) {
                usleep(1000000); // Sleep for 1 second
                std::cout << ".";
                std::cout.flush();
            }
            std::cout << "$" << withdraw_amt << " has been successfully withdrawn from your account!" << std::endl;
        } else {
            std::cout << "Insufficient balance. You cannot withdraw " << withdraw_amt << "." << std::endl;
        }
        presentchoices(user_input);
    }
}

void deposit(const std::string& user_input) {
    auto it = std::find(username.begin(), username.end(), user_input);
    if (it != username.end()) {
        int user_index = std::distance(username.begin(), it);
        int deposit_amt;
        std::cout << "Enter amount to be deposited: ";
        std::cin >> deposit_amt;
        Balance[user_index] += deposit_amt;
        std::cout << "Depositing " << deposit_amt;
        for (int dot = 0; dot < 3; dot++) {
            usleep(1000000); // Sleep for 1 second
            std::cout << ".";
            std::cout.flush();
        }
        std::cout << "$" << deposit_amt << " has been successfully deposited to your account!" << std::endl;
        presentchoices(user_input);
    }
}

void quit() {
    std::cout << "Thank you for banking with us!" << std::endl;
    exit(0);
}
