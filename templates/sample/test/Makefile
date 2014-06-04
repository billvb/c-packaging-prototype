
all: shared
	$(CC) $(CFLAGS) -static -o test.bin test.c ../build/$(LIBNAME)

shared:
	$(CC) $(CFLAGS) test.c -o test.shared.bin -L../build -l$(NAME)

clean:
	rm -f *.o *.so *.a *.bin
