#pragma once
#include <string>
class Animal
{
private:
        std::string m_name;
        int m_age;
public:
        Animal();
        ~Animal();
        Animal(const std::string &name,int age=3);
        void set_age(int age);    
        void set_name(std::string name);    
        void show_age() const;
        const Animal & compare_age(const Animal & a) const;
};


class Bank
{
private:
        char m_name[40];
        char m_account[10];
        double m_balence;
public:
        Bank();
        Bank(const std::string & name,const std::string & accont,double balence);
        void show(void) const;
        void deposit(double balence);
        void withdraw(double balence);
};