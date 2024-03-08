#include <iostream>
#include <curl/curl.h>

// Callback function to write received data to a string
size_t WriteCallback(void *contents, size_t size, size_t nmemb, std::string *output) {
    size_t totalSize = size * nmemb;
    output->append((char *)contents, totalSize);
    return totalSize;
}

int main() {
    // Initialize libcurl
    curl_global_init(CURL_GLOBAL_ALL);
    
    // Create a CURL object
    CURL *curl = curl_easy_init();
    if (curl) {
        // Set the URL to perform the GET request
        curl_easy_setopt(curl, CURLOPT_URL, "https://flipkart.com");
        
        // Set the callback function to receive the response data
        std::string responseString;
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &responseString);
        
        // Perform the GET request
        CURLcode res = curl_easy_perform(curl);
        if (res == CURLE_OK) {
            // Print the response body
            std::cout << "Response Body:" << std::endl;
            std::cout << responseString << std::endl;
        } else {
            // Print error message if the request fails
            std::cerr << "Failed to perform request: " << curl_easy_strerror(res) << std::endl;
        }
        
        // Clean up and release resources
        curl_easy_cleanup(curl);
    } else {
        std::cerr << "Failed to initialize libcurl." << std::endl;
    }
    
    // Cleanup libcurl
    curl_global_cleanup();
    
    return 0;
}
