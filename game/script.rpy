# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define g = Character(_("Gardien de musée"), color="#FF0000")
define m = Character(_("Moi"), color="002BFF")



# Le jeu commence ici
label start:
    scene black

    stop music fadeout 1.0

    "Vous vous réveillez lentement"

    scene room
    with fade

    "..."

    m "Aujourd’hui j’ai ma journée libre."

    m "YOUPI !!!"

    # Musique d'ambiance bossa commence
    play music "audio/bossa.opus"

    menu:

        m "Et si j’allais au musée ? il y a des expositions intéressantes en ce moment"

        "Oui.":
            m "Je me prépare pour y aller !"
            scene black
            with fade
            jump gomusee

        "Dormir encore un peu.":

            jump start

    return

label gomusee:
    "Vous arrivez devant le musée."

    scene ext
    with fade

    "Il n'y a pas beaucoup d'agitation aujourd'hui…"

    "Vous rentrez."

    scene hall
    with fade

    "Vous vous dirigez vers le gardien de musée qui se trouve dans le hall."

    #faire apparaitre le gardien
    show gardien
    with dissolve

    m "Bonjour, que se passe-t-il ?"

    show gardien choque
    g "Bonjour, une œuvre a disparu !!!"
    m "Oh non ! laquelle ?"

    show gardien triste
    g "Le taureau des Alpes d’Eugène Burnand."

    show taur
    with dissolve

    m "Mais comment allez-vous faire pour la retrouver ?"
    hide taur
    with dissolve

    show gardien
    with dissolve
    g "C’est bien cela la question… Le voleur a laissé un mot, regardez:"
    "Vous lisez le mot suivant:"
    "« Pour retrouver l’œuvre il faudra répondre à mes énigmes artistiques. Veuillez vous rendre au premier étage de la collection pour la première devinette »"
    m "Hmm... Je vois."
    show gardien triste
    g "Nous craignons que cela soit un piège pour nous distraire d’avantage voyez-vous."
    m "Je pourrais essayer de jouer à son jeu…"
    show gardien smile

    g "Vraiment vous seriez d’accord ?"

    menu:
        g "Les questions porteront sans-doute sur l’art. Vous sentez-vous à l’aise avec cela ?"

        "Oui, je suis étudiante en histoire de l'art.":
            jump quizzmusee
        "Non finalement cela ne m’intéresse pas.":
            jump mauvaisefinun


    return

label quizzmusee:
    m "Oui, je suis étudiante en histoire de l’art. Je pense que cela peut être à ma portée." 
    g "Génial! Je vous aiderai dans cette enquête." 
    m "Alors allons-y !"

    scene black
    with fade
    "Vous montez au premier étage afin de trouver la première devinette."

    scene salle
    with fade
    
    "L’étudiante voit un bout de papier près d’une petite sculpture de Rodin. Elle le ramasse et l’ouvre"

    show papier
    with dissolve

    "Le papier affichait le texte suivant:" 

    hide papier
    with dissolve

    menu:
        "« Première énigme artistique ; dans mes peintures j’utilise essentiellement du noir. qui suis-je ? »"

        "A. Soulages":
            jump quizzmuseedeux
        "B. Derain":
            jump mauvaisefindeux

    return

label quizzmuseedeux:
    m "Je pense que c’est Pierre Soulages."

    show gardien
    with dissolve

    g "Ah ! Je pense savoir où nous rendre dans ce cas..."
    g "Pierre Soulages est exposé au deuxième étage !"
    m "Alors c'est forcément là-bas! Allons-y!"

    hide gardien
    with dissolve

    scene black
    with fade

    "Les deux se rendent à la dernière salle de la collection au deuxième étage"

    scene salle2
    with fade

    show gardien choque
    with dissolve

    g "Un morceau de papier !"

    hide gardien choque
    with dissolve

    "Le gardien lève la tête et observe le tableau en face de lui"

    show enig1 at top
    with dissolve

    "Wow !"

    hide enig1
    with dissolve

    show gardien
    with dissolve

    g "Mais oui c’est bien une œuvre de Pierre Soulages elle s’appelle « peinture », et a été réalisé en 1956 ! C’est une donation de la collectionneuse d’art Alice Pauli."
    m "Génial ! Cette œuvre démontre le talent de l’artiste à jouer avec les nuances de couleurs sombres et les texture. Qu’est-ce qui est noté sur le papier ?"
    g "Euh oui alors…"

    hide gardien
    with dissolve

    menu:
        "si vous vous trouvez ici c’est que vous avez deviné. Voici la deuxième énigme : Je suis une œuvre pouvant être rattachée à l’Art Nouveau par la technique utilisée. Aussi, la scène représentée peut faire référence au mythe de Narcisse. Je suis…"
        "A. L’eau mystérieuse d’Ernest Biéler":
            m "L’eau mystérieuse !"
            m "Son style, le graphisme et la technique de la détrempe à l'oeuf en font une oeuvre digne de l'Art nouveau !"
            show gardien smile
            with dissolve
            g "Je pense aussi! Elle se trouve au premier étage. Elle a un très grand format de 146,3 x 376,4 cm ! Elle ne peut passer inaperçue."
            m "Allons-y !"
            jump quizzmuseetrois
        "B. L’Apparition d’un visage nimbé dans le ciel au-dessus de Paris d’ Eugène Grasset":
            jump mauvaisefintrois

    return


label quizzmuseetrois:
 
    scene black
    with fade
    "Les deux descendent à l’étage inférieur et vont dans la salle numéro deux."

    scene salle
    with fade

    show myst at top
    with dissolve

    m "Wow! En effet, l’œuvre est très grande et son cadre doré est impressionnant !"

    hide myst
    with dissolve
    
    show gardien
    with dissolve
    g "Effectivement ! De plus, il est important de noter que c’est le cadre d’origine. Approchons-nous."

    hide gardien
    with dissolve

    show papier
    with dissolve

    m "Voilà encore un message !" 
    
    "Vous lisez le contenu du papier."

    hide papier
    with dissolve

    "« Bravo ! Voici la dernière énigme qui vous permettra de retrouver l’œuvre égarée… »"

    "«... le motif de l'oeuvre en question est omniprésent dans le travail de cet artiste que l'on rattache à l'Arte Povera, mouvement naissant en Italie à la suite de la Deuxième Guerre mondiale. »"

    menu:
        "Cette œuvre fait partie intégrante du musée. Faite d’ombre et de lumière, elle en fait la parfaite carte de visite. Qui est-elle ?"
        "A. A occhi chiusi de Giuseppe Penone":
            m "Hmm... je réponds les yeux fermés c'est Occhi Chiusi de Giuseppe Penone."
            show gardien
            with dissolve
            g "..."
            g "Je commence à avoir des doutes."
            m "Comment cela ?"
            show gardien triste
            g "Vous m'aviez dit que vous étiez une étudiante en art."
            g "Et pourtant... une question si simple."
            g "Je commence à penser que c'est vous qui avez volé cette toile !"
            m "Mais! Comment osez-vous ?"
            jump mauvaisefinquatre
        "B. Luce e Ombre de Giuseppe Penone":
            m "Hmm... le motif en question, si nous parlons de Penone, est sûrement lié à la nature et donc l’arbre serait adéquat."
            m "De plus le contraste des matériaux utilisés, le bronze, l’or et le granite font penser à cette idée d’ombre et de lumière évoquée dans le titre."
            show gardien
            with dissolve
            g "Vous pensez qu’il s’agit de l’œuvre dans le hall ? Cela serait presque trop simple…"
            m "Allons vérifier !"
            jump quizzmuseequatre
    return

label quizzmuseequatre:
    scene black
    with fade
    "Les deux se rendent dans le hall."

    scene hall
    with fade

    "L’étudiante se rapproche de l’œuvre en forme d’arbre."

    show gardien
    with dissolve

    g "L'arbre de Giuseppe Penone est impressionnant de par sa taille. En effet, il fait 14m. de haut. Cela a été compliqué de l'installer dans le musée. "


    "L'étudiante, peu attentive à ce que dit le gardien, apperçoit quelque chose de brillant entre les racines…"
    
    hide gardien
    with dissolve

    show cle at top
    with dissolve

    m "Mais c'est une clé ?!"

    hide cle
    with dissolve

    show gardien choque
    with dissolve

    g "Nous avons vraiment réussi !? Laissez-moi observer la clé."

    "Le gardien prend la clé dans ses mains."

    g "Je crois que c’est celle qui donne accès à l’auditorium."

    hide gardien choque
    with dissolve

    scene black
    with fade

    "Les deux se rendent à l'auditorium."

    scene auditorium
    with fade

    show gardien triste
    with dissolve

    g "Il n’y a pas de Taureau des Alpes à l’horizon…"
    m "Oui ! Regardez !"

    "L’étudiante tire le rideau..."

    show taur at top
    with dissolve

    "Le tableau était caché derrière !"

    hide taur
    with dissolve

    show gardien smile
    with dissolve

    g "Génial ! je dois en informer mes responsables !"

    hide gardien
    with dissolve

    scene sallefin
    with fade

    "La sécurité ainsi que l’équipe de conservation du musée se sont chargées de remettre l’œuvre dans la salle."

    "GÉNIAL !"

    show gardien choque
    with dissolve

    g "Regardez ! J'ai trouvé un énième papier dissimulé derrière la toile. Il est tombé pendant l'accrochage."

    "Le gardien vous tend le message pour que vous découvriez son contenu."

    hide gardien choque
    with dissolve

    "Le message est le suivant:"

    "« Vous êtes des adversaires redoutables... »"

    "« ...Mais ne vous reposez pas sur vos lauriers... »"

    "« ...JE REVIENDRAI ! »"

    scene black
    with fade

    stop music fadeout 1.0

    "Vous rentrez chez vous après une journée riche en émotions."

    "BONNE FIN ! Merci d'avoir joué !"

    return

label mauvaisefinquatre:
    scene black
    with fade

    stop music fadeout 1.0

    "Le gardien convaincu que vous êtes le voleur appelle la sécurité."
    "Vous finissez votre journée au commissariat."
    "MAUVAISE FIN."
    "GAME OVER !"
    return

label mauvaisefintrois:
    scene black
    with fade

    stop music fadeout 1.0
    "En entendant la mauvaise réponse, le voleur s'approche de vous discrètement..."
    "...et vous assomme !"

    scene ext
    with fade

    "..."

    m "J'ai mal à la tête !"

    show gardien triste
    with dissolve

    g "Heureusement, vous revenez à vous !"

    m "Que s'est-il passé ?"

    g "En entendant la mauvaise réponse, un homme a surgit pour vous donner un coup sur la tête."

    g "C'était le voleur. Il est reparti avec la toile..."

    hide gardien triste
    with dissolve

    scene black
    with fade

    "Cette journée aura été un calvaire !"
    "MAUVAISE FIN !!!"
    "GAMEOVER"
    return

label mauvaisefindeux:
    scene black
    with fade

    stop music fadeout 1.0
    "En entendant la mauvaise réponse, le voleur surgit derrière vous..."
    "...et vous assomme"

    scene room
    with fade

    "..."

    m "Mais... c'était un cauchemars ?!"
    "MAUVAISE FIN !!!"
    "GAMEOVER"
    return

label mauvaisefinun:
    scene black
    with fade

    stop music fadeout 1.0
    "Vous rentrez chez vous, triste de ne pas avoir pu aider le gardien..."
    "MAUVAISE FIN !!!"
    "GAMEOVER"
    return
