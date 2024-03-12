from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from issue.models import Issue
from issue.views import IssueAPIView, IssueDetailsAPIView


# Create your tests here.
class IssueAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        # mock data
        self.mock_issue = Issue.objects.create(
            title="Issue #1",
            description="The Issue Details and the impact it has on your application's users.",
        )

    def test_get_issues(self):
        response = IssueAPIView.as_view()(self.factory.get("/issues/"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_issues(self):
        data = {
            "title": "Issues #2",
            "description": "The Issue Details and the impact it has on your application's users.",
        }
        response = IssueAPIView.as_view()(self.factory.post("/issues/", data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_issue_details(self):
        response = IssueDetailsAPIView.as_view()(
            self.factory.get("/issues/"), pk=self.mock_issue.id
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.mock_issue.id, response.data["id"])

    def test_put_issue_details(self):
        new_title = "Issues #1 (Amended)"
        data = {
            "title": new_title,
            "description": "The Issue Details and the impact it has on your application's users.",
        }
        response = IssueDetailsAPIView.as_view()(
            self.factory.put("/issues/", data), pk=self.mock_issue.id
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.mock_issue.refresh_from_db()
        self.assertEqual(self.mock_issue.title, new_title)

    def test_delete_issue_details(self):
        mock_issue = Issue.objects.create(
            title="Issue #3 (To be deleted)",
            description="The Issue Details and the impact it has on your application's users.",
        )
        response = IssueDetailsAPIView.as_view()(
            self.factory.delete("/issues/"), pk=mock_issue.id
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = IssueDetailsAPIView.as_view()(
            self.factory.get("/issues/"), pk=mock_issue.id
        )
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
