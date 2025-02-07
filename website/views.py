from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/edit-note', methods=['POST'])
@login_required
def edit_note():
    try:
        note_data = json.loads(request.data)
        note_id = note_data['noteId']
        new_content = note_data['content']
        
        note = Note.query.get(note_id)
        if note and note.user_id == current_user.id:
            note.data = new_content
            db.session.commit()
            return jsonify({"success": True})
        
        return jsonify({"success": False, "error": "Note not found"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@views.route('/delete-note', methods=['POST'])
@login_required  # Added login_required decorator
def delete_note():  
    try:
        note_data = json.loads(request.data)
        note_id = note_data['noteId']
        note = Note.query.get(note_id)
        
        if not note:
            return jsonify({
                "success": False,
                "message": "Note not found!"
            }), 404
            
        if note.user_id != current_user.id:
            return jsonify({
                "success": False,
                "message": "Unauthorized access!"
            }), 403
            
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted successfully!', category='warning')
        
        return jsonify({
            "success": True,
            "message": "Note deleted successfully!"
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500