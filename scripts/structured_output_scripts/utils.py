from re import S
from google import genai
from pydantic import BaseModel, Field, model_validator
from typing import Optional
import enum
import json


class QuestionFormat(enum.Enum):
    MULTIPLE_CHOICE = 'multiple_choice'
    SHORT_ANSWER = 'short_answer'

class QuestionContent(enum.Enum):
    """ 
    Knowledge questions are about factual recall. Skill-based questions involve an activity 
    or application of knowledge.
    """
    # knowledge
    HISTORY = 'history'
    MYTHOLOGY = 'mythology'
    GEOGRAPHY = 'geography'
    LITERATURE = 'literature'

    # skills
    READING_COMPREHENSION = 'reading_comprehension'
    VOCABULARY = 'vocabulary'
    GRAMMAR = 'grammar'
    TRANSLATION = 'translation'
    LITERARY_DEVICES = 'literary_devices' # also poetic devices
    
class Language(enum.Enum):
    LATIN = 'latin'
    ENGLISH = 'english'
    BOTH = 'both' # only if each language is equally represented, or both are explicitly asked for

class Difficulty(enum.Enum):
    BEGINNER = 'beginner' # 1st year, novice
    INTERMEDIATE = 'intermediate' # 2nd year
    ADVANCED = 'advanced' # 3rd and 4th year
    NA = 'na' # not applicable, for questions that are not language related
    UNKNOWN = 'unknown'


class Passage(BaseModel):
    passage_id: str  # unique
    text: str
    language: Language
    source_name: str
    source_year: int
    questions: list[str]


class Question(BaseModel):
    source_name: str
    source_year: int

    question_id: str # unique identifier for the question
    question_format: QuestionFormat
    question_content: QuestionContent 
    passage_id: Optional[str] = None # if question_content is reading_comprehension
    
    difficulty: Difficulty
    question_language: Language
    answer_language: Language

    question: str
    multiple_choice_options: list[str] # ["a: text", "b: text", ...] or empty
    answers: list[str] # correct answer(s)


class AlignedTextBlock(BaseModel):
    question_text: str 
    answer_text: str

    question_instructions: Optional[str] = None

config={'response_mime_type': 'application/json',
        'response_schema': list[Question]}

config_aligned_text_block = {
    'response_mime_type': 'application/json',
    'response_schema': list[AlignedTextBlock]
}