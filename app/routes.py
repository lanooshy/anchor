# Defines the API routes

from flask import Blueprint, request, jsonify
from .models.summarizer import summarize_text
from .models.task_extractor import extract_tasks

api = Blueprint('api', __name__)

@api.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    discussion_text = data.get('text', '')
    summary = summarize_text(discussion_text)
    return jsonify({"summary": summary})

@api.route('/extract-tasks', methods=['POST'])
def extract_tasks_endpoint():
    data = request.json
    discussion_text = data.get('text', '')
    tasks = extract_tasks(discussion_text)
    return jsonify({"tasks": tasks})
