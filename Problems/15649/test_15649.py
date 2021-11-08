import io
from ans_15649 import *


def test_OpInsert_1(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("6 3\n"))
    solve()
    capture = capsys.readouterr()
    assert (
        capture.out
        == "1 2 3 \n1 2 4 \n1 2 5 \n1 2 6 \n1 3 2 \n1 3 4 \n1 3 5 \n1 3 6 \n1 4 2 \n1 4 3 \n1 4 5 \n1 4 6 \n1 5 2 \n1 5 3 \n1 5 4 \n1 5 6 \n1 6 2 \n1 6 3 \n1 6 4 \n1 6 5 \n2 1 3 \n2 1 4 \n2 1 5 \n2 1 6 \n2 3 1 \n2 3 4 \n2 3 5 \n2 3 6 \n2 4 1 \n2 4 3 \n2 4 5 \n2 4 6 \n2 5 1 \n2 5 3 \n2 5 4 \n2 5 6 \n2 6 1 \n2 6 3 \n2 6 4 \n2 6 5 \n3 1 2 \n3 1 4 \n3 1 5 \n3 1 6 \n3 2 1 \n3 2 4 \n3 2 5 \n3 2 6 \n3 4 1 \n3 4 2 \n3 4 5 \n3 4 6 \n3 5 1 \n3 5 2 \n3 5 4 \n3 5 6 \n3 6 1 \n3 6 2 \n3 6 4 \n3 6 5 \n4 1 2 \n4 1 3 \n4 1 5 \n4 1 6 \n4 2 1 \n4 2 3 \n4 2 5 \n4 2 6 \n4 3 1 \n4 3 2 \n4 3 5 \n4 3 6 \n4 5 1 \n4 5 2 \n4 5 3 \n4 5 6 \n4 6 1 \n4 6 2 \n4 6 3 \n4 6 5 \n5 1 2 \n5 1 3 \n5 1 4 \n5 1 6 \n5 2 1 \n5 2 3 \n5 2 4 \n5 2 6 \n5 3 1 \n5 3 2 \n5 3 4 \n5 3 6 \n5 4 1 \n5 4 2 \n5 4 3 \n5 4 6 \n5 6 1 \n5 6 2 \n5 6 3 \n5 6 4 \n6 1 2 \n6 1 3 \n6 1 4 \n6 1 5 \n6 2 1 \n6 2 3 \n6 2 4 \n6 2 5 \n6 3 1 \n6 3 2 \n6 3 4 \n6 3 5 \n6 4 1 \n6 4 2 \n6 4 3 \n6 4 5 \n6 5 1 \n6 5 2 \n6 5 3 \n6 5 4 \n"
    )
