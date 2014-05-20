#include <extender.h>
#include <sample.h>
#include <stdio.h>

void EXTENDER_helloworld(void)
{

    printf("Note from extender, calling sample.\n");
    SAMPLE_helloworld();
}
