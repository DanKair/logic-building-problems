#include <iostream>
using namespace std;
// #include <vector>

int main(){
    int arr[5];
    int sum;
    // Using loop to assign the each element a user entered value
    for (int i = 0; i <= 5; i++){
        cout << "Enter the value for " << i << "th element: " << "\n";
        cin >> arr[i];
        sum += arr[i];
    }
    // Traverse the array using new syntax from c++11

    for (int element : arr) {
        cout << element << " ";
    }
  
    cout << "\nThe Sum of array is: " << sum << '\n';
}