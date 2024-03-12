from django import urls
from issue.views import IssueAPIView, IssueDetailsAPIView


urlpatterns = [
    urls.path("", IssueAPIView.as_view(), name="issues"),
    urls.path("<int:pk>/", IssueDetailsAPIView.as_view(), name="issue details"),
]