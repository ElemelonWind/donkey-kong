// hi cindy

#include <Windows.h>
#include <stdio.h>
#include <iostream>
#include <chrono>
#include <thread>

void sendClick()
{
    INPUT Inputs[2] = {0};

    // left click
    Inputs[0].type = INPUT_MOUSE;
    Inputs[0].mi.dwFlags = MOUSEEVENTF_LEFTDOWN;

    // release
    Inputs[1].type = INPUT_MOUSE;
    Inputs[1].mi.dwFlags = MOUSEEVENTF_LEFTUP;

    // actually click
    SendInput(3, Inputs, sizeof(INPUT));
}

int main(int argc, char **argv)
{
    // functionally the same as time.delay(5) in python
    std::this_thread::sleep_for(std::chrono::seconds(5));

    POINT cursor;          // access cursor
    GetCursorPos(&cursor); // acquire cursor location
    HDC hdc = GetDC(NULL); // get drawable screen (device context)

    int count = 0;
    while (count < 10)
    {
        COLORREF color = GetPixel(hdc, cursor.x, cursor.y); // get color of screen at cursor

        // straightforward
        int r = GetRValue(color);
        int g = GetGValue(color);
        int b = GetBValue(color);
        // std::cout << r << " " << g << " " << b << "\n";

        if (r == 206 && g == 38 && b == 54)
        {
            continue;
        }

        sendClick();
        count++;

        // it will literally click 10 times before the color switches back to blue so this needs to be here
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }

    // release screen (device context) for other applications to use
    ReleaseDC(NULL, hdc);
    return 0;

    // 18ms avg...
}