#include <iostream>
#include <string>
#include <vector>
#include <queue>
// for formatting purpose
#include <iomanip>

using namespace std;

// print non -1 values in int array
void printIntArray(int[], const int);
void printVectorPuzzle(const vector<int> &, const int);
bool checkVal(int[], const int, const int);

int main() {
    int n = 0;
    cout << "Taking input for n x n puzzle. \n\n\tFirst, please enter the size of n: ";
    cin >> n;

    cout << "\nTaking input for " << n << " x " << n << " puzzle." << endl;

    const int SIZE = n * n;
    int unusedNums[SIZE];
    cout << "\nUnused Numbers: { ";
    for(int i = 0; i < SIZE; ++i) {
        unusedNums[i] = i;
    }
    printIntArray(unusedNums, SIZE);
    cout << "}" << endl;

    int column = 1;
    int row = 1;
    int val = 0;
    vector<int> puzzle;
    cout << "\nNow, please enter" << endl;
    while (column <= n && row <= n) {
        cout << "Available options: ";
        printIntArray(unusedNums, SIZE);
        cout << endl;

        cout << "\trow: [" << row << "], column: [" << column << "] : ";
        while(cin >> val) { 
            if(checkVal(unusedNums, SIZE, val)) {
                break;
            }

            cout << "{ " << val << " } already exist or is not valid option\n" << "\tTry again: ";
        }
        
        puzzle.push_back(val);

       
        column++;
        if(row < n && column > n) {
            row++;
            column = 1;
        }
    }

    cout << endl << "result:" << endl;
    printVectorPuzzle(puzzle, n);
    cout << endl;
    

    return 0;
} 


void printIntArray(int arr[], const int SIZE) {
    for(int i = 0; i < SIZE; ++i) {
        if(arr[i] != -1) {
            cout << arr[i] << " ";
        }
    }

    return;
}

// my original code
// void printVectorPuzzle(const vector<int> &puzzle, const int N) {
//     int counter = 1;

//     for(int i = 0; i < puzzle.size(); ++i) {
//         cout << puzzle.at(i) << " ";
//         counter++;
//         if(counter > N) {
//             cout << endl;
//             counter = 1;
//         }
//     }

//     return;
// }


// getting help with formatting from outside library and LM's
void printVectorPuzzle(const vector<int> &puzzle, const int N) {
    // Find width based on max possible number (N*N - 1)
    int maxNum = N * N - 1;
    int width = to_string(maxNum).length() + 1; // +1 for spacing

    for (int i = 0; i < puzzle.size(); ++i) {
        cout << setw(width) << puzzle.at(i);
        if ((i + 1) % N == 0)
            cout << '\n';
    }

    return; 
}

bool checkVal(int arr[], const int SIZE, const int VAL) {
    for(int i = 0; i < SIZE; ++i) {
        // cout << "comparing ( " << arr[i] << ", " << VAL << " )" << endl;
        if(arr[i] == VAL) {
            arr[i] = -1;
            return true;
        }
    }

    return false;
}