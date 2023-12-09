import pygame
import sys
from pygame.locals import *
from ia import ia

def choisir_mode_de_jeu():
    pygame.init()

    # Fenêtre qui permet de choisir le mode de jeu
    ecran = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Choisissez le mode de jeu')
    police_titre = pygame.font.Font("pacman.TTF", 80)
    fond_ecran = pygame.image.load("image fond menu/menu-fond.jpg")
    fonte_titre = pygame.font.SysFont(None, 80)
    police_texte_joueur = pygame.font.Font("Pokemon_Solid.TTF", 30)
    fonte = pygame.font.SysFont(None, 40)
    horloge = pygame.time.Clock()

    # Couleurs
    blanc = (255, 255, 255)
    gris_clair = (200, 200, 200)
    gris_fonce = (150, 150, 150)
    noir = (0, 0, 0)
    couleur_texte = noir

    while True:
        ecran.blit(fond_ecran, (0, 0))
        titre = police_titre.render('Tic-Tac-Toe', True, gris_fonce)
        
        ombre_titre = police_titre.render('Tic-Tac-Toe', True, (0, 0, 0))
        ecran.blit(ombre_titre, (ecran.get_width() // 2 - ombre_titre.get_width() // 2 + 4, 54))

        # Affichage du titre principal
        ecran.blit(titre, (ecran.get_width() // 2 - titre.get_width() // 2, 50))

        pygame.draw.rect(ecran, gris_clair, (350, 300, 350, 50), border_radius=10)
        pygame.draw.rect(ecran, gris_clair, (350, 410, 350, 50), border_radius=10)

        pos = pygame.mouse.get_pos()

        # Bouton "Joueur contre Joueur"
        if 350 <= pos[0] <= 650 and 300 <= pos[1] <= 400:
            pygame.draw.rect(ecran, gris_fonce, (350, 300, 350, 50), border_radius=10)
            couleur_texte = blanc
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                return 1
        else:
            couleur_texte = noir

        texte_joueur = police_texte_joueur.render('Joueur contre Joueur', True, couleur_texte)
        ecran.blit(texte_joueur, (355, 310))

        # Bouton "Joueur contre IA"
        if 350 <= pos[0] <= 650 and 410 <= pos[1] <= 460:
            pygame.draw.rect(ecran, gris_fonce, (350, 410, 350, 50), border_radius=10)
            couleur_texte = blanc
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                return 2
        else:
            couleur_texte = noir

        texte_ia = police_texte_joueur.render('Joueur contre IA', True, couleur_texte)
        ecran.blit(texte_ia, (385, 420))

        pygame.display.flip()

        # Quitter Pygame
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                return None

        horloge.tick(60)


def choisir_niveau_ia():
    pygame.init()

    # Fenêtre qui permet de choisir le niveau de l'IA
    ecran_niveau = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Choisissez le niveau de l\'IA')
    fond_ecran = pygame.image.load("image fond menu/niveau.jpg")
    
    police_titre = pygame.font.Font("pacman.TTF", 80)
    police_niveau = pygame.font.Font("Pokemon_Solid.TTF", 40)
    horloge = pygame.time.Clock()

    niveau_choisi = None

    while True:
        ecran_niveau.blit(fond_ecran, (0, 0))

        # Afficher le titre "Tic-Tac-Toe" en haut de la fenêtre
        titre_surface = police_titre.render('Tic-Tac-Toe', True, (200, 200, 200))
        ombre_titre = police_titre.render('Tic-Tac-Toe', True, (30, 30, 30))
        ecran_niveau.blit(ombre_titre, (ecran_niveau.get_width() // 2 - ombre_titre.get_width() // 2 + 4, 35))
        titre_rect = titre_surface.get_rect(center=(ecran_niveau.get_width() // 2, 70))
        ecran_niveau.blit(titre_surface, titre_rect.topleft)

        # Calcul de la position verticale au milieu
        hauteur_fenetre = ecran_niveau.get_height()
        milieu_vertical = hauteur_fenetre // 2

        # Affichage des options pour choisir le niveau de l'IA
        texte_facile = police_niveau.render('Facile', True, (0, 0, 0))
        texte_moyen = police_niveau.render('Moyen', True, (0, 0, 0))
        texte_difficile = police_niveau.render('Difficile', True, (0, 0, 0))

        hauteur_texte = texte_facile.get_height()
        espace_entre_options = 20

        rect_facile = pygame.Rect(350, 300, 350, 50)
        rect_moyen = pygame.Rect(350, 410, 350, 50)
        rect_difficile = pygame.Rect(350, 520, 350, 50)

        # Vérifie si la souris est sur l'une des options
        souris_sur_facile = rect_facile.collidepoint(pygame.mouse.get_pos())
        souris_sur_moyen = rect_moyen.collidepoint(pygame.mouse.get_pos())
        souris_sur_difficile = rect_difficile.collidepoint(pygame.mouse.get_pos())

        # Dessine les rectangles en fonction de la position de la souris
        pygame.draw.rect(ecran_niveau, (150, 150, 150) if not souris_sur_facile else (50, 50, 50), rect_facile, border_radius=10)
        pygame.draw.rect(ecran_niveau, (150, 150, 150) if not souris_sur_moyen else (50, 50, 50), rect_moyen, border_radius=10)
        pygame.draw.rect(ecran_niveau, (150, 150, 150) if not souris_sur_difficile else (50, 50, 50), rect_difficile, border_radius=10)

        # Dessine le texte en fonction de la position de la souris
        couleur_texte_facile = (255, 255, 255) if souris_sur_facile else (0, 0, 0)
        couleur_texte_moyen = (255, 255, 255) if souris_sur_moyen else (0, 0, 0)
        couleur_texte_difficile = (255, 255, 255) if souris_sur_difficile else (0, 0, 0)

        texte_surface_facile = police_niveau.render('Facile', True, couleur_texte_facile)
        texte_surface_moyen = police_niveau.render('Moyen', True, couleur_texte_moyen)
        texte_surface_difficile = police_niveau.render('Difficile', True, couleur_texte_difficile)

        ecran_niveau.blit(texte_surface_facile, (rect_facile.centerx - texte_surface_facile.get_width() // 2, rect_facile.centery - texte_surface_facile.get_height() // 2))
        ecran_niveau.blit(texte_surface_moyen, (rect_moyen.centerx - texte_surface_moyen.get_width() // 2, rect_moyen.centery - texte_surface_moyen.get_height() // 2))
        ecran_niveau.blit(texte_surface_difficile, (rect_difficile.centerx - texte_surface_difficile.get_width() // 2, rect_difficile.centery - texte_surface_difficile.get_height() // 2))

        pygame.display.flip()

        # Quitter Pygame
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Clique Souris
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_facile.collidepoint(pos):
                    niveau_choisi = "facile"
                    pygame.quit()
                    return niveau_choisi
                elif rect_moyen.collidepoint(pos):
                    niveau_choisi = "moyen"
                    pygame.quit()
                    return niveau_choisi
                elif rect_difficile.collidepoint(pos):
                    niveau_choisi = "difficile"
                    pygame.quit()
                    return niveau_choisi

        pygame.display.flip()

        horloge.tick(60)

# Défini le niveau de difficulté
niveau_difficulte = "difficile"
mode_jeu = choisir_mode_de_jeu()

if mode_jeu is not None:
    if mode_jeu == 2:
        niveau_ia = choisir_niveau_ia()
        if niveau_ia is not None:
            niveau_difficulte = niveau_ia

    pygame.init()

    hauteur_ecran = 300
    largeur_ecran = 300
    largeur_ligne = 6
    ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
    pygame.display.set_caption('Tic-Tac-Toe')

    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    bleu = (0, 0, 255)
    fonte = pygame.font.SysFont(None, 40)
    clique = False
    joueur = 1
    marques = [[0] * 3 for _ in range(3)]
    fin_partie = False
    vainqueur = 0
    zone_rejouer = Rect(largeur_ecran // 2 - 80, hauteur_ecran // 2, 160, 50)

# Dessine le plateau sur le quel les pionts vont etre posé
    def dessiner_plateau():
        ecran.fill((255, 255, 210))
        grille = (50, 50, 50)
        for x in range(1, 3):
            pygame.draw.line(ecran, grille, (0, 100 * x), (largeur_ecran, 100 * x), largeur_ligne)
            pygame.draw.line(ecran, grille, (100 * x, 0), (100 * x, hauteur_ecran), largeur_ligne)

# Dssine les lignes sur le plateau pour le jeu
    def dessiner_marques():
        for x, ligne in enumerate(marques):
            for y, valeur in enumerate(ligne):
                if valeur == 1:
                    pygame.draw.line(ecran, rouge, (x * 100 + 15, y * 100 + 15), (x * 100 + 85, y * 100 + 85), largeur_ligne)
                    pygame.draw.line(ecran, rouge, (x * 100 + 85, y * 100 + 15), (x * 100 + 15, y * 100 + 85), largeur_ligne)
                elif valeur == -1:
                    pygame.draw.circle(ecran, vert, (x * 100 + 50, y * 100 + 50), 38, largeur_ligne)

# vérifie si la partie est bien fini
    def verifier_fin_partie():
        global fin_partie, vainqueur
        for x in range(3):
            if sum(marques[x]) == 3 or marques[0][x] + marques[1][x] + marques[2][x] == 3:
                vainqueur, fin_partie = 1, True
            elif sum(marques[x]) == -3 or marques[0][x] + marques[1][x] + marques[2][x] == -3:
                vainqueur, fin_partie = 2, True
        if marques[0][0] + marques[1][1] + marques[2][2] == 3 or marques[2][0] + marques[1][1] + marques[0][2] == 3:
            vainqueur, fin_partie = 1, True
        elif marques[0][0] + marques[1][1] + marques[2][2] == -3 or marques[2][0] + marques[1][1] + marques[0][2] == -3:
            vainqueur, fin_partie = 2, True
        if not any(0 in ligne for ligne in marques):
            vainqueur, fin_partie = 0, True

# Demande à la fin de la partie le status de ces stats (gagné, match nul, etc...), + rejouer
    def dessiner_fin_partie():
        texte_fin = f"Joueur {vainqueur} Gagné" if vainqueur != 0 else "Partie NUL"
        img_fin = fonte.render(texte_fin, True, bleu)
        pygame.draw.rect(ecran, vert, (largeur_ecran // 2 - 100, hauteur_ecran // 2 - 60, 200, 50))
        ecran.blit(img_fin, (largeur_ecran // 2 - 100, hauteur_ecran // 2 - 50))
        texte_rejouer = 'Rejouer ?'
        img_rejouer = fonte.render(texte_rejouer, True, bleu)
        pygame.draw.rect(ecran, vert, zone_rejouer)
        ecran.blit(img_rejouer, (largeur_ecran // 2 - 80, hauteur_ecran // 2 + 10))

    en_cours = True
    while en_cours:
        dessiner_plateau()
        dessiner_marques()

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN and not fin_partie:
                pos = pygame.mouse.get_pos()
                cellule_x, cellule_y = pos[0] // 100, pos[1] // 100
                if 0 <= cellule_x < 3 and 0 <= cellule_y < 3 and marques[cellule_x][cellule_y] == 0:
                    marques[cellule_x][cellule_y] = joueur
                    joueur *= -1
                    verifier_fin_partie()
            elif evenement.type == pygame.MOUSEBUTTONUP and fin_partie:
                pos = pygame.mouse.get_pos()
                if zone_rejouer.collidepoint(pos):
                    fin_partie, joueur, marques, vainqueur = False, 1, [[0] * 3 for _ in range(3)], 0

        if mode_jeu == 2 and not fin_partie and joueur == -1:
            if niveau_difficulte is not None:
                mouvement_ia = ia(marques, -1, niveau_difficulte)
                if mouvement_ia is not None and marques[mouvement_ia // 3][mouvement_ia % 3] == 0:
                    marques[mouvement_ia // 3][mouvement_ia % 3] = joueur
                    joueur *= -1
                    verifier_fin_partie()

        if fin_partie:
            dessiner_fin_partie()

        pygame.display.update()

    pygame.quit()