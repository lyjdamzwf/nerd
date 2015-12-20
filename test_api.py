from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NSTypes

# init the client
#dev_token = "S=s10:U=1555f:E=159151dea97:C=151bd6cbd98:P=1cd:A=en-devtoken:V=2:H=380eababc06d9ea47ecb2c368c2eb79a"
dev_token = "S=s1:U=91d01:E=158f264ada0:C=1519ab38110:P=1cd:A=en-devtoken:V=2:H=13955499880239b6fa0dea8628cf34c1"
client = EvernoteClient(token=dev_token)


# userStore operations
userStore = client.get_user_store()
user = userStore.getUser()
print user.username


# noteStore operations
noteStore = client.get_note_store()

notebooks = noteStore.listNotebooks()
for nb in notebooks:
    filter = NSTypes.NoteFilter()
    filter.notebookGuid = nb.guid

    # noteResultSpec = NSTypes.NotesMetadataResultSpec()
    # noteResultSpec.includeTitle = True

    # noteMDList = noteStore.findNotesMetadata(filter, 0, 100, noteResultSpec)

    # for noteMD in noteMDList.notes:
    #     print noteMD.title

    noteList = noteStore.findNotes(filter, 0, 100)

    for note in noteList.notes:
        noteContent = noteStore.getNoteContent(note.guid)
        print note.title + "-" + noteContent



# note = Types.Note()
# note.title = "heheda"
# note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
# note.content += '<en-note>hahahaha</en-note>'
# # note.content += 'hahaha'
# note = noteStore.createNote(note)
