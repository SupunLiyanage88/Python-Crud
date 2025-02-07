function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((res) => res.json())
    .then(data => {
        if (data.success) {
            // Remove the note element from DOM
            const noteElement = document.getElementById(`note-${noteId}`);
            if (noteElement) {
                noteElement.remove();
            }
            
            // Reload page to show flash message
            window.location.reload();
        } else {
            // Handle error cases
            alert(data.message || "Error deleting note");
        }
    })
    .catch(e => {
        console.error("Error:", e);
        alert("An error occurred while deleting the note");
    });
}