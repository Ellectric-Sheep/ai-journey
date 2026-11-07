#include <iostream>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int x : v) {
        sum += x;
    }
    std::cout << "sum = " << sum << std::endl;
    std::cout << "Hello, C++!" << std::endl;
    return 0;
}
