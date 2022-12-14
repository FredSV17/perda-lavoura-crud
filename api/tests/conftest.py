from main import create_app
import pytest

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

# @pytest.fixture(scope='module')
# def test_clear_table(test_client):
#     response = test_client.delete('loss/clear')
#     assert response.status_code == 200
