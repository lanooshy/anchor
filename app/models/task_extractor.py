import re

def extract_tasks(discussion_text):
    # Basic regex for identifying tasks
    task_pattern = r"(?:I'll|We need to|Let's|Can someone|Please).*"
    tasks = re.findall(task_pattern, discussion_text, re.IGNORECASE)
    return tasks
