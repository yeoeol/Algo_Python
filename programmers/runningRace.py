def solution(players, callings):
    players_rank = {name:rank for rank, name in enumerate(players)}

    for name in callings:
        players_rank[name] -= 1
        players_rank[players[players_rank[name]]] += 1

        players[players_rank[name]], players[players_rank[name]+1] = players[players_rank[name]+1], players[players_rank[name]]

    return players

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])