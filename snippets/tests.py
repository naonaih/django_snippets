from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import resolve
from snippets.views import top, snippets_new, snippets_edit, snippets_detail
from snippets.models import Snippet

# Create your tests here.

UserModel = get_user_model()

class = CreateSnippetTest(TestCase):
	def setUp(self):
		self.user = UserModel.objects.create(
			username="test_user",
			email="test@example.com",
			password="top_select_pass0001",
			)
		self.client.force_login(self.user)

	def test_render_creation_form(self):
		response = self.client.get("/snippets/new/")
		self.assertContains(response, "スニペットの登録",status_code=200)

	def test_create_snippet(self):
		date = {'title': 'タイトル','code':'コード','description':'解説'}
		self.client.post("/snippets/new",date)
		snippet = Snippet.objects.get(title='タイトル')
		self.assertEqual('コード',snippet.code)
		self.assertEqual('解説',snippet.description)
	





# class SnippetDetailTest(TestCase):
# 	def setUp(self):
# 		self.user = UserModel.objects.create(
# 			username="test_user",
# 			email="test@example.com",
# 			password="top_select_pass0001",
# 			)
# 		self.snippet = Snippet.objects.create(
# 			title="title1",
# 			code="print('Hello')",
# 			description="description1",
# 			created_by=self.user,
# 			)

# 	def test_should_use_expected_template(self):
# 		response = self.client.get("/snippet/%s" % self.snippet.id)
# 		self.assertTemplateUsed(response, "snippet/snippets_detail_html")

# 	def test_top_page_returns_200_and_expected_heading(self):
# 		response = self.client.get("/snippet/%s" % self.snippet.id)
# 		self.assertContains(response, self.snippet.title, status_code=200)




# class topPageRenderSnippetsTest(TestCase):
# 	def setUp(self):
# 		self.user = UserModel.objects.create(
# 			username="test_user",
# 			email="test@example.com",
# 			password="top_select_pass0001",
# 			)
# 		self.snippet = Snippet.objects.create(
# 			title="title1",
# 			code="print('Hello')",
# 			description="description1",
# 			created_by=self.user,
# 			)

	# def test_should_return_snippet_title(self):
	# 	request = RequestFactory().get("/")
	# 	request.user = self.user
	# 	response = top(request)
	# 	self.assertContains(response, self.snippet.title)

	# def test_should_return_username(self):
	# 	request = RequestFactory().get("/")
	# 	request.user = self.user
	# 	response = top(request)
	# 	self.assertContains(response, self.user.username)	

# class TopPageViewTest(TestCase):
# 	def test_top_returns_200(self):
# 		#request = HttpRequest()
# 		response = self.client.get("/")
# 		self.assertEqual(response.status_code,200)

# 	def test_top_expected_content(self):
# 		request = HttpRequest()
# 		response = top(request)
# 		self.assertEqual(response.content,b"Hello World")


# class CreateSnippetsTest(TestCase):
# 	def test_should_resolve_snippets_new(self):
# 		found = resolve("/snippets/new/")
# 		self.assertEqual(snippets_new, found.func)

# class SnippetsDetailTest(TestCase):
# 	def test_should_resolve_snippets_detail(self):
# 		found = resolve("/snippets/1/")
# 		self.assertEqual(snippets_detail, found.func)

# class EditSnippetsTest(TestCase):
# 	def test_should_resolve_snippets_edit(self):
# 		found = resolve("/snippets/1/edit/")
# 		self.assertEqual(snippets_edit, found.func)

# class TopPageTest(TestCase):
# 	def test_top_page_returns_200_and_expected_title(self):
# 		response = self.client.get("/")
# 		self.assertContains(response, "Djangoスニペット",status_code=200)

# 	def test_top_page_uses_expected_template(self):
# 		response = self.client.get("/")
# 		self.assertTemplateUsed(response,"snippets/top.html")



