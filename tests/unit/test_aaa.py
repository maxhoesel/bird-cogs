import aaa
from aaa import responses


def test_get_response():
    triggers = ["aaa", "yarr"]
    for t in triggers:
        resp = responses.get_response(t)
        assert isinstance(resp, str)
        assert len(resp) > 0
