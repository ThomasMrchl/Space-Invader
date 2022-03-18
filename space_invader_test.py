import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application
import random 
import os
import time

def game():
    # lancement des modules inclus dans pygame
    pygame.init() 

    white = (255, 255, 255)
    couleuror = (252, 252, 0)

    # création d'une fenêtre de 800 par 600
    screen = pygame.display.set_mode((800,600), pygame.NOFRAME)
    pygame.display.set_caption("Space Invaders")
    # chargement de l'image de fond
    fond = pygame.image.load('background.png').convert_alpha()
    #changement de la police d'ecriture
    font = pygame.font.Font('Deadly Advance.otf', 30)

    # creation du joueur
    player = space.Joueur()
    # creation de la balle
    tir=space.Balle(player)
    tir.etat="chargee"
    tirs = []
    # creation des ennemis
    listeEnnemis = []
    for indice in range(space.Ennemi.NbEnnemis):
        vaisseau = space.Ennemi()
        listeEnnemis.append(vaisseau)

    ### BOUCLE DE JEU  ###
    running = True # variable pour laisser la fenêtre ouverte
    jeu = False

    while running : # boucle infinie pour laisser la fenêtre ouverte
        # dessin du fond
        pygame.time.Clock().tick(150)
        screen.blit(fond,(0,0))
        #screen.blit(home_button,(15,15))
        meilleurscorejoueur = font.render(str(player.max_score), True, couleuror, None)
            
        scorejoueur = font.render(str(player.score), True, white, None)
        screen.blit(scorejoueur,(680,15))
        screen.blit(meilleurscorejoueur,(680,45))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement

            #gestion du clavier
            pygame.key.set_repeat(500,30)
            if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                    player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                    player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_SPACE : # espace pour tirer
                    player.tirer()
                    tir.etat = "tiree"


                
        
        ### Actualisation de la scene ###
        # Gestions des collisions
        for ennemi in listeEnnemis:
            ennemi.update_health_bar(screen)
            if tir.toucher(ennemi):
                ennemi.damage(10)
                player.marquer()
                #rajoute de la vie a chaque fois qu'un ennemi est tuer
                if player.health<=player.max_health:
                    player.health+=1
            if ennemi.toucher_joueur(player):
                player.health -= 1

        if player.score >= 50:
            player.image= pygame.image.load("vaisseau2.png").convert_alpha()
        # placement des objets
        # le joueur
        # appel de la fonction qui dessine le vaisseau du joueur
        player.deplacer()
        screen.blit(tir.image,[tir.depart,tir.hauteur])
        tir.bouger()
        screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur

            # les ennemis
        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur])

        player.update_health_bar(screen)

        if player.health==0:
            if player.score >= player.max_score:
                fichier = open('score.txt', 'w')
                fichier.write(str(player.score))
                fichier.close()
            running=False
            lost()

        pygame.display.update()


def menu():
    pygame.init() 

    white = (255, 255, 255)
    couleuror = (252, 252, 0)

    # création d'une fenêtre de 800 par 600
    screen = pygame.display.set_mode((800,600), pygame.NOFRAME)
    pygame.display.set_caption("Space Invaders")
    # chargement de l'image de fond
    fond = pygame.image.load('background2.png').convert_alpha()
    fond2 = pygame.image.load('background.png').convert_alpha()
    #changement de la police d'ecriture
    font = pygame.font.Font('Deadly Advance.otf', 30)

    listeEnnemis = []
    for indice in range(space.Ennemi.NbEnnemis):
        vaisseau = space.Ennemi()
        listeEnnemis.append(vaisseau)
        
    ### BOUCLE DE JEU  ###
    running = True # variable pour laisser la fenêtre ouverte

    while running : # boucle infinie pour laisser la fenêtre ouverte
        # dessin du fond
        screen.blit(fond2,(0,0))

        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur])
            ennemi.vitesse = random.randint(3,8)

        screen.blit(fond,(0,0))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement

            #gestion du clavier
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_TAB : # si une touche a été tapée KEYUP quand on relache la touche
                    running = False
                    game()
                    print('system')
                if event.key == pygame.K_RETURN :
                    running = False
                    rules()

        

        pygame.display.update()

def rules():
    pygame.init() 

    white = (255, 255, 255)
    couleuror = (252, 252, 0)

    # création d'une fenêtre de 800 par 600
    screen = pygame.display.set_mode((800,600), pygame.NOFRAME)
    pygame.display.set_caption("Space Invaders")
    # chargement de l'image de fond
    fond = pygame.image.load('background.png').convert_alpha()
    rulesgame = pygame.image.load('background3.png').convert_alpha()
    #changement de la police d'ecriture
    font = pygame.font.Font('Deadly Advance.otf', 30)

    listeEnnemis = []
    for indice in range(space.Ennemi.NbEnnemis):
        vaisseau = space.Ennemi()
        listeEnnemis.append(vaisseau)

        
    ### BOUCLE DE JEU  ###
    running = True # variable pour laisser la fenêtre ouverte

    while running : # boucle infinie pour laisser la fenêtre ouverte
        # dessin du fond
        screen.blit(fond,(0,0))

        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur])
            ennemi.vitesse = random.randint(3,8)

        screen.blit(rulesgame,(0,0))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement

            #gestion du clavier
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_TAB : # si une touche a été tapée KEYUP quand on relache la touche
                    running = False
                    menu()
        pygame.display.update()

def lost():
    pygame.init() 

    white = (255, 255, 255)
    couleuror = (252, 252, 0)

    # création d'une fenêtre de 800 par 600
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Space Invaders")
    # chargement de l'image de fond
    fond = pygame.image.load('background.png').convert_alpha()
    fond3 = pygame.image.load('background4.png').convert_alpha()
    #changement de la police d'ecriture
    font = pygame.font.Font('Deadly Advance.otf', 30)

    listeEnnemis = []
    for indice in range(space.Ennemi.NbEnnemis):
        vaisseau = space.Ennemi()
        listeEnnemis.append(vaisseau)

        
    ### BOUCLE DE JEU  ###
    running = True # variable pour laisser la fenêtre ouverte

    while running : # boucle infinie pour laisser la fenêtre ouverte
        # dessin du fond
        screen.blit(fond,(0,0))

        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur])
            ennemi.vitesse = random.randint(3,8)

        screen.blit(fond3,(0,0))

        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement

            #gestion du clavier
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_TAB : # si une touche a été tapée KEYUP quand on relache la touche
                    running = False
                    menu()
                if event.key == pygame.K_RETURN :
                    running = False
                    rules()
        pygame.display.update()

menu()