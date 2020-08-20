from tutorial.snippets.models import Snippet
from tutorial.snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Serialize
snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
print(serializer.data)

content = JSONRenderer().render(serializer.data)
print(content)
