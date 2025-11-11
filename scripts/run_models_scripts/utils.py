
model_names_to_endpoints = {
    'qwq': 'Qwen/QwQ-32B',
    'qwen3': 'Qwen/Qwen3-32B',
    'llama3': 'meta-llama/Llama-3.3-70B-Instruct',
    'llama3-turbo': 'meta-llama/Llama-3.3-70B-Instruct-Turbo',
    'gpt-oss': "openai/gpt-oss-120b",
    'deepseek-r1': 'deepseek-ai/DeepSeek-R1-0528',
    'deepseek': 'deepseek-ai/DeepSeek-R1',
    'o3-mini': 'o3-mini-2025-01-31'
}

sys_prompt = '''You are a Classicist with expert knowledge in Greek and Roman history, language, and culture.'''
mc_format_instructions= '''At the end of your response, give the letter of the correct answer as
Answer: Letter'''
short_ans_one_word_format_instructions= '''At the end of your response, give your answer as a single word like this:
Answer: Word'''
long_ans_format_instructions= '''At the end of your response, give your answer as:
Answer: answer text'''
feet_eng_instr = '''The possible feet are: amphibrac, anapest, choriamb, dactyl, dichoree, great ionic, iambus, pyrrhic, second epitrit, small ionic, spondee, tribrac, trochee'''
feet_lat_instr = '''Pedes possibiles sunt: amphibrac, anapest, choriamb, dactyl, dichoree, great ionic, iambus, pyrrhic, second epitrit, small ionic, spondee, tribrac, trochee'''
