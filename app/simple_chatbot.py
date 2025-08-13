def simple_match(query, employees, min_match_words=1):
    query_lower = query.lower()
    query_words = query_lower.split()
    matched = []

    for emp in employees:
        combined_text = " ".join(emp["skills"] + emp["projects"]).lower()
        matched_words_count = sum(word in combined_text for word in query_words)
        if matched_words_count >= min_match_words:
            matched.append(emp)

    return matched[:3]

def format_response(query, matched):
    if not matched:
        return f"Sorry, I couldn't find any matches for: '{query}'."

    response = f"Found {len(matched)} potential match(es) for: '{query}':\n\n"
    for emp in matched:
        response += (
            f"- **{emp['name']}**: {emp['experience_years']} years experience, "
            f"Skills: {', '.join(emp['skills'])}, "
            f"Projects: {', '.join(emp['projects'])}, "
            f"Availability: {emp['availability']}\n"
        )
    return response

def filter_employees(query, employees):
    if isinstance(query, list):
        query = " ".join(query)

    matched = simple_match(query, employees)
    return format_response(query, matched)
