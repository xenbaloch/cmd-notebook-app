import datetime

# Store the next available id for all new notes
last_id = 0


# A class to represent a note in the notebook
class Note:

    def __init__(self, memo, tags=""):
        """Initialize a note with a memo and optional space-separated tags.
        Automatically seth the note's creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """A function that matches the notes against filtered text. Returns True
        if it matches, otherwise False.

        Search is case sensitive and matches both text and tags."""
        return filter in self.memo or filter in self.tags


# A class to represent the collection of Notes that can be tagged, modified, and searched
class Notebook:
    def __init__(self):
        """Initialize the notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """Locate the note with the given id"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value."""
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter):
        """Find all the notes that matches the given filter string"""
        return [note for note in self.notes if note.match(filter)]
