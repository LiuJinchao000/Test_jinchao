#include <class.h>
#include <iostream>
using namespace std;
Animal::Animal()
{
        m_name="none";
        m_age=0;
        std::cout<<m_name<<"animal initial ():"<<m_age<<"//"<<m_name<<std::endl;
}

Animal::~Animal()
{
    std::cout<<m_name<<"animal xigou with:"<<m_age<<"//"<<m_name<<std::endl;

}

Animal::Animal(const std::string &name, int age)
{
        m_name=name;
        m_age=age;

        std::cout<<m_name<<"animal initial with:"<<m_age<<"//"<<m_name<<std::endl;

}

void Animal::set_age(int age)
{
        using namespace std;
        std::cout<<"animal previous age:"<<m_age<<std::endl;
        m_age=age;
        cout<<"set age :"<<m_age<<endl;
}

void Animal::set_name(std::string name)
{
        using namespace std;
        cout<<m_name<<"---pre---"<<endl;
        m_name=name;
        cout<<m_name<<"------"<<endl;
}

void Animal::show_age() const
{
        std::cout<<"age older is"<<m_age<<endl;
}

const Animal & Animal::compare_age(const Animal &a) const
{
    // TODO: insert return statement here
    if(a.m_age>m_age)
        return a;
    else
        return *this;


}

Bank::Bank()
{
}

Bank::Bank(const std::string &name, const std::string &accont, double balence)
{
}

void Bank::show(void) const
{
        std::cout<<m_account<<m_balence<<m_account<<std::endl;
}

void Bank::deposit(double balence)
{
        m_balence+=balence;
}

void Bank::withdraw(double balence)
{
        m_balence-=balence;

}
