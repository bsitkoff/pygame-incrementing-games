#!/usr/bin/env python3
import os
import sys
import subprocess
import json

# Add Codio assessments path
sys.path.append('/usr/share/codio/assessments')
from lib.grade import send_partial_v2, FORMAT_V2_HTML

def parse_arguments():
    """Parse command line arguments."""
    args = {
        'question_context': '',
        'use_llm': False,
        'debug': False
    }

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == '--question' and i + 1 < len(sys.argv):
            args['question_context'] = sys.argv[i + 1]
            i += 2
        elif arg == '--use-llm':
            args['use_llm'] = True
            i += 1
        elif arg == '--debug':
            args['debug'] = True
            i += 1
        else:
            i += 1

    return args

def check_with_llm(question: str, answer: str):
    """Use OpenAI to check if answer shows genuine engagement."""
    api_key = os.environ.get('OPENAI_API_KEY')
    base_url = os.environ.get('OPENAI_BASE_URL')

    if not api_key or not base_url:
        return False, "LLM not available"

    try:
        full_url = f"{base_url}/chat/completions"

        prompt = f"""You are helping a teacher assess student responses for genuine engagement.

Question: {question}

Student Answer: {answer}

Does this student response show a genuine attempt to engage with the question? Consider:
- Did they try to address what was asked?
- Is there evidence of thinking, even if incomplete or incorrect?
- Did they provide substance beyond minimal responses like "I don't know"?

Respond with only:
- "GENUINE" if they made a real attempt
- "NON_ATTEMPT" if it's clearly insufficient, off-topic, or avoids the question

Focus on effort and engagement, not correctness."""

        curl_data = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 20,
            "temperature": 0
        }

        curl_cmd = [
            'curl', '-X', 'POST', full_url,
            '-H', f'Authorization: Bearer {api_key}',
            '-H', 'Content-Type: application/json',
            '-d', json.dumps(curl_data),
            '--silent'
        ]

        result = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=15)

        if result.returncode != 0:
            return False, f"API call failed: {result.stderr}"

        response_data = json.loads(result.stdout)
        llm_response = response_data['choices'][0]['message']['content'].strip()

        is_genuine = "GENUINE" in llm_response.upper()
        return is_genuine, f"LLM full response: {llm_response}"

    except Exception as e:
        return False, f"LLM error: {str(e)}"

def main():
    """Main execution following Codio's official pattern."""
    VERSION = "3.1-debug"

    student_answer = os.environ.get('CODIO_FREE_TEXT_ANSWER', '')
    args = parse_arguments()

    if args['debug']:
        print(f"DEBUG: freetext.py version {VERSION}")
        print(f"DEBUG: Arguments parsed: {args}")
        print(f"DEBUG: Student answer: '{student_answer}'")
        print(f"DEBUG: Environment variables:")
        print(f"  OPENAI_API_KEY: {'SET' if os.environ.get('OPENAI_API_KEY') else 'NOT SET'}")
        print(f"  OPENAI_BASE_URL: {os.environ.get('OPENAI_BASE_URL') or 'NOT SET'}")

    if not student_answer.strip():
        print("🤔 You may want to revise this answer and resubmit - it looks like it might not be ready for your teacher.")
        exit(1)

    if args['use_llm'] and args['question_context']:
        is_genuine, debug_info = check_with_llm(args['question_context'], student_answer)

        if args['debug']:
            print(f"DEBUG: LLM result: genuine={is_genuine}, info={debug_info}")

        if is_genuine:
            print(f"✅ Your answer has been submitted to your teacher.")
            exit(0)
        else:
            print(f"🤔 You may want to revise this answer and resubmit - it looks like it might not be ready for your teacher.")
            if args['debug']:
                print(f"DEBUG: Rejection reason: {debug_info}")
            exit(1)
    else:
        print("✅ Your answer has been submitted to your teacher.")
        exit(0)

if __name__ == '__main__':
    main()
