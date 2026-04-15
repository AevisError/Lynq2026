#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int stairs = get_int("stairs: ");

    // if user inputs negative ints and zero, ask again.
    while (stairs <= 0)
    {
        stairs = get_int("stairs: ");
    }

    int floor, brick, gap;

    // no. of steps...
    for (floor = 1; floor <= stairs; floor++)
    {

        // number of spaces before each line...
        for (gap = 1; gap <= (stairs - floor); gap++)
        {
            printf(" ");
        }

        // now display "x"....
        for (brick = 1; brick <= (floor * 2); brick++)
        {
            printf("#");
            if (brick == floor)
            {
                printf("  ");
            }
        }

        // go to next line...
        printf("\n");
    }
}