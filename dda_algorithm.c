#include <stdio.h>
#include <stdlib.h>
#include <graphic.h>
#include <math.h>


int abs (int n)
{
    return ((n>0)? n: (n*(-1)));
}

void DDA(int x0, int y0, int x1, int y1)
{
    int dx = x1-x0;
    int dy = y1-y0;

    int steps = abs(dx)>abs(dy)? abs(dx):abs(dy);

    float xinc = dx/steps;
    float yinc = dy/steps;

    for (int i=1; i<=steps;i++)
    {
        putpixel(x1,y1,RED);
        x1 += xinc;
        y1 += yinc;
    }
}
int main()
{
    int gd = DETECT, gm;

    initgraph(&gd, &gm, "");

    int x0=100 y0=100, x1=200, y1=200;
    DDA(x0,y0,x1,y1);

    return 0;
}
