#include <sample.h>
#include <extender.h>

#include <string.h>
#include <stdio.h>

int main(int argc, char ** argv)
{
    EXTENDER_helloworld();
    SAMPLE_helloworld();

    for (int i=0; i < argc; i++)
    {
        printf("[%2d] ", strlen(argv[i]));
    }

    printf("\n");
    return 0;
}
