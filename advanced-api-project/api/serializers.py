from rest_framework import serializers
from .models import Author, Book
from datetime import date



class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Converts Book model instances to and from JSON representations.
    Includes all fields of the Book model and handles validation
    for individual book records.
    """
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Serializes the author's basic information along with a nested
    representation of all related books. The books field uses
    BookSerializer to dynamically include associated book records
    in the response.
    """
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["name"]
