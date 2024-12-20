//
// Created by An Inconspicuous Semicolon on 20/12/2024.
//

#include "Library.hpp"

#include <iostream>

namespace isc
{
void say_hello(std::string_view name)
{
    std::cout << "Hello, " << name << "!" << std::endl;
}
}
