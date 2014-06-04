
NAME=$(shell basename $(CURDIR))
LIBNAME=lib$(shell basename $(CURDIR)).a
SHARED_LIBNAME=lib$(shell basename $(CURDIR)).so

SRCDIR=$(CURDIR)/src
INC=-I./include -I../include -I../../include
CFLAGS=$(INC) -ansi -std=c89 -Werror -Wall -Wextra -pedantic -fPIC
CC=gcc

export 

all:
	make -C build
	make -C test

clean:
	make -C build clean
	make -C test clean

