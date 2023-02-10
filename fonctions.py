import random, pygame

roboto = "Roboto-Regular.ttf"
largeur_ecran = 640
hauteur_ecran = 480
noir = (0, 0, 0)
blanc = (255, 255, 255)

def page_debut(ecran, police_principale, score):
    pygame.draw.rect(ecran, noir, pygame.Rect(0,0, 700, 700))

    if score != None:
        affich_score_jeu(ecran,score)
    score_rec = pygame.Rect((550,5), (72,30))
    zone_rec = pygame.Surface(score_rec.size)
    zone_rec.fill((255,20,147))
    ecran.blit(zone_rec, (550,5))

    score = police_principale.render("score", 1 , blanc)
    ecran.blit(score, (560,10))

    debut_partie = police_principale.render("Voulez-vous recommencer une nouvelle partie ?", True , (0,0,150) )
    ecran.blit(debut_partie, (125,80))
    
    oui = police_principale.render("oui", 1 , (0,200,0) )
    ecran.blit(oui, (150,200))

    non = police_principale.render("non", 1 , (200,0,0) )
    ecran.blit(non, (450,200))

    score = 0
    nom = ''
    compteur = 0

    snake_position = [100, 50]

    snake_corps = [[100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
            ]

    fruit_position = pomme()
    return score, nom, compteur, snake_position, snake_corps, fruit_position

def pomme():
    fruit_position = [random.randrange(1, (largeur_ecran//10)) * 10, random.randrange(1, (hauteur_ecran//10))*10]
    return fruit_position

def affich_score_jeu(ecran, score):
	score_font = pygame.font.SysFont(roboto, 30)
	score_surface = score_font.render(f"Score : {str(score)}", True,blanc)
	score_rect = score_surface.get_rect()
	ecran.blit(score_surface, score_rect)
	
def lecture_tableau_score():
    tableau_score = {}
    try:
        with open("scores.txt", "r") as f:
            for mot in f.readlines():
                ancien_nom, ancien_score = mot.split(":")
                ancien_score = ancien_score.strip()
                ancien_score = int(ancien_score)
                tableau_score[ancien_nom] = ancien_score
            return tableau_score
    except:
        return tableau_score

        
def nouveau_score(nom, score):
    tableau_score = lecture_tableau_score()
    ancien_score = recherche_score(nom)
    if ancien_score > score:
        score = ancien_score
    tableau_score[nom] = score
    try:
        with open("scores.txt", "w") as f:
            for nom, score in tableau_score.items():
                f.write(f"{nom}: {score}\n")
    except:
        print(f"Une erreur s'est produite lors de l'écriture du ancien_nom et du ancien_score dans le fichier scores.txt")
    return "Ca fonctionne"

def affich_score(police, ecran):
    tableau_score = lecture_tableau_score()
    
    with open("scores.txt", "r") as f:
        i = 130
        for ancien_nom, ancien_score in tableau_score.items():
            ancien_score = (f"{ancien_nom}: {ancien_score}")
            score_difficile = police.render (ancien_score, 1 , blanc)
            ecran.blit(score_difficile, (50, i))
            i+=30
                
def recherche_score(nom):
    tableau_score = lecture_tableau_score()
    
    with open("scores.txt", "r") as f:
        for ancien_nom, ancien_score in tableau_score.items():
            if nom == ancien_nom:
                return ancien_score
        return 0