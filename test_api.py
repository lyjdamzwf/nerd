from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

# init the client
dev_token = "S=s1:U=91d01:E=158f264ada0:C=1519ab38110:P=1cd:A=en-devtoken:V=2:H=13955499880239b6fa0dea8628cf34c1"
client = EvernoteClient(token=dev_token)


# userStore operations
userStore = client.get_user_store()
user = userStore.getUser()
print user.username


# noteStore operations
noteStore = client.get_note_store()

notebooks = noteStore.listNotebooks()
for n in notebooks:
    print n.name

note = Types.Note()
note.title = "test title"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>hahahaha</en-note>'
# note.content += 'hahaha'
note = noteStore.createNote(note)
