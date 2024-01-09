class Playlist:
    def __init__(self, nome, genero, musicas):
        self.nome = nome
        self.genero = genero
        self.musicas = musicas

    def adicionar(self, musica):
        self.musicas.append(musica)

    def remover(self):
        self.musicas.pop()

    def reproduzir(self):
        print(f"Play em {self.nome}")
        for musica in self.musicas:
            print(f"Tocando {musica}...")
        print("Essa festa foi um sucesso!")

    def duracao(self):
        duracao_playlist = len(self.musicas) * 3
        return duracao_playlist

qtd_playlists = int(input())

playlists = []
for i in range(qtd_playlists):
    nome = input()
    genero = input()
    musicas = input().split(", ")
    playlist = Playlist(nome, genero, musicas)
    playlists.append(playlist)

genero_festa = input()
duracao_festa = int(input())

playlist_festa = None

for playlist in playlists:
    if playlist.genero == genero_festa:
        playlist_festa = playlist
        break

if not playlist_festa:
    print(f"Não tenho nenhuma playlist do gênero {genero_festa}, infelizmente não poderei tocar")
else:
    if duracao_festa > playlist_festa.duracao() and (duracao_festa - playlist_festa.duracao()) // 3 != 0:
        n = (duracao_festa - playlist_festa.duracao()) // 3
        for i in range(n):
            musica_extra = input()
            playlist_festa.adicionar(musica_extra)
        print(f'Precisaremos adicionar mais {n} músicas a playlist {playlist_festa.nome}')
    elif duracao_festa < playlist_festa.duracao() and (playlist_festa.duracao() - duracao_festa) // 3 != 0:
        n = (playlist_festa.duracao() - duracao_festa) // 3
        for i in range(n):
            playlist_festa.remover()
        print(f'Precisaremos remover {n} músicas da playlist {playlist_festa.nome}')

    playlist_festa.reproduzir()