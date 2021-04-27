#include <iostream>
#include <vector>

using namespace std;

// Return max profit 
int knapsackRecursive(vector<int> profit, vector<int> weight, int maxWeight, int index = 0) {
    if(index > profit.size()) {
        return 0;
    }
    if(weight[index] > maxWeight) 
        return knapsackRecursive(profit, weight, maxWeight, index+1);
    else 
        return max(profit[index] + knapsackRecursive(profit, weight, maxWeight-weight[index], index+1), 
            knapsackRecursive(profit, weight, maxWeight, index+1));
}

int knapsackMemoize(vector<int> profit, vector<int> weight, int maxWeight, vector<vector<int> > &mem, int index) {
    if(index < 0 || maxWeight < 0) {
        return 0;
    }
    cout << "here" << endl;
    if(maxWeight == 0 || index == 0) {
        mem[index][maxWeight] = 0;
    }
    if(weight[index] > maxWeight) {
        if(index > 0 && mem[index-1][maxWeight] != 0)
            mem[index][maxWeight] = mem[index-1][maxWeight];
        else {
            mem[index][maxWeight] = knapsackMemoize(profit, weight, maxWeight, mem, index-1);
        }
    } else {
        int netProfit = 0;
        if(index > 0 && mem[index-1][maxWeight] != 0)
            netProfit = max(netProfit, mem[index][maxWeight]);
        else 
            netProfit = max(netProfit, knapsackMemoize(profit, weight, maxWeight, mem, index-1));
        
        if(index > 0 && mem[index-1][maxWeight-weight[index]] != 0)
            netProfit = max(netProfit, profit[index] + mem[index-1][maxWeight-weight[index]]);
        else
            netProfit = max(netProfit, knapsackMemoize(profit, weight, maxWeight-weight[index], mem, index-1));
        
        mem[index][maxWeight] = netProfit;
    }
    return mem[index][maxWeight];
}

int knapsackMemoize(vector<int> profit, vector<int> weight, int maxWeight) {
    // Initializing memoization matrix to 0
    vector<vector<int> > mem(profit.size()-1, vector<int>(maxWeight, 0));

    return knapsackMemoize(profit, weight, maxWeight, mem, profit.size()-1);
}

int main() {
    vector<int> profit{1, 4, 5, 9, 7}, weight{1, 3, 4, 3, 5};
    int maxWeight = 8;
    cout << knapsackMemoize(profit, weight, maxWeight) << endl;
}
