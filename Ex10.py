class TestPhrase:
    def test_length(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Phrase is too long!"