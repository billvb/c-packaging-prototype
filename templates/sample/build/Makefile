
SRCS=$(wildcard $(SRCDIR)/*.c)
OBJS=$(SRCS:.c=.o)
SHARED_OBJS=$(SRCS:.c=.o)

all: $(OBJS) shared
	ar cr $(LIBNAME) $(OBJS) 

shared: $(OBJS)
	$(CC) -shared -o lib$(NAME).so $(OBJS)

clean:
	rm -f *.o *.so *.a $(OBJS)
