#include <bits/stdc++.h>

using namespace std;

class Customer
{
public:
    int id;
    Customer(int id):id(id) {}
};

class Booking
{
public:
    int id;
    char from;
    char to;
    int time;
    Customer *cust;
    int rent;
    Booking(int id, int cust_id, char from, char to, int time):id(id), from(from), to(to), time(time) {
        cust = new Customer(cust_id);
    }

    void get_summary() {
        cout << id << '\t' << cust->id << '\t' << from << '\t' << to << '\t' << rent << endl;
    }
};

class Taxi
{
public:
    int id;
    char location;
    // Time after which taxi is available
    int available;
    int earning;
    vector<Booking> bookings;
    Taxi(): id(0){}
    Taxi(int id):id(id), location('A'), available(0), earning(0) {}

    void get_summary() {
        cout << "Taxi-" << id << "\tTotal Earnings: Rs." << earning << endl
            << "BookingId \tCustomerId \tFrom \tTo \tAmount"<<endl;
        for(auto booking = bookings.begin(); booking != bookings.end(); booking++) {
            booking->get_summary();
        cout << endl;
        }
    }

};

class TaxiBooking
{
private:
    vector<Taxi> taxis;
    int booking_id;
public:
    TaxiBooking(vector<Taxi> taxi_list):taxis(taxi_list) {
        booking_id = 1;
    }
    
    bool book_taxi(int cust_id, char from, char to, int time) {
        Booking book(booking_id++, cust_id, from, to, time);
        Taxi *min_taxi;
        int min_dist = INT_MAX;
        for(int i=0; i<taxis.size(); i++) {
            if(taxis[i].available <= time) {
                if((abs(taxis[i].location-from) < min_dist)||(min_dist == abs(taxis[i].location-from) && taxis[i].earning < min_taxi->earning)) {
                    min_dist = (taxis[i].location-from);
                    min_taxi = &taxis[i];
                }
            }
        }
        if(min_dist == INT_MAX) {
            cout << "Taxi not available" << endl;
            cout << "Booking rejected" << endl;
            return false;
        }
        else {
            calculate_amt(*min_taxi, book);
            min_taxi->bookings.push_back(book);
            cout << "Taxi can be alloted." << endl;
            cout << "Taxi-" << min_taxi->id << " is alloted" << endl;
            return true;
        }
    }

    void calculate_amt(Taxi &taxi, Booking &book) {
        taxi.available = book.time + abs(taxi.location - book.from) + abs(book.from - book.to);
        int distance = 15 * abs(book.from-book.to);
        book.rent = (distance-5) * 10 + 100;
        taxi.earning += book.rent;
    }

    void get_summary() {
        for(int i=0; i<taxis.size() ; i++) {
            taxis[i].get_summary();
        }
    }
};

int main() {
    int n, choice = 0, time, cust_id;
    char from, to;
    cout << "number of taxis: ";    cin >> n;
    vector<Taxi> taxis;
    for(int i=0; i<n; i++) 
        taxis.push_back(Taxi(i+1));
    TaxiBooking book_obj(taxis);
    while(true) {
        cout << "Main Menu" << endl
            << "1. Book taxi" << endl
            << "2. Get summary" << endl
            << "3. Exit" << endl;
        cin >> choice;
        switch(choice) {
            case 1:
                cout << "Enter Customer_id, From, to, time :";
                cin >> cust_id >> from >> to >> time;
                book_obj.book_taxi(cust_id, toupper(from), toupper(to), time);
                // book.push_back(Booking(book.size()+1, cust_id, from, to, time));
                // if(!book[book.size()-1].book_taxi(taxis)) {
                //     book.pop_back();
                // }
            break;
            case 2:
                // for(int i=0; i<n; i++) 
                //     taxis[i].get_summary();
                book_obj.get_summary();
            break;
            default:
                return 0;
        }

    }
    return 0;
}