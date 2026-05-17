#define SDL_MAIN_USE_CALLBACKS 1
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

static SDL_Window *window = NULL;
static SDL_Renderer *renderer = NULL;
static Uint64 last_time = 0;

#define WINDOW_HEIGHT = 1080;
#define WINDOW_WIDTH = 1920;

#define MIN_PIXELS_PER_SECOND = 10;
#define MAX_PIXELS_PER_SECOND = 20;

int main(int argc, char *argv[]) {
  // Constants
  int GAME_X, GAME_Y;
  GAME_X = 1920;
  GAME_Y = 1080;
  bool RUNNING = true;
  // Use Calloc to ensure the start is all 0's'
  unsigned char *GAME_MATRIX =
      (unsigned char *)calloc(GAME_X * GAME_Y, sizeof(bool));

  //-----------------------------------------------------
  // Var declarations
  int scale, mouse_x, mouse_y;
  scale = 10;

  //-----------------------------------------------------
  // Init
  if (GAME_MATRIX == NULL) {
    printf("\nCalloc failed");
    return 1;
  }
  if (!SDL_INIT(SDL_INIT_VIDEO)) {
    printf("\nCould not initiallize SDL_Window");
    return 1;
  }

  //-----------------------------------------------------
  // Logic
  while (RUNNING) {
    for (int y = 0; y < GAME_Y; y++) {
      for (int x = 0; x < GAME_X; x++) {
        // adjust for indexing
        unsigned int index = y * GAME_X + x;
        if (GAME_MATRIX[index]) {
          int live_count = 0;
          // Get neighbor indexes
          unsigned int north, south, east, west, north_east, north_west,
              south_east, south_west;
          north = index - GAME_X;
          north_east = index - GAME_X + 1;
          east = index + 1;
          south_west = index + GAME_X + 1;
          south = index + GAME_X;
          south_east = index + GAME_X - 1;
          west = index - 1;
          north_west = index - GAME_X - 1;
          // Error check for boundary issue
          // Need to find a way to have no neighbor rather than set the index to
          // 0
          if (north < 0) {
            north = 0;
          }
          if (north_east < 0) {
            north_east = 0;
          }
          if (north_west < 0) {
            north_west = 0;
          }
          if (south > GAME_Y) {
            south = 0;
          }
          if (south_east > GAME_Y) {
            south_east = 0;
          }
          if (south_west > GAME_Y) {
            south_west = 0;
          }

          // Adjust count (value will either be a 1 or a 0)
          if (GAME_MATRIX[north] | GAME_MATRIX[north_west] | GAME_MATRIX[west] |
              GAME_MATRIX[south_west] | GAME_MATRIX[south] | GAME_MATRIX[east] |
              GAME_MATRIX[south_east] | GAME_MATRIX[north_east]) {
            live_count += 1;
          }
          // Check if cell should live or die
          if (live_count >= 4) {
            GAME_MATRIX[index] = true;
          } else {
            GAME_MATRIX[index] = false;
          }
        }
      }
    }
  }
  //-----------------------------------------------------
  // Close out the game
  free(GAME_MATRIX);
  return 0;
}
void SDL_AppQuit(void *appstate, SDL_AppResult result) {}
