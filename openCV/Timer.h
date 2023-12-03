#include <chrono>
#include <iostream>
class Timer
{    
private:
    std::chrono::time_point<std::chrono::high_resolution_clock> start,end;
    std::chrono::duration<double> duration;
public:
    Timer()
    {
        start=std::chrono::high_resolution_clock::now();
    }
    ~Timer()
    {
        end=std::chrono::high_resolution_clock::now();
        duration=end-start;
        double ms=duration.count()*1000.0;
        std::cout<<"Timer took : "<<ms<<std::endl;
    }
};