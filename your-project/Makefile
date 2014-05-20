INC=-I./cpak-deps/include
LIBS=-L./cpak-deps/lib

DEPS=$(wildcard cpak-deps/lib/*.a)

all:
	gcc -std=c99 -o your-project.bin src/your-project.c $(INC) $(LIBS) $(DEPS)

clean:
	rm -f your-project.bin
