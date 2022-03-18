import pygame  # necessaire pour charger les images et les sons
import random
import os 

class Joueur() : # classe pour crÃ©er le vaisseau du joueur
    def __init__(self) :
        self.sens=""
        self.image= pygame.image.load("vaisseau.png").convert_alpha()
        self.position = 400
        self.hauteur=540
        self.score = 0
        self.health=50
        self.max_health=50
        fichier = open("score.txt", "r")
        texte = fichier.read()
        self.max_score = int(texte)
    def marquer(self):
        self.score+=1 
        print("Score=", self.score)

    def deplacer(self):
        if self.sens == 'gauche' and self.position>0:
            self.position-=2 #premiere valeur pour la position
        elif self.sens== 'droite' and self.position<740:
            self.position += 2
    def update_health_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (0, 0, 0), [self.position+5, self.hauteur+35, self.max_health, 5])
        pygame.draw.rect(surface, (17, 242, 48), [self.position+5, self.hauteur+35, self.health, 5])
    def tirer(self):
        pass

class Balle():
    def __init__(self, joueur):
        self.etat=""
        self.image=pygame.image.load("unnamed.png").convert_alpha()
        self.depart = joueur.position+16
        self.hauteur = 1000
        self.joueur = joueur
    def bouger(self):
        if self.etat !='tiree':
            self.depart = self.joueur.position+23
        else:
            if self.hauteur>0:
                self.hauteur -= 30
            else : 
                self.etat=""
                self.depart = self.joueur.position+16
                self.hauteur = 800
    def toucher(self,ennemi):
        if -30< self.hauteur-ennemi.hauteur<30 and -30< self.depart -ennemi.depart<30:
            return True
        else :
            return False

class Ennemi():
    NbEnnemis = 10
    def __init__(self):
        self.depart =random.randint(50, 700)
        self.hauteur = 0
        self.image = pygame.image.load('invader1.png').convert_alpha()
        self.vitesse = random.randint(1,3)
        self.health=50
        self.max_health=50
    def avancer(self):
        self.hauteur+=self.vitesse
        if self.hauteur >= 850:
            self.hauteur = -50
            self.depart = random.randint(50,750)
    def disparaitre(self):
        self.depart = random.randint(20,100)
        self.hauteur = -100
    def damage(self, amount):
        #infliger les degats
        self.health -= amount
        #verifier si son nouveau nombre de point de vie est inferieur ou egale a 0
        if self.health <= 0:
            #reapparaitre
            self.depart = random.randint(50,750)
            self.vitesse = random.randint(1 ,3)
            self.health = self.max_health
    def toucher_joueur(self,joueur):
        if -30< self.hauteur-joueur.hauteur<30 and -30< self.depart - joueur.position<30:
            return True
        else:
            return False
    def update_health_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.depart + 5, self.hauteur - 13, self.max_health, 7])
        pygame.draw.rect(surface, (250, 32, 6), [self.depart + 5, self.hauteur - 13, self.health, 7])
 