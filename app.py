from phrasehunter.game import Game

if __name__ == '__main__':
    try:
        game = Game()
        game.start()
        
    except EOFError:
        print('\nSee you Next Time!')
       
    except KeyboardInterrupt:
        print('\nSee you Next Time!')
        quit()
        
