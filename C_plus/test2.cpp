#include <iostream>
using namespace std;

int main(){
    cout << "구매금액을 입력하세요" << endl;
    int caltot, calpoint;
    cin >> caltot;
    calpoint = caltot * 0.01;
    cout << "포인트는" << calpoint << "점 입니다.\n";
}