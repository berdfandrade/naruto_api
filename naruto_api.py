
import random

frases_naruto = {
    "Naruto Uzumaki": [
        "Eu nunca desisto! Meu nome é Naruto Uzumaki!",
        "Eu vou me tornar o Hokage, acredite!",
        "Eu não vou voltar atrás, eu nunca desisto!",
        "Eu sou um ninja que quebra as regras, mas eu nunca quebro os laços de amizade!",
        "Não importa o quão difícil seja o desafio, eu vou enfrentá-lo de frente!",
        "Eu não sou um monstro... Eu sou um ninja!",
        "Você sabe qual é a coisa mais importante para um shinobi? É nunca desistir de seus sonhos!",
        "Mesmo que eu tenha que arrastar meu corpo ferido, ainda vou me tornar o Hokage!",
        "Eu posso ficar forte se eu for seu amigo!",
        "O verdadeiro poder não vem de técnicas especiais, mas da força de vontade!",
        "Eu sou especial, eu sempre tive sonhos!",
        "Eu odeio as palavras 'darling' e 'bondade'! O que eu quero é poder!"
    ],
    "Sasuke Uchiha": [
        "Eu caminharei pelo caminho das trevas para proteger minha vila!",
        "Um dia eu vou me vingar... Não importa o que aconteça!",
        "Eu vou provar que sou mais forte do que qualquer um!",
        "A fraqueza é um pecado. Eu nunca vou admitir a derrota!",
        "Não importa o quão longe eu caia na escuridão, eu sempre vou encontrar o meu caminho de volta!",
        "Não se preocupe, eu vou matá-lo rápido.",
        "Eu não me importo com os sonhos dos outros. Eu vou destruir a minha aldeia e matar meu irmão!",
        "Eu vou fazer você sentir a dor que eu senti!",
        "A vingança é o único caminho para mim.",
        "O amor é um fardo. Quanto mais você ama alguém, mais fraco você se torna.",
        "Eu sou um gênio! Eu não sou inútil como você!",
        "Aqueles que não entendem a verdadeira dor nunca poderão entender a verdadeira paz."
    ],
    "Kakashi Hatake": [
        "Aqueles que quebram as regras são chamados de escória, mas aqueles que abandonam seus amigos são piores do que a escória.",
        "A verdadeira medida de um shinobi está na forma como ele vive e morre, não nas suas realizações.",
        "O trabalho em equipe é fundamental para ser um shinobi de sucesso.",
        "Um shinobi deve ver por trás da aparência e ler as entrelinhas.",
        "Aqueles que não entendem o verdadeiro significado do trabalho em equipe estão fadados ao fracasso.",
        "Desculpe, eu cheguei atrasado porque perdi meu caminho, de novo.",
        "Copiar meu Sharingan é impossível, não importa o quão talentoso você seja!",
        "Eu estou lendo um livro.",
        "Um ninja nunca mostra suas verdadeiras cores.",
        "Aqueles que abandonam a missão são piores do que a escória.",
        "Como um ninja, você sempre deve acreditar em suas próprias palavras.",
        "Eu sou Kakashi Hatake. O Ninja da Folha que lê livros de sexo."
    ],
    "Sakura Haruno": [
        "Eu vou me tornar uma ninja forte e proteger meus amigos!",
        "Eu não sou mais uma garotinha indefesa!",
        "Eu não sou fraca! Eu vou provar a todos que sou uma ninja poderosa!",
        "Eu não preciso ser protegida o tempo todo. Eu posso cuidar de mim mesma!",
        "Eu vou trazer Sasuke de volta, custe o que custar!",
        "Eu não sou só um rostinho bonito!",
        "Eu não quero ser vista como uma garota fraca!",
        "Eu não vou mais chorar. Eu vou me tornar uma ninja forte!",
        "Eu sou uma kunoichi de Konoha! Não subestime as garotas!",
        "Eu nunca vou desistir de trazer Sasuke de volta!",
        "Eu não preciso dos seus elogios, eu só quero ser útil para o time!",
        "Eu sou Sakura Haruno, a futura médica ninja!"
    ],
    "Rock Lee": [
        "Eu não preciso de ninjutsu ou genjutsu. Eu vou me tornar um mestre do taijutsu!",
        "Mesmo que eu não tenha talento natural, vou me esforçar e superar meus limites!",
        "A persistência é a chave para o sucesso! Eu nunca vou desistir!",
    ],
    "Choji Akimichi": [
        "Eu sou grande e forte! Vou proteger meus amigos com todo o meu poder!",
        "A comida é minha paixão! Não posso resistir a um bom prato!",
        "Não subestime o poder de um Akimichi!",
    ],
    "Neji Hyuga": [
        "Meu Byakugan me permite ver através de todas as ilusões!",
        "O destino não é algo imutável. Eu vou mudar meu próprio destino!",
        "A verdadeira força vem de se livrar das fraquezas.",
    ],
    "Shikamaru Nara": [
        "Que problema... isso é tão problemático.",
        "Eu prefiro ficar deitado e observar as nuvens... é menos problemático.",
        "Às vezes, a pessoa mais preguiçosa pode ser a mais inteligente.",
    ],
    "Konohamaru Sarutobi": [
        "Eu sou o futuro Hokage! Vou superar o Naruto!",
        "Quando eu crescer, vou me tornar tão poderoso quanto o meu avô!",
        "Não importa o quão difícil seja, eu vou seguir em frente!",
    ],
    "Itachi Uchiha": [
        "A verdadeira força está no coração, não nas habilidades.",
        "Às vezes, é necessário suportar a tristeza para alcançar a paz.",
        "Eu farei qualquer coisa para proteger a minha vila e minha família.",
    ],
    "Deidara": [
        "A verdadeira arte é uma explosão!",
        "Minhas criações de argila são uma forma de arte viva.",
        "O mundo precisa apreciar minha arte, mesmo que seja à força!",
    ],
    "Kisame Hoshigaki": [
        "Eu sou o tubarão do mar névoa, ninguém escapa da minha fome insaciável por batalha!",
        "Aqueles que estão dispostos a sacrificar tudo pelo poder são verdadeiramente fortes.",
        "A batalha não é uma questão de vencer ou perder, é uma questão de sobreviver ou morrer.",
    ],
    "Orochimaru": [
        "A imortalidade é o maior objetivo que se pode alcançar.",
        "A busca pelo conhecimento proibido é a única maneira de alcançar o verdadeiro poder.",
        "A morte é apenas o começo da minha evolução.",
    ],
    "Pain": [
        "A dor é a prova da existência.",
        "Para trazer a paz, é necessário quebrar a ilusão do mundo.",
        "A verdadeira justiça só pode ser alcançada pela dor e pelo sofrimento.",
    ],
    "Hinata Hyuga": [
        "Eu vou superar minha timidez e me tornar uma ninja forte!",
        "Meu amor por Naruto me dá força para superar qualquer desafio!",
        "Acreditar em si mesmo é a chave para alcançar o sucesso!",
    ],
     "Jiraiya": [
        "Eu sou o Super Pervertido Lendário Jiraiya!",
        "Um shinobi nunca desiste! Nunca desistir é meu modo ninja!",
        "Vou escrever um novo capítulo em minha história ninja!",
    ],
    "Tsunade Senju": [
        "Eu sou a Quinta Hokage! Não subestime o poder de uma mulher!",
        "Acredite em si mesmo e nunca desista!",
        "A coragem é a chave para superar qualquer obstáculo!",
    ],
    "Gaara": [
        "Eu sou a areia que protege a Vila da Areia!",
        "A solidão é dolorosa... mas às vezes é necessário.",
        "Aqueles que não podem encontrar um propósito na vida são mais assustadores que a morte.",
        "Eu costumava odiar tudo e todos... mas agora eu encontrei pessoas que me importam.",
        "Através da dor e do sofrimento, eu encontrei meu verdadeiro caminho.",
        "Aqueles que não conhecem o verdadeiro amor nunca poderão conhecer a verdadeira dor.",
    ],
      "Kiba Inuzuka": [
        "Meu olfato e o de Akamaru nunca falham! Nós sempre faremos justiça!",
        "Um verdadeiro shinobi e seu companheiro nunca se separam.",
        "Akamaru e eu somos uma equipe imbatível!",
        "Eu farei qualquer coisa para proteger meus amigos e minha matilha!",
        "Eu sou Kiba Inuzuka, o melhor amigo de Akamaru!",
        "Meu instinto animal nunca me falha!",
    ],
    "Temari": [
        "Meu leque de vento é a minha arma mais poderosa!",
        "Não subestime o poder do vento!",
        "Eu sou uma mulher forte e independente!",
        "Eu vou trazer a vitória para a Vila da Areia!",
        "Eu sou Temari, a kunoichi do deserto!",
        "Eu não tenho paciência para tolos.",
    ],
    "Shino Aburame": [
        "Meus insetos são meus aliados mais confiáveis.",
        "A verdadeira força é silenciosa e implacável.",
        "Os insetos são seres fascinantes... e letais.",
        "Não subestime o poder da natureza!",
        "Eu sou Shino Aburame, o mestre dos insetos!",
        "Meu controle sobre os insetos é inigualável!",
    ],
    "Kankuro": [
        "Minhas marionetes são meu meio de expressão artística.",
        "Não há nada mais satisfatório do que controlar uma marionete com perfeição.",
        "Eu sou Kankuro, o manipulador de marionetes!",
        "As marionetes são minha forma de lutar e proteger minha vila.",
        "Eu domino o poder das marionetes com maestria!",
        "Não subestime o poder de uma marionete habilidosa.",
    ],
    "Tenten": [
        "Eu sou especialista em armas! Meu arsenal nunca falha!",
        "A precisão é a chave para dominar as armas ninja.",
        "Não subestime a habilidade de uma verdadeira especialista em armas!",
        "Eu sou Tenten, a kunoichi das armas!",
        "Com minhas armas, eu nunca perco o alvo!",
        "Eu transformo armas em arte!",
    ],
    "Ino Yamanaka": [
        "Eu sou uma kunoichi talentosa e elegante!",
        "Meus jutsus mentais são minha arma secreta!",
        "Eu vou superar todas as expectativas e me tornar uma ninja poderosa!",
        "Eu sou Ino Yamanaka, a especialista em técnicas de mente!",
        "Nunca subestime o poder da mente!",
        "Minhas técnicas de mente são imbatíveis!",
    ],
      "Might Guy": [
        "Eu sou o Poderoso Ninja que não pode usar ninjutsu ou genjutsu!",
        "A juventude é a maior força do mundo!",
        "Aqueles que acreditam na juventude podem superar qualquer desafio!",
    ],
    "Tsunami": [
        "Eu sou a mãe de Naruto! Vou protegê-lo com todas as minhas forças!",
        "O amor de uma mãe é incondicional e poderoso!",
        "Eu tenho orgulho de ser a mãe do futuro Hokage!",
    ],
    "Iruka Umino": [
        "Eu sou o professor dedicado de Naruto! Vou guiá-lo pelo caminho ninja!",
        "Acredito no potencial de cada aluno!",
        "A maior recompensa de um professor é ver seu aluno ter sucesso!",
    ],
    "Shizune": [
        "Eu sou a fiel assistente de Tsunade! Vou apoiá-la em todas as situações!",
        "A lealdade é uma qualidade valiosa em um shinobi.",
        "Com sabedoria e habilidade, podemos superar qualquer desafio!",
    ],
    "Kurenai Yuhi": [
        "Eu sou Kurenai Yuhi, a especialista em genjutsu!",
        "Os olhos podem enganar... cuidado com os meus genjutsus!",
        "A verdadeira força está na mente e na estratégia.",
    ],
    "Anko Mitarashi": [
        "Eu sou Anko Mitarashi, a especialista em jutsus do tipo serpente!",
        "As serpentes são minhas aliadas mais confiáveis!",
        "Não subestime o poder das serpentes!",
    ],
    "Yamato": [
        "Eu sou Yamato, o especialista em controle de chakra!",
        "Meu poder de controle de chakra é imbatível!",
        "A harmonia entre o homem e a natureza é essencial para ser um shinobi de sucesso.",
    ],
    "Suigetsu Hozuki": [
        "Eu sou Suigetsu Hozuki, o usuário do jutsu da água!",
        "A água é minha aliada e minha fonte de poder!",
        "Eu sou fluído como a água e invencível como um tsunami!",
    ],
    "Karui": [
        "Eu sou Karui, a ninja da Vila da Nuvem!",
        "Não me subestime! Eu sou uma kunoichi poderosa!",
        "Vou lutar com todas as minhas forças para proteger meus amigos e minha vila!",
    ],    "Darui": [
        "Eu sou Darui, o shinobi habilidoso da Vila da Nuvem!",
        "Meu raio negro é imbatível!",
        "Não mexa com a Nuvem Negra!",
    ],
    "Mabui": [
        "Eu sou Mabui, a mensageira da Vila das Nuvens!",
        "Minha técnica de teletransporte é uma das mais rápidas!",
        "Eu posso entregar qualquer mensagem, não importa o quão longe seja!",
    ],
    "Ao": [
        "Eu sou Ao, o especialista em técnicas de sensor da Vila da Névoa!",
        "Meu Byakugan é afiado e implacável!",
        "Eu nunca perco nada que esteja acontecendo ao meu redor!",
    ],
    "Kurotsuchi": [
        "Eu sou Kurotsuchi, a líder da Vila da Pedra!",
        "A terra é minha aliada e minha proteção!",
        "Eu vou lutar com coragem e determinação!",
    ],
    "Akatsuchi": [
        "Eu sou Akatsuchi, o shinobi da Vila da Pedra!",
        "Meu poderoso jutsu de transformação da terra é imbatível!",
        "Eu defendo a Vila da Pedra com toda a minha força!",
    ],
    "Samui": [
        "Eu sou Samui, a kunoichi poderosa da Vila da Nuvem!",
        "Meu jutsu de relâmpago é veloz e devastador!",
        "Eu não tenho medo de enfrentar qualquer desafio!",
    ],
    "Omoi": [
        "Eu sou Omoi, o shinobi corajoso da Vila da Nuvem!",
        "Minha espada corta através de qualquer obstáculo!",
         "Eu nunca recuo diante da batalha!"
    ],
      "Yugito Nii": [
        "Eu sou Yugito Nii, a portadora do Nibi, o Bijuu de Duas Caudas!",
        "Meu poder é feroz como o fogo!",
        "Eu sou uma kunoichi temível da Vila da Nuvem!",
    ],
    "Haku": [
        "Eu sou Haku, o shinobi habilidoso da Vila da Névoa!",
        "Minha arte do espelho é inigualável!",
        "Eu acredito na força do amor e da amizade.",
    ],
    "Kimimaro": [
        "Eu sou Kimimaro, o portador do Kekkei Genkai Shikotsumyaku!",
        "Meus ossos são minha arma mais poderosa!",
        "Eu daria minha vida pela minha vila e pelo meu clã!",
    ],
    "Shisui Uchiha": [
        "Eu sou Shisui Uchiha, o shinobi habilidoso do Clã Uchiha!",
        "Meu Sharingan é afiado como uma faca!",
        "Eu protegerei minha vila com minha vida!",
    ],
}

def obter_frase_aleatoria():
    personagem = random.choice(list(frases_naruto.keys()))
    frase = random.choice(frases_naruto[personagem])
    return frase, personagem

frase, personagem = obter_frase_aleatoria()

print("Personagem: ", personagem)
print("Frase: ", frase)

