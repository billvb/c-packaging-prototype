DEPS=-lsample
LIBDIR=-L./lib -L../lib -L../../lib
LIBNAME=lib$(shell basename $(CURDIR)).a

SRCDIR=$(CURDIR)/src
INC=-I./include -I../include -I../../include
CFLAGS=$(INC) -ansi -std=c89 -Werror -Wall -Wextra -pedantic
CC=gcc

export 

all:
	make -C build
	make -C test

clean:
	make -C build clean
	make -C test clean

