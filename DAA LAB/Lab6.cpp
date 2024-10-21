#include<iostream>
#include<cstdlib> // For rand()

using namespace std;

int partition(int *arr, int p, int r) {
    int x = arr[r];
    int i = p - 1;
    for (int j = p; j < r; j++) {
        if (arr[j] <= x) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[r]);
    return i + 1;
}

void quickSort(int *arr, int p, int r) {
    if (p < r) {
        int q = partition(arr, p, r);
        quickSort(arr, p, q - 1);
        quickSort(arr, q + 1, r);
    }
}

// Randomized partition function
int randomPartition(int *arr, int p, int r) {
    // Randomly select a pivot index between p and r
    int randomIndex = rand() % (r - p + 1) + p; // Random index between p and r
    swap(arr[randomIndex], arr[r]); // Swap the randomly chosen pivot with the last element
    return partition(arr, p, r); // Call partition on the modified array
}

// Randomized Quick Sort
void randomizedQuickSort(int *arr, int p, int r) {
    if (p < r) {
        int q = randomPartition(arr, p, r);
        randomizedQuickSort(arr, p, q - 1);
        randomizedQuickSort(arr, q + 1, r);
    }
}

int main() {
    int A[] = {60, 10, 50, 90, 30};
    int n = sizeof(A) / sizeof(A[0]);
    
    // Call the randomized quick sort
    randomizedQuickSort(A, 0, n - 1);
    
    // Print sorted array
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << '\n';
    
    return 0;
}
