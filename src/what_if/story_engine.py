STORY = {
    "start": {
        "title": "What If… Iron Man Hesitated?",
        "text": "The Nano Gauntlet pulses in Tony’s hand...",
        "choices": [
            {"text": "He tries to remove the Stones safely", "to": "stone_extraction"},
            {"text": "He passes the Gauntlet to Strange", "to": "give_to_strange"}
        ]
    },

    "stone_extraction": {
        "title": "Attempting Stone Extraction",
        "text": "Tony calls on Friday to attempt micro-extraction…",
        "choices": [
            {"text": "Continue extraction", "to": "extraction_success"},
            {"text": "Abort and reconsider", "to": "start"}
        ]
    },
}
