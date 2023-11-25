#include <cereal/archives/json.hpp>
#include <iostream>

struct Minimal
{
  std::string myData;

  template <class Archive>
  std::string save_minimal( Archive const & ) const
  { return myData; }

  template <class Archive>
  void load_minimal( Archive const &, std::string const & value )
  { myData = value; }
};

struct Normal
{
  std::string myData;

  template <class Archive>
  void serialize( Archive & ar )
  { ar( myData ); }
};

int main()
{
  Minimal m = {"minimal"};
  Normal  n = {"normal"};

  cereal::JSONOutputArchive ar( std::cout );
  ar( CEREAL_NVP(m), CEREAL_NVP(n) );
}