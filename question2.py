from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
from transformers import AutoModel, AutoTokenizer
import json


from poly_llm.to_test.separate_paren_groups import separate_paren_groups, test_separate_fake_groups, test_separate_uni_groups, test_separate_paren_groups
from poly_llm.to_test.file_name_check import file_name_check, test_file_name_check, test_bad_format_name_check, test_good_format_name_check
from poly_llm.to_test.closest_integer import closest_integer, test_closest_integer,test_closest_sup_integer, test_closest_lower_integer
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade, test_numerical_letter_grade_frontier, test_numerical_letter_grade_frontier,test_numerical_letter_neg
from poly_llm.to_test.find_closest_elements import find_closest_elements, test_find_closest_elements, test_find_first_closest, test_last_first_closest
import inspect


model_name = "Salesforce/codet5-large-ntp-py"

# This function helps to generate test cases
def test_function(function, examples = None, model_name = model_name):
    executor = AbstractExecutor(function)
    prompt_generator = PromptGenerator(function)
    tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    llm_generator = LLMTestGenerator(model, tokenizer, function)
    prompt = prompt_generator.generate_prompt(few_shot_examples=examples)
    return  llm_generator.create_test_function(prompt)

def extract_few_shot(test_example):
  lines, _ = inspect.getsourcelines(test_example)
  lines = ''.join(lines)
  return lines


functions_to_test = [file_name_check, separate_paren_groups, closest_integer, numerical_letter_grade, find_closest_elements ]
for func in functions_to_test:
  test, test_name = test_function(func)
  f = open(f"./question_2_2/{test_name}.py", "w")
  f.write(test)
  f.close()