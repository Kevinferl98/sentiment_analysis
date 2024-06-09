import unittest
from app.routes import analyze_sentiment
from app import create_app
from unittest.mock import patch, MagicMock

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_analyze_sentiment(self):
        text = "This is a test"
        result = analyze_sentiment(text)
        self.assertIn('text', result)
        self.assertIn('polarity', result)
        self.assertIn('subjectivity', result)
        self.assertEqual(result['text'], text)
        self.assertTrue(-1 <= result['polarity'] <= 1)
        self.assertTrue(-1 <= result['subjectivity'] <= 1)

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('app.routes.mongo')
    def test_sentiment_analysis_route_2(self, mock_mongo):
        mock_collection = mock_mongo.collection
        mock_collection.insert_one.return_value = MagicMock()
        response = self.client.post('/sentiment_analysis', json={'text': 'This is a test'})
        self.assertEqual(response.status_code, 200)
        mock_collection.insert_one.assert_called_once()


if __name__ == '__main__':
    unittest.main()