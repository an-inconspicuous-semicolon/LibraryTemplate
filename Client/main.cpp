//
// Created by An Inconspicuous Semicolon on 20/12/2024.
//

#include <Windows.h>
#include <LibraryTemplate/Library.hpp>

int main()
{
    isc::say_hello(NAME);
    return 0;
}

int aWinMain(HINSTANCE, HINSTANCE, LPCSTR, int)
{
    return main();
}

