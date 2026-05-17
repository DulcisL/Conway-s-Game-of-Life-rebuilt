CC      = gcc
CFLAGS  = -O3 -Wall -Wextra $(shell sdl2-config --cflags)
LDFLAGS = $(shell sdl2-config --libs)
TARGET = src/main
SOURCES = src/main.c

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

clean:
	@echo "Cleaning Project"
	rm -f *.o
	rm -f $(TARGET)
	@echo "Clean Complete"

.PHONY: all clean
