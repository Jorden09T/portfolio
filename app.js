let notes = []
let editingNoteId = null


function loadNotes() {
    const savedNotes = localStorage.getItem('quickNotes')
    return savedNotes ? JSON.parse(savedNotes) : []
}

/* saves Note without causing a refresh */
function saveNote(event){
    event.preventDefault()

    /* .trim gets rid of white space */
    const title = document.getElementById('noteTitle').value.trim();
    const content = document.getElementById('noteContent').value.trim();

    if(editingNoteId){
        //update exisiting note
        const noteIndex = notes.findIndex(note => note.id === editingNoteId)
        //searches for the note index in the notes array
        notes[noteIndex] = {
            ...notes[noteIndex],
            title: title,
            content: content
        }
    } else {
        //add new note

        /* unshift adds a value to the beginning of the array / each note has 3 properities */
        notes.unshift({
            id: generateId(),
            title: title,
            content: content
        })
    
    }

    
    /* Saves all the Notes */
    saveNotes()
    renderNotes()
}

/* returns current time stamp as a string */
function generateId(){
    return Date.now().toString()
}

/* a function to store notes that we save - localstorage only stores strings */
function saveNotes(){
    localStorage.setItem('quickNotes', JSON.stringify(notes))
}

function deleteNote(noteId) {
    notes = notes.filter(note => note.id != noteId)
    saveNotes()
    renderNotes()
}



/* function that updates the page based on the # of notes */
function renderNotes(){
    const notesContainer = document.getElementById('notesContainer');

    if(notes.length === 0){
        notesContainer.innerHTML = `
            <div class="empty-state">
                <h2>No notes yet</h2>
                <p>Create your first note to get started!</p>
                <button class="add-note-btn" onclick="openNoteDialog()">+ Add Your First Note</button>
            <div>
        `
        return
    }
    
    /* setting the inner html = expects a string, .map allows us to execute for each note */
    notesContainer.innerHTML = notes.map(note => `
        <div class="note-card">
            <h3 class="note-title">${note.title}</h3>
            <p class="note-content">${note.content}</p>
            <div class="note-actions">
                <button class="edit-btn" onclick="openNoteDialog('${note.id}')" title="Edit Note">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>
                    </svg>
                </button>
                <button class="delete-btn" onclick="deleteNote('${note.id}')" title="Delete Note">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M18.3 5.71c-.39-.39-1.02-.39-1.41 0L12 10.59 7.11 5.7c-.39-.39-1.02-.39-1.41 0-.39.39-.39 1.02 0 1.41L10.59 12 5.7 16.89c-.39.39-.39 1.02 0 1.41.39.39 1.02.39 1.41 0L12 13.41l4.89 4.88c.39.39 1.02.39 1.41 0 .39-.39.39-1.02 0-1.41L13.41 12l4.89-4.89c.38-.38.38-1.02 0-1.4z"/>
                    </svg>
                </button>
            </div>
        </div>
        `).join('')
}

function openNoteDialog(noteId = null) {
    const dialog = document.getElementById('noteDialog');
    const titleInput = document.getElementById('noteTitle');
    const contentInput = document.getElementById('noteContent');


    if(noteId){
        //edit the () with (noteId)
        const noteToEdit = notes.find(note => note.id === noteId)
        editingNoteId = noteId
        document.getElementById('dialogTitle').textContent = 'Edit Note'
        titleInput.value = noteToEdit.title
        contentInput.value = noteToEdit.content
    } else {
        //creating a new note
        editingNoteId = null
        document.getElementById('dialogTitle').textContent = 'Add New Note'
        titleInput.value = ''
        contentInput.value = ''
    }

    /*opens dialog elements */
    dialog.showModal()
    /*Jumps into the title field */
    titleInput.focus()
}

/* close Note */
function closeNoteDialog() {
    document.getElementById('noteDialog').close()
}

function toggleTheme() {
    const isDark = document.body.classList.toggle('dark-theme')
    localStorage.setItem('theme', isDark ? 'dark' : 'light')
    document.getElementById('themeToggleBtn').textContent = isDark ? '🌞':'🌙'
}

function applyStoredTheme() {
    if(localStorage.getItem('theme') === 'dark'){
        document.body.classList.add('dark-theme')
        document.getElementById('themeToggleBtn').textContent = '🌞'
    }
}

/* close Note when clicking outside of note, runs when document is loaded and contains most of your
logic content*/
document.addEventListener('DOMContentLoaded', function(){
    applyStoredTheme()

    /* sets gobal notes array to be whatever is in the local storage */
    notes = loadNotes()

    /* shows the rendered notes*/
    renderNotes()

    /* note creation when forum is submitted */
    document.getElementById('noteForm').addEventListener('submit', saveNote)

    //Dark mode
    document.getElementById('themeToggleBtn').addEventListener('click', toggleTheme)


    /* submit event = close note by clicking anywhere but forum */
    document.getElementById('noteDialog').addEventListener('click', function(event){
        if(event.target == this) {
            closeNoteDialog()
        }
    })
})