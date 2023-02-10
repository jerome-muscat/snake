import pygame
from fonctions import *
from ia import ia

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

debut_partie = police_principale.render ("Voulez-vous commencer une nouvelle partie ?", True , (0,0,150) )
ecran.blit(debut_partie, (125,80))

oui_rec = pygame.Rect((150,200), (30,20))
zone_rec = pygame.Surface(oui_rec.size)
zone_rec.fill(noir)
ecran.blit(zone_rec, (150,200))

oui = police_principale.render ("oui", 1 , (0,200,0) )
ecran.blit(oui, (150,200))

non_rec = pygame.Rect((450,200), (35,20))
zone_rec = pygame.Surface(non_rec.size)
zone_rec.fill(noir)
ecran.blit(zone_rec, (450,200))

non = police_principale.render ("non", 1 , (200,0,0) )
ecran.blit(non, (450,200))

compteur = 0
nom = ""

snake_position = [150, 100]

snake_corps = [[150, 100],
        [140, 100],
        [130, 100],
        [120, 100]
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
                compteur = 1
                pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

                retour_debut = pygame.Rect((10,5), (260,30))
                zone_rec = pygame.Surface(retour_debut.size)
                zone_rec.fill((255,20,147))
                ecran.blit(zone_rec, (10,5))

                score = police_principale.render ("retour à l'écran de début", 1 , blanc)
                ecran.blit(score, (20,10))
                
                score_affichage = police_principale.render ("tableau des scores", 1 , (0,200,0) )
                ecran.blit(score_affichage, (50,100))
                
                affich_score(police_principale, ecran)

            if pygame.mouse.get_pressed()[0] and compteur == 1 and retour_debut.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

                reinitialise = page_debut(ecran, police_principale, None)
                score = reinitialise[0]
                nom = reinitialise[1]
                compteur = reinitialise[2]       

            if pygame.mouse.get_pressed()[0] and non_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                jeu = False

            if pygame.mouse.get_pressed()[0] and oui_rec.collidepoint(pygame.mouse.get_pos()) and compteur == 0:
                compteur = 2 
                pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

                zone_ajout = police_principale.render ("Voulez-vous laisser l'ia joueur à votre place ? ", 1 , blanc )
                ecran.blit(zone_ajout, (135,80))

                ia_rec = pygame.Rect((150,150), (30,20))
                zone_rec = pygame.Surface(ia_rec.size)
                zone_rec.fill(noir)
                ecran.blit(zone_rec, (150,150))

                oui = police_principale.render ("oui", 1 , (0,200,0) )
                ecran.blit(oui, (150,150))

                non_ia_rec = pygame.Rect((450,150), (35,20))
                zone_rec = pygame.Surface(non_ia_rec.size)
                zone_rec.fill(noir)
                ecran.blit(zone_rec, (450,150))

                non = police_principale.render ("non", 1 , (200,0,0) )
                ecran.blit(non, (450,150))
            
            if pygame.mouse.get_pressed()[0] and compteur == 2 and ia_rec.collidepoint(pygame.mouse.get_pos()):
                nom = 'ia'
                jeu_deroule = None
                compteur = 4

            if pygame.mouse.get_pressed()[0] and compteur == 2 and non_ia_rec.collidepoint(pygame.mouse.get_pos()):
                compteur = 3
                jeu_deroule = None

                pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

                zone_ajout = police_principale.render ("Veuillez entrer votre nom ou pseudos ", 1 , blanc )
                ecran.blit(zone_ajout, (135,180))

                valid_rec = pygame.Rect((450,330), (80,30))
                valider_rec = pygame.Surface(valid_rec.size)
                valider_rec.fill((220,220,220))
                ecran.blit(valider_rec, (450,330))

                valid = police_principale.render ("Valider", 1 , blanc )
                ecran.blit(valid, (455,335))

            if pygame.mouse.get_pressed()[0] and compteur == 3 and valid_rec.collidepoint(pygame.mouse.get_pos()):
                compteur = 4
            
        if event.type == pygame.KEYDOWN and compteur == 3:
            nom += event.unicode

        if event.type == pygame.KEYDOWN and compteur == 4 and nom != "ia":
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
    
    if compteur == 3:
        base_font = pygame.font.Font(None, 32)
        zone_saisie = pygame.Rect(225, 270, 200, 50)
        pygame.draw.rect(ecran, blanc, zone_saisie, 2)
        texte = base_font.render(nom, True, blanc)
        ecran.blit(texte, (zone_saisie.x+5, zone_saisie.y+5))
        pygame.display.flip()

    if compteur == 4:
        ecran.fill((0, 0, 0))

        if nom == "ia":
            direction = ia(snake_corps, fruit_position, snake_position, change_direction, direction)
        else : 
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
            while fruit_position in snake_corps:
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
    pygame.time.Clock().tick(13)
pygame.quit()