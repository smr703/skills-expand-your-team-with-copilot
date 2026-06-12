import unittest
from pathlib import Path

from src.backend.database import init_database
from src.backend.routers.activities import get_activities


class DifficultyLevelsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_database()
        cls.index_html = Path(
            "/home/runner/work/skills-expand-your-team-with-copilot/"
            "skills-expand-your-team-with-copilot/src/static/index.html"
        ).read_text(encoding="utf-8")

    def test_activity_api_returns_optional_difficulty_levels(self):
        activities = get_activities()

        self.assertEqual(
            activities["Programming Class"]["difficulty_level"], "Beginner"
        )
        self.assertEqual(
            activities["Science Olympiad"]["difficulty_level"], "Advanced"
        )
        self.assertNotIn("difficulty_level", activities["Chess Club"])

    def test_difficulty_filter_buttons_are_present(self):
        self.assertIn("Filter by difficulty:", self.index_html)
        self.assertIn('data-difficulty=""', self.index_html)
        self.assertIn('data-difficulty="Beginner"', self.index_html)
        self.assertIn('data-difficulty="Intermediate"', self.index_html)
        self.assertIn('data-difficulty="Advanced"', self.index_html)


if __name__ == "__main__":
    unittest.main()
