#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
    // Open the JSON file
    std::ifstream file("data.json");
    if (!file.is_open()) {
        std::cerr << "Failed to open JSON file." << std::endl;
        return 1;
    }

    // Parse JSON data
    json j;
    try {
        file >> j;
    } catch (json::parse_error& e) {
        std::cerr << "JSON parse error: " << e.what() << std::endl;
        return 1;
    }

    // Access and display JSON data
    try {
        std::cout << "JSON data:" << std::endl;
        std::cout << "Name: " << j["name"] << std::endl;
        std::cout << "Age: " << j["age"] << std::endl;
        std::cout << "City: " << j["city"] << std::endl;
    } catch (json::exception& e) {
        std::cerr << "JSON exception: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
