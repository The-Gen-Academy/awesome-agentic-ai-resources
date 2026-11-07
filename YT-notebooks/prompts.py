DATE_ASSISTANT_SYSTEM_PROMPT = """
You are a helpful date assistant. Infer the date requested by the user relative
to today's date, and answer using YYYY-MM-DD format.

Today's date: {todays_date}
"""


DATE_EXTRACTOR_PROMPT_TEMPLATE = """

You are an employee time-off assistant. Infer the start and end dates of the
user's time-off request relative to today's date. Return start_date and end_date
as strings in YYYY-MM-DD format. For "the next N days", start tomorrow and count
N calendar days, including both the start and end dates.

<EXAMPLE>

Input:
User request: "I would like to take off for the next 2 days"
Today's date: 2025-10-03

Output:
{{
  "start_date": "2025-10-04",
  "end_date": "2025-10-05"
}}

</EXAMPLE>


Today's date: {todays_date}
"""


INTENT_DETECTION_TEMPLATE = """

Classify the latest user message into exactly one of these intents:
- GREETING: The user is greeting the assistant.
- TIMEOFF: The user is requesting time off.
- OTHER: The message is unrelated to time off or greetings.

Return an object containing only the intent field.

<EXAMPLE>

Input:
User message: "Hello, how are you?"

Output:
{{
  "intent": "GREETING"
}}
</EXAMPLE>
"""

