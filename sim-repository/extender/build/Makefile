
SRCS=$(wildcard $(SRCDIR)/*.c)
OBJS=$(SRCS:.c=.o)

all: $(OBJS)
	ar cr $(LIBNAME) $(OBJS)

clean:
	rm -f *.o *.so *.a $(OBJS)
