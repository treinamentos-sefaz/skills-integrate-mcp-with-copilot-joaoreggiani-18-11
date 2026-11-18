import unittest

from src.app import activities, get_activities, signup_for_activity


class GitHubSkillsActivityTests(unittest.TestCase):
    def test_activity_is_available_for_signup(self):
        activity_name = "GitHub Skills"
        student_email = "student@mergington.edu"

        self.assertIn(activity_name, get_activities())
        activity = get_activities()[activity_name]
        self.assertEqual(activity["participants"], [])

        result = signup_for_activity(activity_name, student_email)
        self.addCleanup(activity["participants"].remove, student_email)

        self.assertEqual(
            result,
            {"message": "Signed up student@mergington.edu for GitHub Skills"},
        )
        self.assertIn(student_email, activity["participants"])


if __name__ == "__main__":
    unittest.main()
