
from app_main import app
from tests import OhmTestCase


class CommunityTest(OhmTestCase):
    def test_get_community(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "Recently Created Users" in response.data
