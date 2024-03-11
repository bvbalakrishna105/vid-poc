#include <iostream>

int main(int argc, char *argv[]) {
    // Check if there is exactly one argument
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <argument>" << std::endl;
        return 1; // Return error code 1
    }

    // Print the argument passed to the program
    std::cout << "Argument provided: " << argv[1] << std::endl;

    return 0; // Return success
}
