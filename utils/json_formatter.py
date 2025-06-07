import json

def format_json(response):
    # Takes a parsed json or a dictionary with 'body' as key

    try:
        # If dict with 'body' as key, parse
        if isinstance(response, dict) and 'body' in response:
            body = json.loads(response['body'])
        else:
            # Otherwise assume it's already been parsed
            body = response
        pretty = json.dumps(body, indent=4, sort_keys=True)
        return pretty
    except Exception as e:
        return f"Error formatting JSON: {str(e)}"
