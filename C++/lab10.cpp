#include <iostream>
using namespace std;
// The factorial program

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
    */
    cout << "The factorial of " << num << " is " << result << endl;
}