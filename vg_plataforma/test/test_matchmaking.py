import pytest
from matchmaking import Matchmaker, Player




def test_matchmaker_pairs_similar_rating():
    m = Matchmaker()
    p1 = Player(id="p1", rating=1200)
    p2 = Player(id="p2", rating=1210)
    p3 = Player(id="p3", rating=1500)

    m.enqueue(p1)
    m.enqueue(p2)
    m.enqueue(p3)

    matches = m.find_matches()

    # Debe emparejar p1 con p2, y dejar p3 en cola
    assert any((a.id == 'p1' and b.id == 'p2') or (a.id == 'p2' and b.id == 'p1') for a, b in matches)
    assert all('p3' not in (a.id, b.id) for a, b in matches)




def test_rating_update_after_game():
    m = Matchmaker()
    p1 = Player(id='p1', rating=1200)
    p2 = Player(id='p2', rating=1200)


    new_r1, new_r2 = m.update_ratings(p1, p2, winner_id='p1')
    assert new_r1 > 1200
    assert new_r2 < 1200