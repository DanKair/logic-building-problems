// C++ program for displaying only multiplies of 3 and 5 (e.g 3, 6, 9, 10, 12, 15 and etc)
#include <iostream>
using namespace std;

// 1. We will run a loop till the n-term
// 2. i value will be added to sum number
// 3. if sum % 3 == 0: print sum, else: do nothing
// 4. Or You can create another variable called multiplies_of_five_or_three and assign sum value to them
// 5. At the end, display this variable
/*
int main(){
    int sum = 0;
    int n;
    cout << "Enter the end value till which loop will execute: " << "\n";
    cin >> n;

    for (int i = 0; i <= n; i++){
        sum += i;
        if(sum % 3 == 0 || sum % 5 == 0){
            cout << sum << "\n";
        }

    }
}
    */

// 1. Declare prev1, prev2, sum and n variables
// 2. Assign prev1 = 0 and prev2 = 1, because the first values are 0 and 1
// 3. Iterate till n (n is user input value)
// 4. our sum should hold the sum of 2 previous values
// 5. update the first value with second value and second value update to the new sum value

int main(){
    int prev1 = 0;
    int prev2 = 1;
    int sum = 0;
    int n;
    cout << "How many times you wanna to do fibonnaci series: " << "\n";
    cin >> n;

    for (int i = 0; i < n; i++){
        sum = prev1 + prev2;
        prev1 = prev2;
        prev2 = sum;
        cout << "The number is: " << sum << "\n";
    }

}


/* The pattern building program
int main(){
    int rows;
    cout << "Enter the number of row for your triangle: " << "\n";
    cin >> rows;

    for (int i=1; i <= rows; i++){
        for (int j=1; j <= i; j++){
            cout << "* ";
        }
    cout << endl;
  }
}
*/
