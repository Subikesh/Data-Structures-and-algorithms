#include <iostream>
#include <vector>

using namespace std;

template <typename T = int>
void printVector(vector<T> vec) {
    for(auto ite: vec) {
        cout << ite << ' ';
    }
    cout << endl;
}

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

int knapsackDp(vector<int> profit, vector<int> weight, int maxWeight, vector<vector<int> > &dp) {
    int i, w, n= profit.size();

    for(i = 0; i<=n; i++) {
        for(w = 0; w<=maxWeight; w++) {
            if(i==0) {  // If no item is there to fill
                dp[i][w] = 0;
                continue;
            }
            if(weight[i-1] > w) { // If current item cannot be added in knapsack
                dp[i][w] = dp[i-1][w];
            } else {
                dp[i][w] = max(dp[i-1][w],          // If item not included
                              (dp[i-1][w-weight[i-1]]+profit[i-1]) );   // If item is included
                if(dp[i-1][w] > dp[i-1][w-weight[i-1]]+profit[i-1]) {
                    dp[i][w] = dp[i-1][w];
                }
                else {
                    dp[i][w] = dp[i-1][w-weight[i-1]]+profit[i-1];
                }
            }
        }
    }
    return dp[n][maxWeight];
}

vector<bool> sackRetrace(vector<vector<int> > dp, vector<int> weight) {
    int i = dp.size()-1, j= dp[0].size()-1;
    vector<bool> knapsack(weight.size(), false);
    while(i>0) {
        if(dp[i-1][j] != dp[i][j]) {
            // retraced.push_back(i-1);
            knapsack[i-1] = true;
            j -= weight[i-1];
        }
        i--;
    }
    return knapsack;
}

int knapsackDp(vector<int> profit, vector<int> weight, int maxWeight) {
    // Initializing DP matrix to 0
    vector<vector<int> > dp(profit.size()+1, vector<int>(maxWeight+1, 0));
    int res = knapsackDp(profit, weight, maxWeight, dp);
    vector<bool> sackItems = sackRetrace(dp, weight);
    cout << "Sack items ";
    printVector<bool>(sackItems);
    return res;
}

int main() {
    vector<int> profit{1, 4, 8, 5, 7}, weight{1, 3, 4, 3, 5};
    int maxWeight = 8;
    cout << "Weights "; printVector(weight);
    cout << "Profits "; printVector(profit);
    int maxProfit =  knapsackDp(profit, weight, maxWeight);
    cout << "Max profit: " << maxProfit;
    return 0;
}
