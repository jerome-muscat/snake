import pygame
from fonctions import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("8-bit-fantasy-adventure-music_M4w9J7Kf.mp3")
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

score_rec = pygame.Rect((550,5), (72,30))
zone_rec = pygame.Surface(score_rec.size)
zone_rec.fill((255,20,147))
ecran.blit(zone_rec, (550,5))

police_principale = pygame.font.SysFont(roboto ,30)
score = police_principale.render ("score", 1 , blanc)
ecran.blit(score, (560,10))

# permet de créer une zone avec du texte qui contiendra le texte de la variable debut_partie.
debut_partie = police_principale.render ("Voulez-vous commencer une nouvelle partie ?", True , (0,0,150) )
ecran.blit(debut_partie, (125,80))

# permet de créer une zone cliquable nommée oui_rec, elle y contiendra le texte de la variable oui.
oui_rec = pygame.Rect((150,200), (30,20))
zone_rec = pygame.Surface(oui_rec.size)
zone_rec.fill(noir)
ecran.blit(zone_rec, (150,200))

oui = police_principale.render ("oui", 1 , (0,200,0) )
ecran.blit(oui, (150,200))

# permet de créer une zone cliquable nommée non_rec, elle y contiendra le texte de la variable non.
non_rec = pygame.Rect((450,200), (35,20))
zone_rec = pygame.Surface(non_rec.size)
zone_rec.fill(noir)
ecran.blit(zone_rec, (450,200))

non = police_principale.render ("non", 1 , (200,0,0) )
ecran.blit(non, (450,200))

# permet d'initialiser différente variable :
# nbr_erreur correspond aux erreurs utilisés pour l'affichage du pendu,
# compteur est une variable que j'ai utilisé pour activer/désactiver l'affichage/utilisation de fonctionnalités
##comme des zones de texte ou encore des zones cliquable...
compteur = 0
nom = ""

snake_position = [100, 50]

snake_corps = [[100, 50],
        [90, 50],
        [80, 50],
        [70, 50]
        ]

fruit_position = pomme()
apparition_fruit = True

direction = 'droite'
change_direction = direction

pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

jeu_deroule = None

score = 0
compteur = 0
jeu = True

pygame.display.flip()
while jeu:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and score_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                compteur = 0.5
                pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

                # permet de créer une zone cliquable nommée retour_debut, elle y contiendra le texte de la variable score. 
                retour_debut = pygame.Rect((10,5), (260,30))
                zone_rec = pygame.Surface(retour_debut.size)
                zone_rec.fill((255,20,147))
                ecran.blit(zone_rec, (10,5))

                score = police_principale.render ("retour à l'écran de début", 1 , blanc)
                ecran.blit(score, (20,10))
                
                # permet de créer du texte contenu dans les variables score_facile, scor_moyen et score_difficile.
                score_affichage = police_principale.render ("tableau des scores", 1 , (0,200,0) )
                ecran.blit(score_affichage, (50,100))
                
                # cette fonction permet d'afficher le tableau des scores
                affich_score(police_principale, ecran)

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle retour_debut et il est actif lorsque le compteur a pour valeur 0.5.
            if pygame.mouse.get_pressed()[0] and compteur == 0.5 and retour_debut.collidepoint(pygame.mouse.get_pos()):
                # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

                # ce bloque permet d'afficher la première page et de rénisialisé les différentes variables
                # au fonctionnement du jeu
                reinitialise = page_debut(ecran, police_principale, None)
                score = reinitialise[0]
                nom = reinitialise[1]
                compteur = reinitialise[2]       
                
            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle non_rec et il est actif lorsque le compteur a pour valeur 0. Si c'est le cas, le jeu s'arrete.
            if pygame.mouse.get_pressed()[0] and non_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                jeu = False
                # break

            # ce if permet de détecter un clique gauche avec pygame.mouse.get_pressed()[0] lorsqu'il se produit
            # sur le rectangle oui_rec et il est actif lorsque le compteur a pour valeur 0.
            if pygame.mouse.get_pressed()[0] and oui_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                compteur = 1
                jeu_deroule = None
                # pygame.draw.rect permet de dessiner un rectangle, ici il est blanc pour effacer les affichages précedents.
                pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

                # permet de créer et afficher le texte contenu dans les variables zone_ajout, description et description_suite.
                zone_ajout = police_principale.render ("Veuillez entrer votre nom ou pseudos ", 1 , blanc )
                ecran.blit(zone_ajout, (135,180))

                # permet de créer un bonton nommée valide_rec, ce dernier contiendra le texte de la variable valid.
                valid_rec = pygame.Rect((450,330), (80,30))
                valider_rec = pygame.Surface(valid_rec.size)
                valider_rec.fill((220,220,220))
                ecran.blit(valider_rec, (450,330))

                valid = police_principale.render ("Valider", 1 , blanc )
                ecran.blit(valid, (455,335))

            if pygame.mouse.get_pressed()[0] and compteur == 1 and valid_rec.collidepoint(pygame.mouse.get_pos()):
                compteur = 2
            
        
        if event.type == pygame.KEYDOWN and compteur == 1:
            nom += event.unicode

        if event.type == pygame.KEYDOWN and compteur == 2:
            if event.key == pygame.K_UP:
                change_direction = 'haut'
                

            if event.key == pygame.K_DOWN:
                change_direction = 'bas'

            if event.key == pygame.K_LEFT:
                change_direction = 'gauche'

            if event.key == pygame.K_RIGHT:
                change_direction = 'droite'

        if event.type == pygame.QUIT:
            jeu = False
    
    if compteur == 1:
        base_font = pygame.font.Font(None, 32)
        zone_saisie = pygame.Rect(225, 270, 200, 50)
        pygame.draw.rect(ecran, blanc, zone_saisie, 2)
        texte = base_font.render(nom, True, blanc)
        ecran.blit(texte, (zone_saisie.x+5, zone_saisie.y+5))
        pygame.display.flip()

    if compteur == 2:
        ecran.fill((0, 0, 0))
        if change_direction == 'haut' and direction != 'bas':
            direction = 'haut'

        if change_direction == 'bas' and direction != 'haut':
            direction = 'bas'

        if change_direction == 'gauche' and direction != 'droite':
            direction = 'gauche'

        if change_direction == 'droite' and direction != 'gauche':
            direction = 'droite'
        
        if direction == 'haut':
            snake_position[1] -= 10

        if direction == 'bas':
            snake_position[1] += 10

        if direction == 'gauche':
            snake_position[0] -= 10

        if direction == 'droite':
            snake_position[0] += 10
        
        snake_corps.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 1
            apparition_fruit = False
        else:
            snake_corps.pop()
        
        if not apparition_fruit:
            fruit_position = pomme()
            
        apparition_fruit = True
        ecran.fill((0,0,0))

        for pos in snake_corps:
            if pos == snake_corps[0]:
                pygame.draw.rect(ecran, (0,120,0),
                                pygame.Rect(pos[0], pos[1], 10, 10))
            else:
                pygame.draw.rect(ecran, (0,255,0),
                                pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(ecran, (255,0,0), pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > largeur_ecran-10:
            # perdu(score, ecran)
            jeu_deroule = nouveau_score(nom,score)
            reinitialise = page_debut(ecran, police_principale, score)
            score = reinitialise[0]
            nom = reinitialise[1]
            compteur = reinitialise[2]
            snake_position = reinitialise[3]
            snake_corps = reinitialise[4]
            fruit_position = reinitialise[5]

            apparition_fruit = True
            direction = 'droite'
            change_direction = direction            

        if snake_position[1] < 0 or snake_position[1] > hauteur_ecran-10:
            # perdu(score, ecran, police_principale)
            jeu_deroule = nouveau_score(nom,score)
            reinitialise = page_debut(ecran, police_principale, score)
            score = reinitialise[0]
            nom = reinitialise[1]
            compteur = reinitialise[2]
            snake_position = reinitialise[3]
            snake_corps = reinitialise[4]
            fruit_position = reinitialise[5]
            apparition_fruit = True
            direction = 'droite'
            change_direction = direction


        for block in snake_corps[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                # perdu(score, ecran, police_principale)
                jeu_deroule = nouveau_score(nom,score)
                reinitialise = page_debut(ecran, police_principale, score)
                score = reinitialise[0]
                nom = reinitialise[1]
                compteur = reinitialise[2]
                snake_position = reinitialise[3]
                snake_corps = reinitialise[4]
                fruit_position = reinitialise[5]

                apparition_fruit = True

                direction = 'droite'
                change_direction = direction

        if jeu_deroule == None:
            affich_score_jeu(ecran,score)

    pygame.display.update()
    pygame.time.Clock().tick(10)
    # pomme(ecran)
pygame.quit()