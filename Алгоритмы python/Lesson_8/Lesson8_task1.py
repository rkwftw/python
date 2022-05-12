# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

def handshakes_count(n):
    edges = [i for i in range(1, n + 1)]
    verts = []

    for i in edges:
        for j in range(i + 1, n + 1):
            verts.append((i, j))

    print(f'Количество рукопожатий: {len(verts)}')
    print(f'Пары рукопожатий: {verts}')


n = int(input('Веедите количество людей: '))
handshakes_count(n)