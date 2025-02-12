#include <iostream>
#include <string>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

// Function to handle the response from the API
size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

// Function to call OpenAI API
std::string callChatGPT(const std::string& question) {
    const std::string apiKey = "YOUR_API_KEY"; // Replace with your OpenAI API Key
    const std::string url = "https://api.openai.com/v1/chat/completions";

    CURL* curl;
    CURLcode res;
    std::string readBuffer;

    json requestBody = {
        {"model", "gpt-3.5-turbo"}, // Specify the model you want to use
        {"messages", json::array({ {{"role", "user"}, {"content", question}} })} },
        {"max_tokens", 150} // Limit the response length
    };

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();

    if (curl) {
        struct curl_slist* headers = NULL;
        headers = curl_slist_append(headers, ("Authorization: Bearer " + apiKey).c_str());
        headers = curl_slist_append(headers, "Content-Type: application/json");

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, requestBody.dump().c_str());

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        res = curl_easy_perform(curl);

        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();

    return readBuffer; // Return the response
}

int main() {
    std::string userInput;
    std::string defaultQuestion = "What is the capital of France?"; // Default question

    // You can replace this line with user input if desired
    userInput = defaultQuestion; // Or std::getline(std::cin, userInput);

    std::string response = callChatGPT(userInput);

    // Parse the JSON response
    json responseJson = json::parse(response);

    // Access the assistant's reply
    std::string answer = responseJson["choices"][0]["message"]["content"];

    std::cout << "ChatGPT's response: " << answer << std::endl;

    return 0;
}
