#define SDL_MAIN_USE_CALLBACKS 1
#include <stdio.h>
#include <SDL2/SDL.h>


int main(int argc, char *argv[]){

        //Initialize Variables
        const SDL_VideoInfo* info = NULL;
        SDL_Surface *SCREEN;
        int DX = 1920;
        int DY = 1080;
        int PixelDepth = 3;
        int Flags = 0;
        
        printf("Initializing SDL ... \n");
        //error check if the video was initialized
        if (SDL_Init(SDL_INIT_VIDEO) == -1){
            printf("Failed to initialize \n", SDL_GetError());
            exit(-1);
        }
        printf("SDL Initialized \n");

        //Get SDL_OpenGl info and initialize
        info =SDL_GetVideoInfo(SDL_GL_RED_SIZE, 1);
        SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 1);
        SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 1);
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 3);
        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 0);

        //Request initial window
        Flags = SDL_OPENGL | SDL_FULLSCREEN;

        //Set up the screen 
        SCREEN = SDL_SetVideoMode(DX, DY, PixelDepth, Flags);
        //Check that screen was initialized
        if (SCREEN == NULL) {
            printf(stderr, "Screen could not be initialized \n", SDL_GetError());
            exit(1);
        }

        //Quit SDL Before program close
        SDL_Quit();
        printf("Program out\n");

        return 0;

}