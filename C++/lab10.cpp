#include <iostream>
using namespace std;
// The factorial program
/*
int main(){
    // while i != 0: res = i * (i - 1)
    int num;
    int result = 1;
    int counter = 0;
    cout << "Enter the number: " << "\n";
    cin >> num;

    // while (num > 1){
    //     result *= num;
    //     num -= 1;
    // }

    while (counter != num){
        counter += 1;
        result *= counter;
        cout << "The result is: " << result << endl;
    }

    // Why i = 2? Because you wanna 1 * 2 from the beginning, not 1 * 1 and then only 1 * 2
    /*
    for (int i = 2; i <= num; i++){
        result = result * i;
        cout << "The result is: " << result << endl;
    }
    
    cout << "The factorial of " << num << " is " << result << endl;
}
*/

int main() {
    string s;
    cout << "Enter the string of your choice: ";
    cin >> s;

    // Convert the string to uppercase using
    // ASCII values
    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= 'a' && s[i] <= 'z')
            s[i] = s[i] - 32;
    }

    cout << s;
    return 0;
}